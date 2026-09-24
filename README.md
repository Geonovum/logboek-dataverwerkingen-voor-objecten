# logboek-dataverwerkingen-voor-objecten

Resultaten van het innovatiebudgetproject om te onderzoeken of de standaard Logboek dataverwerkingen ook voor (geo)objecten toegepast kan worden.

## Handreiking (ReSpec)

De handreiking is opgezet volgens het [NL-ReSpec-template](https://github.com/Geonovum/NL-ReSpec-template):

* [`index.html`](index.html) en [`js/config.js`](js/config.js) bevatten de ReSpec-opbouw en documentmetadata
* de hoofdstukken staan als markdown in de root (`Samenvatting.md`, `H1-inleiding.md` t/m `H6-conclusies.md`, `conventies.md`)
* afbeeldingen staan in [`media/`](media/)

Werkversie: https://geonovum.github.io/logboek-dataverwerkingen-voor-objecten/

### Publiceren

Publicatie gaat via een GitHub Release (zie de [instructies in het template](https://github.com/Geonovum/NL-ReSpec-template#publiceren-van-documenten)):

* een **pre-release** publiceert naar https://test.docs.geostandaarden.nl/
* een **release** maakt een pull request aan op [`Geonovum/docs.geostandaarden.nl`](https://github.com/Geonovum/docs.geostandaarden.nl/pulls); na merge staat het document op https://docs.geostandaarden.nl/ldv/logboek-dataverwerkingen-voor-objecten/

Werk vóór een release `publishDate` in `js/config.js` bij en controleer dat de `Main Workflow` groen is met **"Publicatiegereed: ja"**.

## Overige onderdelen

* [`mvp_pygeoapi_logging_demo/`](mvp_pygeoapi_logging_demo/) – MVP met pygeoapi en OpenTelemetry-logging
* [`prov-o_mapping/`](prov-o_mapping/) – mapping van traces naar PROV-O
* [`codesprint-resultaten/`](codesprint-resultaten/) – resultaten van de codesprint
* [`logboek_objecten_extensie/`](logboek_objecten_extensie/) – concept van de extensie voor objecten
* [`PSA/`](PSA/) – voorbeeld van traces in RDF
