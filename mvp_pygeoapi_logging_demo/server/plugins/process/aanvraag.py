from os import makedirs, path
from logging import getLogger


from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

#additional imports for opentelemetry
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.trace import Status, StatusCode
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)

import geopandas as gpd
import numpy as np

LOGGER = getLogger(__name__)

PROCESS_METADATA = {
    'version': '0.1',
    'id': 'aanvraag',
    'title': 'Aanvraag kapvergunning',
    'description': 'Demo om persoonsgegeven en object samen te loggen',
    'keywords': ['aanvraag', 'kapvergunning', 'otel demo'],
    "jobControlOptions": [
				"sync-execute"
	],
    # 'links': [{
    #     'type': 'text/html',
    #     'rel': 'canonical',
    #     'title': 'information',
    #     'href': 'https://scikit-learn.org/stable/modules/outlier_detection.html#local-outlier-factor',
    #     'hreflang': 'en-US'
    # }],
    'inputs':{
        'dataset':{
            'title': 'Dataset',
            'description': 'geojson dataset of points, in one CRS. ',
            "schema": { "type": "string", "format": "url" },
            'minOccurs': 1,
            'maxOccurs': 1,
            'keywords': ['geojson ogc api features', 'point data']
        },
        'object_id':{
            'title': 'The object id for which a permit is requested',
            'description': 'The object id for which a permit is requested.',
            'minOccurs': 0,
            'maxOccurs': 1,
            'schema': {
                'oneOf': ['integer'],
                # 'defaultValue': 20,
            }
        }, 
        'subject_id':{
            'title': 'The subject id',
            'description': 'ID of the person requesting the permit',
            'minOccurs': 0,
            'maxOccurs': 1,
            'schema': {
                'oneOf': ['string'],
                # 'defaultValue': 30,
            },
        },
    },
    'outputs': {
        'output_dataset':{
            'title': 'Output Dataset',
            'description': 'output',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
                }
            },
    },
    'example': {}
}

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "http://localhost:5000/processes/aanvraag"
})

provider = TracerProvider(resource=resource)
# processor = BatchSpanProcessor(ConsoleSpanExporter())
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://collector:4318/v1/traces"))
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("aanvraag.tracer")


class AanvraagProcessor(BaseProcessor):
   

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.aanvraag.AanvraagProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)
    
    def execute(self, data):
        with tracer.start_as_current_span("Aanvraag_span") as span: #parent
            # create a parent log record
            span.set_attribute("dpl.objects.processing_association_id", "http://localhost:5000/processes/aanvraag")
            span.set_attribute("dpl.core.processing_activity_id", "RVA: Aanvraag Kapvergunning")
            # span.set_attribute("dpl.objects.data_association_id", 'not_set')
            span.set_status(Status(StatusCode.OK)) # does not work yet

            obj_id = int(data.get('object_id'))
            subj_name = data.get('subject_id', '')
            dataset = data.get("dataset")

            if dataset is None:
                raise ProcessorExecuteError('Cannot process without input dataset')
            

            gdf = gpd.read_file(dataset)

            
            gdf['kap_aanvraag'] = np.where(gdf['id'].astype(int) == obj_id, subj_name, '0')
            #In the 'simple' implementation we do not create a separate span for each feature, but log 1 activity with the list of all processed feature plus extra metadata tbd.
            
            span.set_attribute("dpl.objects.data_object_id", obj_id)
            span.set_attribute("dpl.objects.data_object_def", "http://localhost:5000/collections/bomen/queryables?f=json")
            span.set_attribute("dpl.core.data_subject_id", subj_name)
            #timestamp does not serialize properly to json, so for now do a subset as workaround
            gdf_out = gdf[['id','leaf_type','geometry','species:nl','kap_aanvraag']]
            mimetype = 'application/geo+json'
            outputs = {
                        'id': 'output_dataset',
                        'value': gdf_out.to_json()
                    }

            return mimetype, outputs

    def __repr__(self):
        return '<AanvraagProcessor> {}'.format(self.name)