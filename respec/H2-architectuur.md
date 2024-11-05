# Architectuur

De standaard voor het loggen van dataverwerkingen gaat over het verantwoorden van het gebruik van informatie door de overheid. Hierbij moeten er keuzes gemaakt worden wat er wel en niet vastgelegd wordt. Het is immers in de praktijk niet haalbaar om elke individuele transactie of bevraging vast te leggen en daar nog waardevolle inzichten uit te kunnen halen. 

## Huidige situatie

De huidige (concept) standaard Logboek dataverwerkingen [[LDV]] definieert de scope van wat er gelogd moet worden sterk in de context van de AVG:

*Functioneel toepassingsgebied: De standaard Logboek Dataverwerkingen moet worden toegepast als persoonsgegevens worden verwerkt ten behoeve van het ontsluiten van overheidsinformatie en/of functionaliteit.*

Dit geeft heldere kaders over welke dataverwerkingen er vastgelegd moeten worden en een verwijzing naar een register om de verantwoording van die activiteit te onderbouwen.

## Gewenste situatie

Als de standaard uitgebreid wordt met het loggen van transacties op (geo)objecten dient zich de vraag aan welk afwegingskader er gebruikt kan worden om te bepalen welke verwerkingen wel en niet gelogd dienen te worden.

Voor dit onderzoek kiezen we voor het [Algoritmeregister](https://algoritmes.overheid.nl/nl) als kader om te bepalen of een verwerking gelogd moet worden of niet.

Met de uitbreiding van de scope van de te loggen verwerkingen wordt de semantische duiding van de verwerking en het object waar de verwerking op van toepassing is ook belangrijker. Hiervoor onderzoeken we of er een relatie gelegd kan worden naar een definitie op basis van de [[NLSBB]] standaard om eenduidig vast te leggen op welk object de verwerking betrekking heeft.

Ten slotte willen we onderzoeken of de standaard in een bredere context geduid kan worden door de mapping naar de [PROV-O](https://www.w3.org/TR/prov-o/) standaard te maken. 


## Positionering

### GDI Gegevensuitwisseling

![GDI Gegevensuitwisseling Bedrijfsobjectenmodel](./respec/media/gdi-gegevensuitwisseling-bedrijfsobjectenmodel.png)
[Bedrijfsobjectenmodel GDI Gegevensuitwisseling](https://minbzk.github.io/gdi-gegevensuitwisseling/?view=id-efc531031d114860a309f6eeacdad289)

De logboek dataverwerking standaard kan gepositioneerd worden in de GDI Gegevensuitwisseling als standaard waarin een 'Uitwisselingsafspraak' geformaliseerd wordt. Waarbij de daadwerkelijke logging betrekking heeft op de 'Operatie'.

### NORA Nationaal Semantisch Vlak

![Nora Nationaal Semantisch Vlak](./respec/media/Nora-Nationaal_semantisch_vlak.png)
[Nora Nationaal Semantisch Vlak](https://www.noraonline.nl/wiki/Nationaal_Semantisch_Vlak)
In het kader van het NORA Nationaal Semantisch Vlak kan de logboek dataverwerking standaard gepositioneerd worden als het vastleggen van een gebeurtenis die betrekking heeft op een informatieobject.


