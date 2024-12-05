# PROV-O mapping

In deze folder bevinden zich wat werkbestanden om de potentiele prov-o mapping te doen van een opentelemetry trace.

Deze bestanden zijn nog in concept, er is geen enkele garantie dat deze mapping juist is en of de implementatie werkt.

## bestanden

- tempo-query.ipynb is een jupyternotebook om de api van een grafana tempo backend aan te spreken om opentelemetry tracedata op te halen.

- otel_rml_map.ttl is een RML mapping file om de JSON data te converteren naar RDF/Turtle met RMLMapper.
    zie [https://rml.io/docs/rml/introduction/](https://rml.io/docs/rml/introduction/) voor informatie over RML

    `java -jar rmlmapper-7.1.2-r374-all.jar -m otel_rml_map.ttl -o trace-prov.ttl`

- trace-prov.ttl is het voorlopige resultaat uit de RMLMapper
