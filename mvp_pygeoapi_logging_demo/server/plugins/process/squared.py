# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2023 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

#additional imports for opentelemetry
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)

LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'squared',
    'title': {
        'en': 'Squared processor'
    },
    'description': {
        'en': 'An example process that takes a number or integer and returns '
              'the squared result'
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['squared'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'number-or-integer': {
            'title': 'Number',
            'description': 'number or integer',
            'schema': {
                'oneOf': ['number', 'integer'],
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,  # TODO how to use?
            'keywords': ['number']
        }
    },
    'outputs': {
        'squared': {
            'title': 'Squared',
            'description': 'An example process that takes a number or '
                           'integer and returns the squared result',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'number-or-integer': 3
        }
    }
}

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "pygeoapi.process.squared.SquaredProcessor"
})

provider = TracerProvider(resource=resource)
# processor = BatchSpanProcessor(ConsoleSpanExporter())
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://collector:4318/v1/traces"))
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")

class SquaredProcessor(BaseProcessor):
    """Squared Processor example"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.squared.SquaredProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        sc = None
        value = None
        mimetype = 'application/json'
        number_or_integer = data.get('number-or-integer')

        if number_or_integer is None:
            raise ProcessorExecuteError('Cannot process without input')
        if not type(number_or_integer) in (int, float):
            raise ProcessorExecuteError('Input is not a number or integer')
        #TODO: handle logging when errors occur

        with tracer.start_as_current_span("calculate") as span:
            value = number_or_integer * number_or_integer
            span.set_attribute("squared.value", value)
            span.set_attribute("dpl.core.processing_activity_id", "http://localhost:5000/processes/squared")
            span.set_attribute("dpl.core.data_subject_id", 'not_set')
            span.set_status("STATUS_CODE_OK")

            sc = span.get_span_context()

            LOGGER.debug("get span control?")
            LOGGER.debug(sc)

            outputs = {
                'id': 'squared',
                'value': value
            }

            return mimetype, outputs

    def __repr__(self):
        return f'<SquaredProcessor> {self.name}'
