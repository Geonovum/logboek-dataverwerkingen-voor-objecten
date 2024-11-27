# MVP Pygeoapi voorbeeld met Opentelemetry logging

In deze folder staat een MVP demo met een pygeoapi server die via het opentelemetry protocol logt naar een OTLP Collector.

## server

Met het commando `docker compose up` worden 2 containers gestart.

Beide containers loggen naar de commandline (dus de containers niet 'detached' opstarten want dan zie je niks gebeuren)

Als de containers gestart zijn is pygeoapi beschikbaar op http://localhost:5000

De opentelemetry collector logt alleen naar de commandline.

### config

- otel-collector-config.yaml
minimale configuratie van een opentelemetry collector om traces te ontvangen van pygeoapi en naar de console te loggen

- pygeoapi.config.yaml
de benodigde configuratie van de pygeoapi server

- docker-compose.yml
de orchestratie van de docker containers.
  - de pygeoapi container is gebaseerd op het base image van pygeo, maar aangevuld met python libraries uit de requirements.txt
  - de pygeoapi container krijgt de /data en /plugin folders mee waar de data en de functies staan

## client

Via een Jupyter notebook kunnen de beschikbare OGC API Processes functies aangeroepen worden.

Hiervoor is een python omgeving nodig met jupyter notebook, requests, geopandas en eventueel folium.
