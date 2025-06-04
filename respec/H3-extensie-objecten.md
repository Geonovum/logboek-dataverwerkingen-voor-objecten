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

service.name = Logical name of the service
service.instance.id = The string ID of the service instance

Overeenkomstig de Opentelemetry specificatie.

Elk individueel Dataproduct/proces krijgt een eigen naam en id. Dus als er meerdere algoritmes/processen op een server zijn geimplementeerd moet de service.name op het niveau van
het individuele product/proces geinstantieerd worden.

__trace__

```
dpl.objects.algorithm_id
dpl.objects.dataproduct_id 
dpl.objects.dataset [
    dataset_id
    dataset_def
    dataset_port
    feature [
        feature_id
        feature_def
        feature_port
    
        feature_attribute [
            attribute_name
            attribute_value
            attribute_def
        ]
    ]   
]
```

| attribute | Niveau |beschrijving |
|---|---|---|
|dpl.objects.algorithm_id | 1 | verwijzing naar het register van het betreffende algoritme. uri naar uniek identificeerbaar algoritme| 
|dpl.objects.dataproduct_id  | 1 | uri naar een catalogus met de dataproduct metadata |
|dpl.objects.dataset | 2a | lijst met datasets (input en/of output van het dataproduct) | 
|   dataset_id | 2a | unieke id van de dataset |
|   dataset_def | 2a | uri naar de definitie/metadata van de dataset (catalog_record/dcat_ap_nl) |
|   dataset_port | 2a | input/output dataset, dit wordt in de log vastgelegd omdat het niet noodzakelijk uit de metadata in de catalogus afgeleid kan worden |
|   feature | 2b | lijst met features: | 
|     feature_id | 2b | unieke id van het feature| 
|     feature_def | 2b | uri naar een definitie van het feature|
|     feature_port | 2b | input/output feature, dit wordt in de log vastgelegd omdat het niet noodzakelijk uit de metadata in de catalogus afgeleid kan worden|
|   feature_attribute | 3 | lijst van attributen van het feature |
|     attribute_name | 3 | unieke identifier van het attribuut |
|     attribute_value | 3 | waarde van het attribuut in de specifieke verwerking / logregel | 
|     attribute_def | 3 | verwijzing naar de metadata van het attribuut |

Afhankelijk van het volwassenheidsniveau wordt er meer gelogd. Voor de hogere niveaus geldt dat de gegevens van het lagere niveau ook gelogd worden.

Voor niveau 2 (kolomniveau) geldt dat er op gehele dataset gelogd kan worden (2a), of dat er specifiek aangegeven kan worden welke features in een dataset gebruikt zijn (2b).


---