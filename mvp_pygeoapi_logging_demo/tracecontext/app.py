from flask import Flask
import requests
from opentelemetry import trace, baggage
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor

app = Flask(__name__)

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

tracer = trace.get_tracer(__name__)

# Dit is de applicatie die de aanroep van app2 doet. Deze app is te benaderen in de browser op localhost:5002

@app.route('/')
def hello():
    with tracer.start_as_current_span("api1_span") as span:
        
        headers = {}
        # ctx = baggage.set_baggage("hello", "world")
        # TraceContextTextMapPropagator().inject(headers, ctx)
        # inject pakt automatisch de huidige context om in de header te plaatsen
        TraceContextTextMapPropagator().inject(headers)

        print(headers)

        response = requests.get('http://127.0.0.1:5001/', headers=headers)
        return f"Hello from API 1! Response from API 2: {response.text}"

if __name__ == '__main__':
    app.run(port=5002)