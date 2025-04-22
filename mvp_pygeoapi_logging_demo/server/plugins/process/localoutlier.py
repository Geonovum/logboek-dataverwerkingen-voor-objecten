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
from numpy import vstack
from sklearn.neighbors import LocalOutlierFactor

LOGGER = getLogger(__name__)

PROCESS_METADATA = {
    'version': '0.1',
    'id': 'localoutlier',
    'title': 'Local outlier factor (LOF)',
    'description': 'The local outlier factor (LOF) algorithm computes a score indicating the degree of abnormality of each input (observation), in a set of such observations. It measures the local density deviation of a given data point with respect to its neighbors. It considers as outliers the samples that have a substantially lower density than their neighbors.',
    'keywords': ['local outliter factor', 'LOF', 'outlier detection'],
    "jobControlOptions": [
				"sync-execute"
	],
    'links': [{
        'type': 'text/html',
        'rel': 'canonical',
        'title': 'information',
        'href': 'https://scikit-learn.org/stable/modules/outlier_detection.html#local-outlier-factor',
        'hreflang': 'en-US'
    }],
    'inputs':{
        'dataset':{
            'title': 'Dataset',
            'description': 'geojson dataset of points, in one CRS, for which LOF scores should be computed. ',
            "schema": { "type": "string", "format": "url" },
            'minOccurs': 1,
            'maxOccurs': 1,
            'keywords': ['geojson ogc api features', 'point data']
        },
        'n_neighbors':{
            'title': 'Number of neighbors',
            'description': 'Number of neighbors to use by default for `kneighbors` queries. If `n_neighbors` is larger than the number of samples provided, all samples will be used.',
            'minOccurs': 0,
            'maxOccurs': 1,
            'schema': {
                'oneOf': ['integer'],
                'defaultValue': 20,
            }
        }, 
        'leaf_size':{
            'title': 'Leaf size',
            'description': 'Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.',
            'minOccurs': 0,
            'maxOccurs': 1,
            'schema': {
                'oneOf': ['integer'],
                'defaultValue': 30,
            },
        }
        }, 
        'output_column':{
            'title': 'Output column name',
            'description': 'Name of the column in which to store output metric. If this column exists, an error will be thrown',
            'minOccurs': 0,
            'maxOccurs': 1,
            'schema': {
                'oneOf': ['string'],
                'defaultValue': 'abnormality',
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
#     SERVICE_NAME: "pygeoapi.process.localoutlier.LOFProcessor"
# })

# provider = TracerProvider(resource=resource)
# # processor = BatchSpanProcessor(ConsoleSpanExporter())
# processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://collector:4318/v1/traces"))
# provider.add_span_processor(processor)

# # Sets the global default tracer provider
# trace.set_tracer_provider(provider)

# # Creates a tracer from the global tracer provider
# tracer = trace.get_tracer("localoutlier.tracer")

# Parameters that are NOT passed directly to sklearn.neighbors.LocalOutlierFactor
LOF_OMIT = ['training_dataset', 'dataset', 'output_column']

class LOFProcessor(BaseProcessor):
    """Local outlier factor (LOF) processor"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.localoutlier.LOFProcessor
        """
        # Service name is required for most backends
        self.resource = Resource(attributes={
            SERVICE_NAME: "pygeoapi.process.localoutlier.LOFProcessor"
        })

        self.provider = TracerProvider(resource=self.resource)
        # processor = BatchSpanProcessor(ConsoleSpanExporter())
        self.processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://collector:4318/v1/traces"))
        self.provider.add_span_processor(self.processor)

        # # Sets the global default tracer provider
        # trace.set_tracer_provider(provider)

        # # Creates a tracer from the global tracer provider
        # tracer = trace.get_tracer("localoutlier.tracer")

        super().__init__(processor_def, PROCESS_METADATA)
    
    def execute(self, data):
        # Sets the global default tracer provider
        trace.set_tracer_provider(self.provider)

        # Creates a tracer from the global tracer provider
        tracer = trace.get_tracer("localoutlier.tracer")

        with tracer.start_as_current_span("LocalOutlierFactor") as span: #parent
            # create a parent log record
            span.set_attribute("dpl.objects.processing_activity_id", "https://algoritmes.overheid.nl/nl/algoritme/maaidata-provincie-noordholland/68294175")
            span.set_attribute("dpl.objects.dataproduct_id", "http://localhost:5000/collections/catalog/items/pygeoapi.process.localoutlier.LOFProcessor")
            
            dataset_info = [{
                
                    "dataset_id":"knmi_meetstations",
                    "dataset_def":"http://localhost:5000/collections/catalog/items/7b03a8de-5d0c-11ee-8a7e-3ce9f7462b93",
                    "dataset_port": "input"
                
            },
            { 
                "dataset_id":"n_neighbors",
                "dataset_def":"Number of neighbors to use by default for `kneighbors` queries.",
                "dataset_port": "input"
            },
            {
                "dataset_id":"output_dataset",
                "dataset_def": "geojson with an extra column: abnormality",
                "dataset_port": "output"
            }
            ]
            
            
            span.set_attribute("dpl.objects.dataset", str(dataset_info))
            span.set_status(Status(StatusCode.OK)) 

            data['p'] = int(data.get('p', 2))
            data['leaf_size'] = int(data.get('leaf_size', 30))
            data['n_neighbors'] = int(data.get('n_neighbors', 20))
            colName = data.get('output_column', 'abnormality')
            dataset = data.get("dataset")

            if dataset is None:
                raise ProcessorExecuteError('Cannot process without input dataset')
            
            #setup the sklearn classifier
            clf = LocalOutlierFactor(
                    novelty=False,
                    **{k:v for k,v in data.items()
                    if k not in LOF_OMIT}
                )
            predictMethod = clf.fit_predict

            gdf = gpd.read_file(dataset)
            X = vstack([gdf.geometry.x, gdf.geometry.y]).T

            #perform the actual classification
            y_pred = predictMethod(X)
            if colName in gdf.columns:
                raise Exception(f'{colName} exists in input and will not be overwritten')
            gdf[colName] = y_pred
            
            #loop through dataframe to create a logrecord for each object referring to the parent operation
            # for row in gdf.itertuples():
            #     # Create a nested span to track nested work
            #     with tracer.start_as_current_span("LocalOutlierFactor_items") as cs: #child
            #         cs.set_attribute("dpl.objects.data_object_id", row.STN)

            #timestamp does not serialize properly to json, so for now do a subset as workaround
            gdf_out = gdf[['STN','TYPE','geometry','abnormality']]
            mimetype = 'application/geo+json'
            outputs = {
                        'id': 'output_dataset',
                        'value': gdf_out.to_json()
                    }

            return mimetype, outputs

    def __repr__(self):
        return '<LOFProcessor> {}'.format(self.name)