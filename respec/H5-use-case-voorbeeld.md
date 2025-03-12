# Voorbeeld implementatie (MVP)

In de [github repository](https://github.com/Geonovum/logboek-dataverwerkingen-voor-objecten/tree/main/mvp_pygeoapi_logging_demo) staat een Minimal Viable Product (MVP) waarin 
gedemonstreerd wordt hoe het opentelemetry protocol geimplementeerd kan worden in een OGC API Processes functie.

## Use-cases volwassenheidsniveaus

Om de eigenschappen voor de (geo)objecten extensie goed uit te werken helpt het om te kijken naar een aantal voorbeelden en wat er dan gewenst is om vast te leggen.

### Remote Sensing gebiedsclassificatie op basis van AI beeldherkenning ​

Dit is een voorbeeld waarbij een organisatie remote sensing beelden met AI Beeldherkenning verwerkt om gebieden te classificeren. Bijvoorbeeld om natuurgebieden te identificeren. 
In dit geval is er niet direct een betrokkene aan te wijzen (uiteindelijk heeft het gebied natuurlijk wel een eigenaar, maar die is niet betrokken bij de identificatie van het gebied). 
Het is wel van belang om vast te leggen met welke batch remote sensing beelden deze analyse is uitgevoerd en welk algoritme gebruikt is. Beeldkwaliteit door bijvoorbeeld bewolking of 
een defect aan een sensor kunnen de classificatie beinvloed hebben en dan wil je weten voor welke gebieden dit gevolgen heeft gehad.

Dit kan als Niveau 2: 'kolomverwijzing' beschouwd worden. Met dien verstande dat er verwezen wordt naar het type remote sensing data (bv Sentinel-2, LIDAR) en niet de gebruikte beeldwaarden 
van de remote sensing beelden. Er dient wel metadata van het gebruikte dataproduct vastgelegd te worden (timestamp, series) of een identifier die het specifieke dataproduct uniek identificeert.


- dpl.object.processing_activity_id
- dpl.objects.dataproduct [
    - dataproduct_id
    - dataproduct_def
]
### Maaidata analyse, remote sensing beelden analyseren of percelen wel/niet gemaaid zijn​

Dit is een voorbeeld van het verwerken van satellietbeelden om te signaleren of graslanden worden gemaaid tijdens het broedseizoen van beschermde vogelsoorten. 
Dit toezicht is van belang in verband met subsidieverstrekking voor natuurvriendelijk beheer. In deze analyse worden zowel remote sensingbeelden gebruikt als percelen. 
Het resultaat van de analyse heeft een direct gevolg voor de eigenaar (betrokkene) van het perceel. (los van het feit dat er in de implementatie van het algoritme wel een menselijke check plaatsvindt)
Afhankelijk van de implementatie kan het ook nog zo zijn dat de analyse van de percelen zodanig gedaan wordt dat hier een betrokkene nog niet rechtstreeks te achterhalen is.

Dit kan als Niveau 2: 'kolomverwijzing' gelogd worden, maar zou ook als Niveau 3: 'concrete data' geimplementeerd kunnen worden.

Niveau 2:

- dpl.core.processing_activity_id (verwijzing naar de subsidieverlening)
- dpl.core.data_subject_id (indien bekend in de verwerking van percelen)
- dpl.object.processing_activity_id (verwijzing naar het algoritmeregister)
- dpl.objects.dataproduct [
    - dataproduct_id
    - dataproduct_def
]

Niveau 3:

- dpl.core.processing_activity_id (verwijzing naar de subsidieverlening)
- dpl.core.data_subject_id (indien bekend in de verwerking van percelen)
- dpl.object.processing_activity_id (verwijzing naar het algoritmeregister)
- dpl.objects.dataproduct [
    - dataproduct_id 
    - dataproduct_def
    - feature [
        - feature_id
        - feature_def
    ]
    - feature_attribute [
        - attribute_name
        - attribute_value
    ]
]
​

### Aanvraag kapvergunning​

Dit is een (fictief) voorbeeld waar een betrokkene een aanvraag voor een kapvergunning indient. Hierbij moet beoordeeld worden of de betreffende boom gekapt mag worden, of bijvoorbeeld een monumentale status heeft.
In dit geval is er zowel een betrokkene en een activiteit in het register van verwerkingsactiviteiten, als een aanwijsbaar object (de boom). 

Dit kan zowel als Niveau 2: 'kolomverwijzing', maar ook als Niveau 3: 'concrete data' gelogd worden. Waarbij het mogelijk wel voor de hand ligt om Niveau 3 te kiezen omdat de boom direct aanwijsbaar is.

Niveau 3:

- dpl.core.processing_activity_id (verwijzing naar de subsidieverlening)
- dpl.core.data_subject_id (indien bekend in de verwerking van percelen)
- dpl.object.processing_activity_id (verwijzing naar het algoritmeregister)
- dpl.objects.dataproduct [
    - dataproduct_id 
    - dataproduct_def
    - feature [
        - feature_id
        - feature_def
    ]
    - feature_attribute [
        - attribute_name
        - attribute_value
    ]
]


## Use-cases implementatie in een Digitale Tweeling

Naast het MVP voorbeeld en de use-cases ter verdieping van de requirements voor de extensie doen we ook een beproeving in de implementatie in een Digitale Tweeling systeem. 
Deze beproeving dient vooral om de context zoals die in [2.4.1](./H2-architectuur.md#implementatie-keuzes) is beschreven beter te begrijpen.

TODO: resultaat Testbed2 verwerken