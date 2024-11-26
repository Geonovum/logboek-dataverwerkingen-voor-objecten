# Architectuur

De standaard voor het loggen van dataverwerkingen gaat over het verantwoorden van het gebruik van informatie door de overheid. Hierbij moeten er keuzes gemaakt worden wat er wel en niet vastgelegd wordt. Het is immers in de praktijk niet haalbaar om elke individuele transactie of bevraging vast te leggen en daar nog waardevolle inzichten uit te kunnen halen. Deze 'implementatierichtlijnen' vallen buiten de scope van de standaard zelf. Hierdoor kan de standaard in principe heel breed ingezet worden.

## Huidige situatie

De standaard Logboek dataverwerkingen [[LDV]] beschrijft als werkingsgebied:

*Functioneel toepassingsgebied: De standaard Logboek Dataverwerkingen moet worden toegepast als persoonsgegevens worden verwerkt ten behoeve van het ontsluiten van overheidsinformatie en/of functionaliteit.*

Dit kan beschouwd worden als een 'minimaal verplichte' scope.
De standaard is echter zo generiek opgesteld dat deze breder toegepast kan worden.

## Gewenste situatie

Bij de bredere toepassing van de standaard voor het loggen van (geo)objecten dienen zich een aantal aanvullende vragen aan. De uitwerking in dit document probeert antwoorden te geven op die aanvullende vragen.

Voor dit onderzoek kiezen we voor het [Algoritmeregister](https://algoritmes.overheid.nl/nl) als kader om te bepalen of een verwerking gelogd moet worden of niet.

Met de uitbreiding van de scope van de te loggen verwerkingen wordt de semantische duiding van de verwerking en het object waar de verwerking op van toepassing is belangrijker. De logging gaat immers niet altijd meer alleen over persoonsgegevens.
In de standaard wordt de duiding gepositioneerd als [extensie 'Inzage'](https://logius-standaarden.github.io/logboek-dataverwerkingen/#extensies). Voor deze inzage denken we dat het meerwaarde heeft om de gegevens te kunnen definieren in termen van de [PROV-O](https://www.w3.org/TR/prov-o/) standaard. Vanuit deze mapping is een verbinding naar bijvoorbeeld de  [[NLSBB]] of de [[DCAT_AP_NL]] standaard interessant.

## Positionering

### GDI Gegevensuitwisseling

![GDI Gegevensuitwisseling Bedrijfsobjectenmodel](./respec/media/gdi-gegevensuitwisseling-bedrijfsobjectenmodel.png)
[Bedrijfsobjectenmodel GDI Gegevensuitwisseling](https://minbzk.github.io/gdi-gegevensuitwisseling/?view=id-efc531031d114860a309f6eeacdad289)

De logboek dataverwerking standaard kan gepositioneerd worden in de GDI Gegevensuitwisseling als standaard waarin een 'Uitwisselingsafspraak' geformaliseerd wordt. Waarbij de daadwerkelijke logging betrekking heeft op de 'Operatie'.

### NORA Nationaal Semantisch Vlak

![Nora Nationaal Semantisch Vlak](./respec/media/Nora-Nationaal_semantisch_vlak.png)
[Nora Nationaal Semantisch Vlak](https://www.noraonline.nl/wiki/Nationaal_Semantisch_Vlak)
In het kader van het NORA Nationaal Semantisch Vlak kan de logboek dataverwerking standaard gepositioneerd worden als het vastleggen van een gebeurtenis die betrekking heeft op een informatieobject.

## Aandachtsgebieden

De voorlopige conclusie is dat de kern van de standaard zodanig generiek is dat deze in principe ook toegepast kan worden voor het loggen van (geo)objecten.
De aandachtspunten liggen vooral in de te maken keuzes in de implementatie of het uitbreiden met een extensie voor inzage.

### Implementatie keuzes

Bij het implementeren van de loggingstandaard speelt de dynamiek van het digitale tweelingen ecosysteem een grote rol. In de beoogde architectuur ontstaat er een catalogus (of 'appstore') van rekenmodellen die een gebruiker naar behoefte kan inzetten. Het is vooraf dus nog niet duidelijk welke organisatie welk aangeboden rekenmodel gaat inzetten voor het analyseren van een bepaald beleidsvraagstuk. De verwerkingsketen is daarmee op voorhand dus nog niet bekend en er is een scheiding van de verantwoordelijke organisatie en de aanbieder van het rekenmodel.

![Dynamiek in Digitaal Tweelingen Ecosysteem](./respec/media/Front-Backend_achtergrond.png)

### Uitbreiding Inzage

Omdat de scope van de gelogde gegevens breder is dan de context van persoonsgegevens is het van groter belang om inzage te hebben in het kader van welke verwerking gegevens gelogd zijn. Is dit bijvoorbeeld een verwerking op basis van een hoog risico algoritme, of voldoen de objecten wel aan de juiste definities voor toepassing in het betreffende rekenmodel.
