# PSA

## Aanleiding en doelstelling

BZK heeft op basis van een aanvraag in samenwerking met Geonovum innovatiebudget toegewezen gekregen voor het onderwerp 'Standaard voor transparantie besluitvorming ' (IDO240584K). Het belang dat de overheid verantwoording en transparantie biedt aan burgers en bedrijven over hoe zij handelt, is groot. Burgers en bedrijven dienen op de hoogte te zijn van de gebruikte gegevens en besluitvormingsprocessen van de overheid. Hiervoor worden niet alleen persoonsgegevens maar bijvoorbeeld ook data over objecten uit de fysieke leefomgeving gebruikt. Het ministerie van Binnenlandse Zaken en Koninkrijksrelaties directie digitale overheid (regievoerder) heeft aan Geonovum gevraagd hierin ondersteuning te bieden en een offerte uit te brengen voor het uitbreiden voor het Logboek Dataverwerking.

## De opdracht, het resultaat en te bereiken effect

Het probleem dat BZK en Geonovum signaleren is dat het steeds lastiger maar ook steeds belangrijker wordt om aan te geven welke gegevens op welke manier worden gebruikt door de overheid, bijvoorbeeld bij het nemen van besluiten of formuleren van beleid. BZK ziet namelijk dat de informatievoorziening van de overheid steeds meer toe gaat naar een federatieve opzet waarbij meerdere bronnen van verschillende overheidsorganisaties gecombineerd worden om informatievragen te beantwoorden of om besluiten te nemen over een aanvraag van een burger. Daarbij is het heel belangrijk om verantwoording af te kunnen leggen hoe een antwoord op een informatievraag of een besluit tot stand is gekomen. Dit verhoogt de transparantie in het handelen van de overheid. De conceptstandaard voor loggen van verwerkingen (Logboek Dataverwerkingen) is daar een belangrijke bouwsteen in.

*We willen die uitbreiden met geografische informatie om transparantie over gebruik van geo data te bevorderen. Zo nodig dient ook de toepassing van de NL-SBB en DCAT standaarden in dit licht getoetst te worden.*

## Relaties met andere projecten

