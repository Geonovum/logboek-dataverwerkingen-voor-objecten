# Extensie (geo)objecten

Het loggen van (geo)objecten is een bijzonder ruim en daarmee flexibel onderwerp. Er zijn zeer veel mogelijke scenario's, afhankelijk van de gebruikte data, 
het type analyse of algoritme en het gewenste volwassenheidsniveau.

We nemen een paar uitgangspunten op om de scope te verduidelijken.

<aside class="note">

Deze uitgangspunten moeten nog getoetst worden in de praktijk.

De kans is groot dat theorie en praktijk uit elkaar blijven lopen. Bijvoorbeeld voor wat betreft het abstractieniveau waarop een algoritme in een algoritmeregister is 
beschreven en de daadwerkelijke implementatie in een systeem en de (technische) mogelijkheiden om logging te implementeren.

</aside>

1. Input/output poorten conform het idee van 'Dataproducten' als uitgangspunt voor de afbakening van het proces wat wordt gelogd.
2. API specificatie van een proces (als het goed is gelijk aan 1.)


In de Logboek dataverwerkingen standaard wordt de OTLP standaard aanbevolen om de [interface](https://logius-standaarden.github.io/logboek-dataverwerkingen/#interface) 
naar het logboek mee te implementeren.

De OTLP standaard kent een aantal categorieën om telemetrie vast te leggen. Voor de Logboek dataverwerkingen standaard wordt de [traces](https://opentelemetry.io/docs/concepts/signals/traces/) categorie gebruikt.
Op het 'hoogste' niveau kent de standaard ook nog het concept [resource](https://opentelemetry.io/docs/concepts/resources/).

Bij het opzetten van een logboek dataverwerkingen interface kan er dus informatie op het niveau van resource vastgelegd worden. Dit is typisch informatie over het systeem waar de betreffende logging vandaan komt.

De traces zijn vervolgens de individuele verwerkingen die door het betreffende systeem gedaan worden.

__resource__

service.name = \<servicenaam\>

__trace__

```
dpl.object.processing_activity_id
dpl.objects.dataproduct [
    dataproduct_id 
    dataproduct_def
    feature [
        feature_id
        feature_def
    ]
    feature_attribute [
        attribute_name
        attribute_value
    ]
]
```

| attribute | beschrijving |
|---|---|
|dpl.object.processing_activity_id | verwijzing naar het register van het betreffende algoritme. uri naar uniek identificeerbaar algoritme| 
|dpl.objects.dataproduct  | lijst met dataproducten: |
|   dataproduct_id | unieke id voor het dataproduct. uri naar de service/downloadurl van het product | 
|   dataproduct_def | uri naar een catalogus met de dataproduct (dataset) metadata | 
|   feature | lijst met features: | 
|     feature_id | unieke id van het feature| 
|     feature_def | uri naar een definitie van het feature|
|   feature_attribute | lijst van attributen van het feature |
|     attribute_name | unieke identifier van het attribuut |
|     attribute_value | waarde van het attribuut in de specifieke verwerking / logregel | 
|     attribute_def | verwijzing naar de metadata van het attribuut |


---