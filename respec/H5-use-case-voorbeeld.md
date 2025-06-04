#  Implementaties 

## MVP met pygeoapi

In de [github repository](https://github.com/Geonovum/logboek-dataverwerkingen-voor-objecten/tree/main/mvp_pygeoapi_logging_demo) staat een Minimal Viable Product (MVP) waarin 
gedemonstreerd wordt hoe het opentelemetry protocol geimplementeerd kan worden in een OGC API Processes functie.

__Use-cases volwassenheidsniveaus__

Om de eigenschappen voor de (geo)objecten extensie goed uit te werken helpt het om te kijken naar een aantal voorbeelden en wat er dan gewenst is om vast te leggen.

### Remote Sensing gebiedsclassificatie op basis van AI beeldherkenning ​

Dit is een voorbeeld waarbij een organisatie remote sensing beelden met AI Beeldherkenning verwerkt om gebieden te classificeren. Bijvoorbeeld om natuurgebieden te identificeren. 
In dit geval is er niet direct een betrokkene aan te wijzen (uiteindelijk heeft het gebied natuurlijk wel een eigenaar, maar die is niet betrokken bij de identificatie van het gebied). 
Het is wel van belang om vast te leggen met welke batch remote sensing beelden deze analyse is uitgevoerd en welk algoritme gebruikt is. Beeldkwaliteit door bijvoorbeeld bewolking of 
een defect aan een sensor kunnen de classificatie beinvloed hebben en dan wil je weten voor welke gebieden dit gevolgen heeft gehad.

Dit kan als Niveau 2: 'kolomverwijzing' beschouwd worden. Met dien verstande dat er verwezen wordt naar het type remote sensing data (bv Sentinel-2, LIDAR) en niet de gebruikte beeldwaarden 
van de remote sensing beelden. Er dient wel metadata van het gebruikte dataproduct vastgelegd te worden (timestamp, series) of een identifier die het specifieke dataproduct uniek identificeert.

minimale implementatie:

- dpl.objects.algorithm_id
- dpl.objects.dataproduct_id

uitgebreidere implementatie:

- dpl.objects.algorithm_id
- dpl.objects.dataproduct_id
- dpl.objects.dataset[
    - dataset_id
    - dataset_def
    - dataset_port (input)

],
- dpl.objects.dataset[
    - dataset_id
    - dataset_def
    - dataset_port (output)

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
- dpl.objects.algorithm_id (verwijzing naar het algoritmeregister)
- dpl.objects.dataproduct_id 
- dpl.objects.dataset[
    - dataset_id
    - dataset_def
    - dataset_port 
]

Niveau 3:

- dpl.core.processing_activity_id (verwijzing naar de subsidieverlening)
- dpl.core.data_subject_id (indien bekend in de verwerking van percelen)
- dpl.objects.algorithm_id (verwijzing naar het algoritmeregister)
- dpl.objects.dataproduct_id
- dpl.objects.dataset[
    - dataset_id 
    - dataset_def
    - dataset_port
    - feature [
        - feature_id
        - feature_def

        - feature_attribute [
            - attribute_name
            - attribute_value
            - attribute_def
        ]
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
- dpl.objects.algorithm_id (verwijzing naar het algoritmeregister)
- dpl.objects.dataproduct_id
- dpl.objects.dataset [
    - dataset_id 
    - dataset_def
    - dataset_port
    - feature [
        - feature_id
        - feature_def
        - feature_port

        - feature_attribute [
            - attribute_name
            - attribute_value
            - attribute_def
        ]
    ]
]


## Implementatie in Digitale Tweelingen Tooling

Naast het MVP voorbeeld en de use-cases ter verdieping van de requirements voor de extensie doen we ook een beproeving in de implementatie in Digitale Tweeling systemen. 
Deze beproeving dient vooral om de context zoals die in [2.4.1](#implementatie-keuzes) is beschreven beter te begrijpen.

### Vraagstukken

- Kunnen we de logging standaard implementeren in de tooling van de leveranciers
- Kunnen we met de aanroep van API's tussen de systemen ook de tracecontext meegeven zodat logs aan elkaar te relateren zijn
- Kunnen we de rekenmodellen die in de systemen gebruikt worden goed genoeg vastleggen in het algoritmeregister en kunnen we daar dan naar verwijzen

### uitgewerkte scenarios

De scenarios worden geplaatst in de context van de [NLDT architectuur](https://geonovum.github.io/NLDT-Architectuur/). 
Deze architectuur kent een basispatroon zoals getoond in de volgende afbeelding:

<img src="./respec/media/architectuur_driehoek.png" alt="Basis bouwblokken NLDT Architectuur" width="900">



#### Imagem

De Planspace Simulator software van Imagem wordt hier gebruikt als visualisatie component, waarbij rekenmodules van Nelen & Schuurmans, en Tygron worden aangeroepen.
In de user interface van Imagem wordt een knop getoond waarmee een 'besluit' vastgelegd kan worden. De stappen om dit besluit vast te leggen bestaan uit het laden van de relevante data lagen, het aanroepen van een rekenmodel, het tonen van het resultaat van het rekenmodel en het vastleggen van de conclusie die uit de resultaten getrokken worden. 

<img src="./respec/media/diagram-logging.png" alt="logging flow in Planspace Simulator" width="900">



Er wordt dus een logfile aangelegd waarbij de verschillende stappen als 'spans' vastgelegd worden. De aanroep van het rekenmodel initieert het aanleggen van een logfile op het platform van het rekenmodel, waarbij de tracecontext meegegeven wordt om de losse logfiles in een later stadium aan elkaar te kunnen relateren.

Een voorbeeld van de log zoals deze door Imagem is vastgelegd is [hier](https://github.com/Geonovum/logboek-dataverwerkingen-voor-objecten/blob/main/codesprint-resultaten/trace-imagem.json) te vinden.

Er zijn hierbij 2 verschillende implementaties gedaan:
- De aanroep van het hittestress model van Tygron wordt synchroon gedaan (het visualisatie platform 'wacht op antwoord' en doet niets in de tussentijd).
- De aanroep van het overstromingsmodel van Nelen & Schuurmans wordt asynchroon gedaan (het visualisatie platform kan in de tussentijd doorgaan met andere activiteiten en krijgt op een later moment een melding van het resultaat van het rekenmodel).

#### Nelen & Schuurmans

In de uitgewerkte scenarios acteert het 3Di platform van Nelen & Schuurmans als rekemodel voor overstromingsberekeningen. (Nelen & Schuurmans heeft ook een eigen visualisatie component, maar dat is in dit scenario niet ingezet).

De aanroep van het Imagem Planspace Simulator platform resulteert in het aanleggen van een logfile van de berekening, waarbij het trace_id van de aanroepende applicatie vastgelegd wordt om de logfiles op een later moment aan elkaar te kunnen relateren.

Er is hierbij gekeken naar het implementeren van de verschillende [volwassenheidsniveaus](#volwassenheidsniveaus) van logging en de wijze waarop een hoger volwassenheidsniveau (2/3) gelogd zou kunnen worden.

- de eerste implementatie is de mogelijkheid om in de log de uitgevoerde stappen te loggen op basis van de specificatie in dit document.
- de tweede implementatie is de mogelijkheid om in de log te verwijzen naar de interne log van het 3Di systeem, waar toch al alle details vastgelegd worden.

Het voordeel van de eerste implementatie is de vastlegging in de log ten behoeve van de verantwoording, maar dit vraagt extra implementatie inspanning en veroorzaakt dubbele logging.
Het voordeel van de tweede implementatie is dat deze logging toch al gedaan wordt en alles bevat om een complete 'replay' van het model uit te voeren. Dit is alleen wel een platform specifieke implementatie en daarmee minder direct toegangkelijk voor verantwoording.

Een voorbeeld van de log zoals deze door Nelen & Schuurmans is vastgelegd is [hier](https://github.com/Geonovum/logboek-dataverwerkingen-voor-objecten/blob/main/codesprint-resultaten/trace-nelen_schuurmans.json) te vinden.

Behalve de implementatie van de logging heeft Nelen & Schuurmans ook een Proof-of-Concept opgeleverd van een 'logviewer', een applicatie om de verschillende logfiles aan elkaar te relateren en een integraal beeld te geven van de gevolgde stappen.

<img src="./respec/media/otel-trace-viewer.png" alt="Demo viewer that aggregates different trace files" width="900">

#### Tygron

Het platform van Tygron is ingezet als rekenmodel, waarbij de aanroep vanuit het Imagem Planspace Simulator platform gebeurt. Hier wordt een logfile aangelegd waarbij het trace_id vanuit de aanroepende applicatie vastgelegd wordt om de logfiles op een later moment aan elkaar te kunnen relateren. In deze implementatie is vooral gekeken naar de compleetheid van de attributen zoals die gedefinieerd zijn in deze specificatie. 

Een voorbeeld van de log zoals deze door Tygron is vastgelegd is [hier](https://github.com/Geonovum/logboek-dataverwerkingen-voor-objecten/blob/main/codesprint-resultaten/trace-tygron.json) te vinden.

Daarnaast is er een scenario uitgewerkt waarbij het Tygron platform gebruikt wordt als zowel visualisatie component en als rekenmodel. Dit scenario onderstreept het verschil in benadering van het gebruik van een digitale tweeling toepassing en het vastleggen van een besluit vanuit het oogpunt van de verantwoording.

### Bevindingen

Tijdens het implementeren in de tooling zijn de volgende onderwerpen naar boven gekomen.

#### Verschil in invalshoek tussen loggen vanuit verantwoording en gebruik van Digitale Tweeling platformen

Een van de belangrijkste vraagstukken tijdens de implementatie was de 'variabiliteit' waarvoor een digitale tweeling platform ingezet wordt. Er is in de regel niet een specifiek vastegelegd werkproces of stappenplan om tot een bepaalde beleidsbeslissing te komen. Hiermee wordt het ingewikkeld om in de logging specifiek af te bakenen welk deel te relateren is aan een specifiek algoritme of het tot stand komen van een besluit.

Dit is geadresseerd door in het platform van Imagem een specifieke knop te maken die het stappenplan tot het nemen van een besluit initieert. Of dit in de praktijk werkt, is niet verder onderzocht.

Ter illustratie is in het platform van Tygron een log aangelegd die de standaard gang van zaken van het gebruik van het platform logt. (initieren omgeving, laden data, laden modellen, uitvoeren scenarios, visualiseren resultaten). 

#### Verantwoording, transparantie en herleidbaarheid

De Logboek dataverwerkingen standaard redeneert sterk vanuit de juridische beleidscontext en de verantwoording van dataverwerkingen op basis hiervan. 
Voor de scope van de originele standaard past dit goed bij het registreren van verwerkingen op basis van het register van verwerkingsactiviteiten gerelateerd aan persoonsgegevens.

In de praktijk blijkt het niet triviaal om de dynamiek van het werken met Digitale Tweelingen eenduidig aan specifieke dataverwerkingen te relateren (zie ook 5.2.3.1), de term verantwoording lijkt dan niet altijd passend. De transparantie en herleidbaarheid van dataverwerkingen in de verschillende platformen wordt echter wel als heel belangrijk beschouwd. De platformen hebben in de praktijk dus veelal logging ingebouwd om dataverwerkingen te kunnen herleiden en inzicht te geven in de gevolgde stappen. 

#### Doelgroep voor Logging

Het inzicht dat de Logboek dataverwerkingen standaard geeft in de context van de AVG is in principe rechtstreeks relevant voor betrokken personen. In de scenarios die uitgewerkt zijn in de fysieke leefomgeving zijn de expert modellen die gebruikt worden een stuk lastiger te interpreteren. Het ontsluiten van deze logs zou daarom misschien niet rechtstreeks naar burgers moeten zijn, maar naar 'experts' die de context van het model kunnen interpreteren.

#### Tracecontext - 1 overkoepelend ID of per systeem een eigen Trace ID

Bij het implementeren van de tracecontext over systemen heen kwam een onduidelijkheid in de specificatie naar boven. Het standaard gedrag van een OpenTelemetry SDK implementatie is het overnemen van hetzelfde trace_id in de verschillende applicaties. In de [LDV Specificatie](https://logius-standaarden.github.io/logboek-dataverwerkingen/#interface) staat dat de applicatie van een andere organisatie het trace_id van de aanroepende applicatie moet vastleggen in een 'foreign_operation.trace_id'. Dit kan geïmplementeerd worden maar vergt een specifieke implementatie, afwijkend van het standaard gedrag.

#### Granulariteit van verantwoording - Register vs modules in de tooling

Bij het bepalen van het [afwegingskader](#afwegingskader) voor de implementatie van de logboek dataverwerkingen voor (geo) objecten standaard is gekozen om te verwijzen naar het Algoritmeregister. Er zijn [3 algoritmes](https://algoritmes.overheid.nl/nl/algoritme?page=1&organisation=Stichting+Geonovum) opgenomen in het Algoritmeregister ten behoeve van dit onderzoek. 

Tijdens de implementatie van de logging in de platformen blijkt dat er vaak meerdere stappen gerelateerd zijn aan het algoritme zoals dat vastgelegd is in het register. Dit geeft ruimte voor interpretatieverschillen welke stappen wel of niet onderdeel zijn van het algoritme zoals het geregistreerd staat in het register.

#### Dynamiek in gebruik van Digitale Tweeling systemen

Het Digitale Tweelingen ecosysteem werkt toe naar een omgeving waar organisaties 'naar behoefte' een rekenmodel aan kunnen roepen als SaaS (Software as a Service) dienst. Dit roept het vraagstuk op dat een rekenmodel leverancier (zoals Nelen & Schuurmans of Tygron) van te voren niet noodzakelijk weten welke organisaties een dienst gaan afnemen. Om toch een log vast te kunnen leggen van verwerkingen in de context van een vooraf nog onbekende organisatie moet er het nodige geregeld worden in de wijze waarop de SaaS dienst aangeboden wordt. De consequenties hiervan zijn op dit moment nog onduidelijk.

#### Loggen in LDV log of verwijzen naar systeemlog

De rekenmodellen leggen standaard in hun implementaties al een uitgebreide log aan waarmee de scenarios opnieuw opegebouwd of afgespeeld kunnen worden. Dit is leverancier specifiek ingericht. De platformen zijn zeer flexibel en dynamisch ingericht waardoor het niet triviaal is om vast te leggen welke gegevens er op een gegeven moment betrokken zijn bij het komen tot een besluit. Om al deze gegevens in de logboek dataverwerkingen voor (geo) objecten standaard vast te leggen is daarmee ook een complexe opgave. De vraag dient zich aan of de hogere volwassenheidsniveaus haalbaar zijn om te implementeren, en of het verwijzen naar de implementatiespecifieke systeemlogs een oplossing zou kunnen zijn. 

#### Granulariteit in het Algoritmeregister / juridische kaders

De Algoritmes zoals deze nu in het Algoritmeregister zijn vastgelegd kunnen op basis van [verschillende wettelijke grondslagen ingezet worden](https://algoritmes.overheid.nl/nl/algoritme/modelleringssoftware-hittestress-stichting-geonovum/21577420#verantwoordGebruik). Hittestress kan bijvoorbeeld zowel een onderwerp zijn in het kader van planvorming en vergunningverlening in het kader van de omgevingswet, maar het kan ook onderdeel zijn van het monitoren van gevaarlijke situaties op basis van de algemene wet bestuursrecht.

De vraag dient zich dus aan of, en op welke wijze we dat onderscheid kunnen maken in de logging in de applicaties. Mogelijk is hierdoor alsnog onvoldoende duidelijk op welke gronden besluiten genomen zijn en daarmee neemt de waarde van de logging significant af. 

Een mogelijke oplossing zou kunnen zijn om een extra eigenschap op te nemen in de logging om expliciet te maken in het kader van welke wet een bepaalde dataverwerking is gedaan. Hoe dit exact zou moeten en welke consequentie dit voor de werkprocessen zou hebben is nog niet uitgewerkt tijdens dit onderzoek.

#### Voorstel aanvullende eigenschap om op te nemen in de log

Behalve de verwijzing naar een formele catalogus, of het algoritmeregister hebben platform leveranciers vaak ook een plek waar documentatie of aanvullende informatie van een rekenmodel of algoritme te vinden is. Hiervoor nemen we een aanvullende eigenschap op: ```dpl.objects.vendor_operation_ref```

#### processing_activity_id gelijk houden over namespaces heen of specifiek houden

Het kan verwarrend zijn om dezelfde eigenschap (processing_activity_id) in verschillende namespaces te hebben. We kiezen ervoor om de verwijzing naar een register zo expliciet mogelijk te maken. En daarom kiezen we ervoor om dpl.objects.processing_activity_id te hernoemen naar dpl.objects.algorithm_id.
