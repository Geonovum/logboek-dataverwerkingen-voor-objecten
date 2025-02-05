## Volwassenheidsniveaus en scenarios

### Volwassenheid:

0: log je niet in een veld welke data je verwerkt, maar wordt het afgeleid van de verwerkingsactiviteit ID
1: welke velden je daadwerkelijk hebt verwerkt. Je linkt nog steeds naar de verwerkingsactiviteit ID
2: wat was de inhoud van de velden

Voorbeeld van een Excel sheet als register
0: log dat het register is gebruikt, met alle mogelijke kolommen in de sheet
1: logt enkel de specifieke kolommen in de sheet die gebruikt zijn (hoeft dus niet allemaal)
2: welke specifieke inhoud van de velden

---


### Scenario's Subjecten / Objecten
1. (niveau 0/1) alleen subject vastleggen
	1. voorbeeld: aanvraag rijbewijs
	
2. (niveau 1) alleen object vastleggen (want geen direct aanwijsbaar subject)
	1. voorbeeld: Remote Sensing gebiedsclassificatie op basis van AI beeldherkenning (https://algoritmes.overheid.nl/nl/algoritme/remote-sensing-gebiedsclassificatie-op-basis-van-ai-beeldherkenning-provincie-zuidholland/87239212#werking) *"Deze dataset bevat momentopnames van geautomatiseerd gegenereerde vegetatiestructuurclassificaties van de Natura 2000-gebieden"* (het natura 2000 gebied is wel van een niet-natuurlijk persoon, maar de classificatie heeft daar geen betrekking op)

	- vastleggen welke type satellietbeelden er gebruikt zijn

3. (niveau 2) alleen object vastleggen, inclusief verwerkte attributen (want geen direct aanwijsbaar subject)

	- vastleggen welke satellietbeelden (jaartal, band, identificatie van het beeld) er gebruiklt zijn

4. (niveau 2) alleen object vastleggen, er kan een afgeleid subject bepaald worden (geen direct aanwijsbaar subject)
	1. voorbeeld: Maaidata (https://algoritmes.overheid.nl/nl/algoritme/maaidata-provincie-noordholland/68294175#werking) *"Met eenvoudige beslisregels bepalen we voor ieder perceel of een grenswaarde is bereikt, binnen of buiten het broedseizoen."* perceel heeft een subject.

	- vastleggen welke percelen er geanalyseerd zijn

5. (niveau 2) object en subject vastleggen (De verwerking van het object heeft een direct aanwijsbaar subject)
	1. voorbeeld: Aanvraag kapvergunning. een Subject heeft een aanvraag ingediend om een object te kappen (namelijk boom x).

	- vastleggen welke persoon een vergunning heeft aangevraagd voor welke boom



#### definities:
- subject: het persoonsgegeven van een natuurlijk of niet-natuurlijk persoon
- object: een 'ding' wat verwerkt wordt in een actie
- attribuut: een gegeven van een subject of object


