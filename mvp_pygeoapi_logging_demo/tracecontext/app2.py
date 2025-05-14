from flask import Flask, request
from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor
import json

app = Flask(__name__)

resource = Resource(attributes={
            SERVICE_NAME: "http://app2"
        })

trace.set_tracer_provider(TracerProvider(resource=resource))
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

tracer = trace.get_tracer(__name__)

# Dit is de applicatie die aangeroepen wordt door 'app', het enige wat deze doet is "Hello from API 2!" terug sturen...

@app.route('/')
def hello():
    # Example: Log headers received in the request in API 2
    headers = dict(request.headers)
    print(f"Received headers: {headers}")
    carrier ={'traceparent': headers['Traceparent']}
    ctx = TraceContextTextMapPropagator().extract(carrier=carrier)
    print(f"Received context: {ctx}")

  
    # Dit is een implementatiekeuze:
    # Start je een nieuwe span in de trace context (met hetzelde trace_id) van app
    
    # with tracer.start_span("api2_span", context=ctx):
    
    # of start je een 'eigen' trace (met een nieuw trace_id)
    with tracer.start_as_current_span("api2_span") as span:

        # in dat geval leggen we het originele trace_id vast in een attribuut: foreign_operation.trace_id
        parent_trace_id = trace.get_current_span(context=ctx).get_span_context().trace_id
        foreign_operation = {
          "trace_id" : f"0x{parent_trace_id:032x}"
        }
        span.set_attribute("foreign_operation", json.dumps(foreign_operation))
        
        return "Hello from API 2!"

if __name__ == '__main__':
    app.run(port=5001)
