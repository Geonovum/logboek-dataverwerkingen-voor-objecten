# Conclusies

## Extensie (geo)objecten

- Technisch gezien is de standaard goed te implementeren in de software die gebruikt wordt voor digitale tweelingen. Het helpt als de interfacespecificatie van Logboek dataverwerkingen goed overeenkomt met de SDK/API voor OpenTelemetry. In de loop van het onderzoek zijn er een aantal wijzigingen in de standaard Logboek dataverwerkingen doorgevoerd om de aansluiting tussen de standaard en OpenTelemetry te verbeteren.

    - Aanpassing naamgeving operation_id naar span_id om in overeenstemming te zijn met de OpenTelemetry-specificatie
    - Expliciet gemaakt dat de betrokkene ook een niet-natuurlijk persoon kan zijn
    - Het implementeren van tracecontext en foreign_operation kan in de praktijk net anders uitpakken dan in de standaard beschreven (in oktober 2025 is `dpl.core.foreign_operation.trace_id` uit de normatieve tekst verwijderd)

- In de praktijk blijken de beleidsprocessen in de fysieke leefomgeving minder strak afgebakend dan de processen in het kader van de AVG waar de standaard Logboek dataverwerkingen in eerste instantie voor ontwikkeld is. Het uitvoeren van een analyse voor bijvoorbeeld hittestress kan zowel gedaan worden in het kader van een vergunningverleningstraject, waar de Omgevingswet het juridische kader is, als voor een risicoanalyse voor een beleidsmaatregel die valt onder het juridisch kader van de Algemene wet bestuursrecht.

- De wijze waarop medewerkers een platform voor digitale tweelingen typisch gebruiken, door verschillende datalagen te laden en analyses uit te voeren waarbij niet alle datalagen relevant hoeven te zijn voor de uitgevoerde analyse maakt het ingewikkelder om precies dat te loggen wat voor de verantwoording van een beleidsproces van belang is. 

- Om besluiten in de context van beleidsprocessen voor de fysieke leefomgeving eenduidiger te kunnen loggen is niet alleen een gedegen implementatie in software nodig, maar zal er ook in de werkprocessen een aanpassing gedaan moeten worden. 

- Het relateren van een dataverwerking aan een algoritme in het Algoritmeregister blijkt niet eenduidig genoeg. Onderzocht zou moeten worden of een aanvullende verwijzing naar bijvoorbeeld wetten.overheid.nl voldoende eenduidigheid kan geven.

- De standaard biedt veel flexibiliteit door het definiëren van de verschillende detailniveaus. Het is wenselijk om een beleidskader uit te werken waarmee bepaald kan worden welk detailniveau gewenst is in verschillende situaties. Dit zou gerelateerd kunnen zijn aan de classificatie van een algoritme in het Algoritmeregister, maar zou ook gerelateerd kunnen zijn aan het soort werkproces of beleidsproces waar de dataverwerking onderdeel van is.

## Mapping PROV-O

- De mapping naar de PROV-O standaard is mogelijk voor het normatieve deel van de standaard. De patronen komen daarvoor voldoende overeen. 

- Tijdens de afronding van dit onderzoek kwam de 'Data Privacy Vocabulary' in beeld. Deze vocabulaire is opgesteld door een W3C Community Group en gepubliceerd als Final Community Group Report. Daarmee is het geen formele W3C-standaard, maar er lijken veel aanknopingspunten in te zitten om de mapping met deze standaard uit te breiden.

<aside class="note">
The Data Privacy Vocabulary [[DPV]] enables expressing machine-readable metadata about 
the use and processing of (personal or otherwise) data and technologies based on
legislative requirements such as the General Data Protection Regulation [[GDPR]].
</aside>

- Voor de mapping van het loggen van (geo)objecten is er naast PROV-O behoefte aan een vocabulaire die de complexiteit van de gelogde informatie goed weer kan geven. DCAT(-AP-NL) blijft geschikt voor de metadata van de datasets waar `dataset_def` naar verwijst, maar is niet toereikend om de samenhang tussen algoritme, dataproduct en datasets in een verwerking te beschrijven. Een mogelijke kandidaat is de Data Product Ontology [[DPROD]]. Er is ook gekeken naar het applicatieprofiel MLDCAT-AP [[MLDCAT_AP]], een uitbreiding op het Europese DCAT-AP-profiel, maar de insteek op machine learning lijkt in de context van het vastleggen van de rekenmodellen onvoldoende aan te sluiten. Een mapping naar DPROD lijkt beter aan te sluiten.

- De koppeling met NL-SBB [[NL_SBB]] loopt via de `_def`-attributen van de extensie. Die kunnen verwijzen naar begrippen die volgens NL-SBB zijn beschreven, zoals in het voorbeeld in [](#H4) het BRT-begrip 'boom'. Een verdere uitwerking van deze relatie valt buiten dit onderzoek.