- [logboek dataverwerkingen](https://logius-standaarden.github.io/logboek-dataverwerkingen/)
- [DCAT-AP-NL 3.0](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30)
- [NL-SBB](https://geonovum.github.io/NL-SBB/)
- [DTaaS](https://www.geonovum.nl/over-geonovum/actueel/werken-aan-digital-twin-as-a-service) (de use case om een aanvullende standaard mee te beproeven wordt gezocht binnen het DTaaS project)

## Huidige situatie

Er is een (concept) standaard waar dit project een extensie op zou moeten worden.

In de standaard zitten een aantal onderwerpen waar specifiek aandacht voor is in relatie tot deze extensie.

begrippen Logboek gegevensverwerking

- [Applicatie](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-applicaties)
- [Betrokkene](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-betrokkenen)

- [Dataverwerking](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-dataverwerkingen)
Aansluitend bij de Algemene Verordening Gegevensbescherming (art. 4 lid 2), maar breder toegepast dan alleen persoonsgegevens, wordt voor deze standaard ‘elke bewerking of elk geheel van bewerkingen met betrekking tot gegevens, al dan niet uitgevoerd via geautomatiseerde procedures, zoals het verzamelen, vastleggen, ordenen, structureren, opslaan, bijwerken of wijzigen, opvragen, raadplegen, gebruiken, verstrekken door middel van doorzending, verspreiden of op andere wijze ter beschikking stellen, aligneren of combineren, afschermen, wissen of vernietigen van gegevens’ opgevat als een dataverwerking.

- [Inzage](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-inzage)
- [Logboek](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-logboeken)
- [Operatie](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-operaties)
- [Register](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-registers)
- [Trace](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-traces)
- [Verwerkingsverantwoordelijke](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-verantwoordelijke)
- [Verwerkingsactiviteit](https://logius-standaarden.github.io/logboek-dataverwerkingen/#dfn-verwerkingsactiviteiten)

---
[Algemene werking van de standaard](https://logius-standaarden.github.io/logboek-dataverwerkingen/#algemene-werking-van-de-standaard)

Applicaties loggen metadata over Dataverwerkingen in een daarvoor ingerichte softwaretoepassing, het Logboek Dataverwerkingen. Elke Dataverwerking wordt apart gelogd. Dataverwerkingen binnen dezelfde context (bijvoorbeeld een organisatie of een verantwoordelijkheid binnen een organisatie) worden gegroepeerd met behulp van een Trace. Wanneer een Dataverwerkingen een andere Dataverwerking tot gevolg heeft worden de logregels van beide Dataverwerkingen aan elkaar gelinkt. Statische informatie over Dataverwerkingen kan worden opgezocht in Registers op basis van een verwijzing die in elke logregel wordt opgenomen.

---
Logboek Interface

| Veld                  | Type           | optioneel | Omschrijving |
|-----------------------|----------------|---------------|--------------|
| `trace_id`            | 16 byte        | verplicht     | Uniek ID van *Trace*, een groep bij elkaar behorende Dataverwerkingen |
| `operation_id`        |  8 byte        | verplicht     | Uniek ID van de Dataverwerking |
| `status_code`         | enum           | verplicht     | Status van de Dataverwerking |
| `name`                | string         | verplicht     | Naam van de specifieke operatie binnen de Dataverwerking |
| `start_time`          | timestamp (ms) | verplicht     | Tijdstip waarop de Dataverwerking gestart is |
| `end_time`            | timestamp (ms) | verplicht     | Tijdstip waarop de Dataverwerking beëindigd is |
| `parent_operation_id` |  8 byte        | optioneel     | ID van aanroepende Dataverwerking *binnen de huidige Verwerkingsactiviteit* |
| `foreign_operation`   | message        | optioneel     |              |
| `resource`            | message        | optioneel     |              |
| `attributes`          | list           | verplicht     | Verplichte key-value pairs |

Het veld `status_code` is een enumeratie die de volgende waarden kan bevatten:

- 0: STATUS_CODE_UNKNOWN:
- 1: STATUS_CODE_OK:
- 2: STATUS_CODE_ERROR:

Het veld `foreign_operation` is een `message`, opgebouwd uit de volgende velden:

| Veld                  | Type           | optioneel | Omschrijving |
|-----------------------|----------------|---------------|--------------|
| `trace_id`            | 16 byte        | verplicht     | Uniek ID van *Trace* bij externe partij |
| `operation_id`        |  8 byte        | verplicht     | Uniek ID van de Dataverwerking bij externe partij |
| `entity`              |  URI           | verplicht     | URI verwijzend naar externe partij |

Het veld `resource` is een bericht, opgebouwd uit het volgende veld:

- `attributes`: Lijst attributen in de vorm van *KeyValue pairs*. De organisatie kan deze lijst gebruiken om een systeem, applicatie of component aan te duiden op een manier die binnen de organisatie gebruikelijk is. Dit zijn bijvoorbeeld naam en versienummer van een applicatie, of een verwijzing naar een record in een CMDB.

Het veld `attributes` is een lijst van *key-value pairs*, in een namespace met prefix `dpl.` (data processing log). De volgende attributen zijn mogelijk in de namespace `core`:

- `dpl.core.processing_activity_id`: URI; Verwijzing naar register met meer informatie over de verwerkingsactiviteit
- `dpl.core.data_subject_id`: ID van de Betrokkene; versleuteld. Dit is bijvoorbeeld een `BSN` of `Vreemdelingennummer` waarmee wordt aangeduid welke persoon Betrokkene is bij de verwerking, gelet op de AVG.

## Gewenste situatie

De gewenste situatie vraagt ten eerste om aanscherping van de opdracht:
*We willen die uitbreiden met geografische informatie om transparantie over gebruik van geo data te bevorderen.*

- willen we geografische informatie vastleggen bij de dataverwerkingen die nu in scope zijn van de concept standaard? (scope is persoonsgegevens)
- willen we een extensie op de concept standaard met kaders en richtlijnen hoe we dataverwerkingen op (geo)objecten willen loggen?

Uitgaande van het tweede is het belangrijk om vast te stellen wanneer een dataverwerking 'relevant' is om gelogd te worden.
In de huidige concept standaard wordt verwezen naar het Register van Verwerkingsactiviteiten uit AVG art. 30. Hiermee wordt een duidelijk kader gesteld wanneer een activiteit gelogd moet worden.

Als de scope van het loggen van een dataverwerking 'opgerekt' wordt met het vastleggen van dataverwerking op (geo)objecten rijst de vraag naar welk register er verwezen moet worden (technisch gezien in de implementatie) en zou dat register de scope moeten bepalen wanneer een dataverwerking 'relevant' is.

=> is dat misschien het Algoritme register? En biedt dat het kader? Als een dataverwerking gedaan wordt die gebruik maakt van een geregistreerd algoritme dan moet de verwerking gelogd worden via een logboek implementatie.

## Architectuur

### klanten en dienstverlening

### processen en organisatie

Welke implicaties levert het loggen van bijv. een wateroverlast OGC Processing API op?
(een van de use cases van DMI/DTaaS)

- het is een algoritme wat gepubliceerd is in een beschikbare catalogus.
- het algoritme wat gepubliceerd is, is ook geregistreerd in een algoritme register (?)
  - als een kennisinstituut dit rekenmodel aanbiedt wie heeft dan welke verantwoordelijkheid?
- als we willen loggen welke organisatie de berekening heeft gemaakt hebben we niet genoeg aan alleen de OGC processing API, maar hebben we ook de 'flow' eromheen nodig om de geauthoriseerde organisatie uit te lezen.
- waar vindt de logging plaats van de berekening als het proces 'generiek' aangeboden wordt?

### informatie en applicaties

Basis PROV-O model:

```mermaid
classDiagram
Activity : startedAtTime
Activity : endAtTime 
Entity : 
Entity --> Activity : wasGeneratedBy
Agent 
Agent <-- Activity : wasAssociatedWith
Entity --> Agent : wasAttributedTo
Agent --> Agent : actedOnBehalfOf
Activity --> Activity : wasInformedBy
Entity --> Entity : wasDerivedFrom
Entity <-- Activity : used
```

---
plaatje van de relaties in een gedistribueerde LDV omgeving:
![ldv-traces](ldv-traces.png)

Als we proberen te mappen tussen de concepten van LDV en PROV-O.
Dan gelden mogelijk de volgende uitspraken:

- Logboek Interface = Activity

attributes dpl.core.processing_activity_id  *"URI; Verwijzing naar register met meer informatie over de verwerkingsactiviteit"*

=> prov:qualifiedAssociation *"An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity. It further allows for a plan to be specified, which is the plan intended by the agent to achieve some goals in the context of this activity."*

-> hadPlan => prov:Plan *"A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals."*

attributes dpl.core.data_subject_id *"ID van de Betrokkene; versleuteld. Dit is bijvoorbeeld een BSN of Vreemdelingennummer waarmee wordt aangeduid welke persoon Betrokkene is bij de verwerking, gelet op de AVG."*

-> data_subject_id is de Agent/Object van de qualifiedAssociation

parent_operation_id = prov:wasInformedBy

```mermaid
classDiagram
operation --> prov_Association : qualifiedAssociation 
prov_Association --> data_subject_id : qualifiedAssociation
prov_Association --> processing_activity_id : hadPlan
operation --> operation : parent_operation_id
```

| Logboek dataverwerking | PROV-O|
|------------------------|-------|
|Applicatie | Entity |
|Logboek | |
| Register | |

### technologie

## Beveiliging en privacy

## Risico's en openstaande issues

- onderzoeken of de interface van het logboek met de PROV-O ontologie te matchen is.
  - een PROV-O mapping is vooral interessant in relatie tot een 'inzage' extensie waar je de gegevens waar je inzage in geeft representeert in een PROV-O structuur.

## Implementatie

1

Aan het doorgeven van trace id's over omgevingen heen zitten potentieel wel wat implementatie haken en ogen als een algoritme/OGC Processing functie generiek aangeboden kan worden.

optie: altijd een W3CBaggagePropagator in de header context meegeven?
[https://opentelemetry.io/docs/languages/python/propagation/]

2

duidelijke richtlijnen meegeven wanneer een (geo)object gelogd kan worden. Er zijn een hoop algoritmen denkbaar (raster processing) waar het niet eenduidig is welke objecten er 'geraakt' worden.

## Beheer
