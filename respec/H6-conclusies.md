# Conclusies

## Extensie (geo)objecten

- Technisch gezien is de standaard goed te implementeren in de software die gebruikt wordt voor Digitale tweelingen. Het helpt als de interface specificatie van Logboek dataverwerkingen goed overeenkomt met de SDK/API voor opentelemetry. In de loop van het onderzoek zijn er een aantal wijzigingen in de standaard doorgevoerd om de aansluiting tussen de standaard en opentelemetry te verbeteren.

- In de praktijk blijken de beleidsprocessen in de fysieke leefomgeving minder strak afgebakend dan de processen in het kader van de AVG waar de Logboek dataverwerkingen standaard in eerste instantie voor ontwikkeld is. Het uitvoeren van een analyse voor bijvoorbeeld hittestress kan zowel gedaan worden in het kader van een vergunning verleningstraject, waar de Omgevingswet het juridische kader is, als voor een risicoanalyse voor een beleidsmaatregel die valt onder het juridisch kader van de Algemene Wet Bestuursrecht.

- De wijze waarop medewerkers een digitale tweelingplatform typisch gebruiken, door verschillende datalagen te laden en analyses uit te voeren waarbij niet alle data lagen relevant hoeven te zijn voor de uitgevoerde analyse maakt het ingewikkelder om precies dat te loggen wat voor de verantwoording van een beleidsproces van belang is. 

- Om besluiten in de context van beleidsprocessen voor de fysieke leefomgeving eenduidiger te kunnen loggen is niet alleen een gedegen implementatie in software nodig, maar zal er ook in de werkprocessen een aanpassing gedaan moeten worden. 

- Het relateren van een dataverwerking aan een algoritme in het algoritmeregister blijkt niet eenduidig genoeg. Onderzocht zou moeten worden of een aanvullende verwijzing naar bijvoorbeeld wetten.nl voldoende eenduidigheid kan geven.

- De standaard biedt veel flexibiliteit door het definiëren van de verschillende volwassenheidsniveaus. Het is wenselijk om een beleidskader uit te werken waarmee bepaald kan worden welk volwassenheidsniveau gewenst is in verschillende situaties. Dit zou gerelateerd kunnen zijn aan de classificatie van een algoritme in het algoritmeregister, maar zou ook gerelateerd kunnen zijn aan het soort werkproces of beleidsproces waar de dataverwerking onderdeel van is.

## Mapping PROV-O

- De mapping naar de PROV-O standaard is mogelijk voor het normatieve deel van de standaard. De patronen komen daarvoor voldoende overeen. 

- Tijdens de afronding van dit onderzoek kwam de 'Data Privacy Vocabulary' in beeld. Dit is een standaard die door een W3C Community Group is opgesteld. Daarmee is het geen formele W3C standaard, maar er lijken veel aanknopingspunten in te zitten om de mapping met deze standaard uit te breiden.

<aside class="note">
The Data Privacy Vocabulary [[DPV]] enables expressing machine-readable metadata about 
the use and processing of (personal or otherwise) data and technologies based on
legislative requirements such as the General Data Protection Regulation [[GDPR]].
</aside>

- Voor de mapping van het loggen van (geo)objecten, is er naast de PROV-O standaard, behoefte aan een standaard die de complexiteit van de gelogde informatie goed weer kan geven. De DCAT standaard is hiervoor niet toereikend. Een mogelijke kandidaat is de [[DPROD]] standaard. Er is ook gekeken naar de MLDCAT-AP standaard, deze standaard is een uitbreiding op het europese DCAT-AP profiel, maar de insteek op machinelearning lijkt in de context van het vastleggen van de rekenmodellen onvoldoende aan te sluiten en een mapping naar DPROD lijkt beter aan te sluiten.


