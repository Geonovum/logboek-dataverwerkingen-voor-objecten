from os import makedirs, path
from logging import getLogger


from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

#additional imports for opentelemetry
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.trace.propagation import set_span_in_context
from opentelemetry.trace import Status, StatusCode
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)
import json

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

# # Service name is required for most backends
# resource = Resource(attributes={
#     SERVICE_NAME: "http://aanvraag"
# })

# provider = TracerProvider(resource=resource)
# # processor = BatchSpanProcessor(ConsoleSpanExporter())
# processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://collector:4318/v1/traces"))
# provider.add_span_processor(processor)

# # Sets the global default tracer provider
# trace.set_tracer_provider(provider)

# # Creates a tracer from the global tracer provider
# tracer = trace.get_tracer("aanvraag.tracer")


class AanvraagProcessor(BaseProcessor):
   

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.aanvraag.AanvraagProcessor
        """
        # Service name is required for most backends
        self.resource = Resource(attributes={
            SERVICE_NAME: "http://aanvraag"
        })

        self.provider = TracerProvider(resource=self.resource)
        # processor = BatchSpanProcessor(ConsoleSpanExporter())
        self.processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://collector:4318/v1/traces"))
        self.provider.add_span_processor(self.processor)

        # # Sets the global default tracer provider
        # self.trace.set_tracer_provider(self.provider)

        # # Creates a tracer from the global tracer provider
        # self.tracer = self.trace.get_tracer("aanvraag.tracer")

        super().__init__(processor_def, PROCESS_METADATA)
    
    def execute(self, data):
                # Sets the global default tracer provider
        trace.set_tracer_provider(self.provider)

        # Creates a tracer from the global tracer provider
        tracer = trace.get_tracer("aanvraag.tracer")
        
        with tracer.start_as_current_span("Aanvraag_span") as span: #parent


            # create a parent log record
            span.set_attribute("dpl.core.processing_activity_id", "RVA: Aanvraag Kapvergunning")
            span.set_attribute("dpl.objects.processing_activity_id", 'http://localhost:5000/processes/aanvraag')
            span.set_status(Status(StatusCode.OK)) # does not work yet

            obj_id = int(data.get('object_id'))
            subj_name = data.get('subject_id', '')
            dataset = data.get("dataset")

            if dataset is None:
                raise ProcessorExecuteError('Cannot process without input dataset')
            

            gdf = gpd.read_file(dataset)

            
            gdf['kap_aanvraag'] = np.where(gdf['id'].astype(int) == obj_id, subj_name, '0')
            #In the 'simple' implementation we do not create a separate span for each feature, but log 1 activity with the list of all processed feature plus extra metadata tbd.
            
            span.set_attribute("dpl.objects.dataproduct_id", "http://localhost:5000/collections/catalog/items/pygeoapi.process.aanvraag.AanvraagProcessor")
            feature_info = [
            {
                "feature_id" : "boom",
                "feature_def" : "http://brt.basisregistraties.overheid.nl/id/concept/Boom",
                "feature_port" : "input"
            },
            # {
            #     "feature_id" : "boom",
            #     "feature_def" : "https://metadata.simulatie.datastelsel.nl/detailview?resourceId=http:%2F%2Fbrk.basisregistraties.overheid.nl%2Fid%2Fbegrip%2FNatuurlijk_persoon&resourceType=begrippen&resourceLabel=Human%20person",
            #     "feature_port" : "output"
            # }
            ]
            
            feature_attribute = [
                {
                    "attribute_name" : "id",
                    "attribute_value" : obj_id,
                    "attribute_def" : "http://localhost:5000/collections/bomen/items"
                },
                # {
                #     "attribute_name" : "subject_id",
                #     "attribute_value" : subj_name,
                #     "attribute_def" : "input waarde van beoordelingsprocedure"
                # }
            ]

            dataset_info = [{
                    "dataset_id":"bomen",
                    "dataset_def":"http://localhost:5000/collections/catalog/items/7b03a8de-5d0c-11ee-8a7e-3ce9f7462b83",
                    "dataset_port": "input",
                    "feature": feature_info,
                    "feature_attribute" : feature_attribute
            }]

            span.set_attribute("dpl.objects.dataset", json.dumps(dataset_info, ensure_ascii=False))

            


            # span.set_attribute("dpl.objects.feature", str(feature_attribute))
            
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