# Conceptueel model

De kern van het [[PROV_O]] model bestaat uit een Activiteit, een Entiteit en een Agent.

![prov-dm](./respec/media/prov-dm.png)

Om een goede mapping te kunnen maken tussen de Logboek dataverwerkingen standaard en PROV-O volstaat het kernmodel niet. We kijken daarom naar de complete ontologie om alle constructies goed te kunnen mappen.

De basis van de standaard kent het Logboek (met de [interface](https://logius-standaarden.github.io/logboek-dataverwerkingen/#interface) beschrijving), de Applicatie die naar het Logboek schrijft en het Register waarnaar verwezen wordt ter verantwoording van de verwerkingsactiviteit.

![ldv](./respec/media/architecture-grenzen.svg)

Het Logboek is in essentie een lijst van (PROV-O) Activiteiten. Het resultaat van die activiteit (oftewel de PROV-O Entity) is de gewijzigde data in de applicatie. Een PROV-O Agent is hier zowel de betrokkene of het object waar de datawijziging over gaat en de actor die de wijziging doorvoert.
Zowel Agent als Entity komen daarmee niet rechtstreeks in het kernmodel voor.
En we kunnen daarmee het Register ook niet eenduidig mappen op een van de kernconcepten van het PROV-O model.

Als we een laag dieper kijken naar de [interface](https://logius-standaarden.github.io/logboek-dataverwerkingen/#interface) beschrijving vinden we daar echter wel aanknopingspunten voor een verdere mapping.

## Logboek Interface

```text
    Een van de gedefinieerde attributen is het veld `resource`. 
    Dit is een bericht, opgebouwd uit het volgende veld:

    - `attributes`: Lijst attributen in de vorm van *KeyValue pairs*. 
    De organisatie kan deze lijst gebruiken om een systeem, 
    applicatie of component aan te duiden op een manier die binnen de 
    organisatie gebruikelijk is. 
    Dit zijn bijvoorbeeld naam en versienummer van een applicatie, 
    of een verwijzing naar een record in een CMDB.

    Het veld `attributes` is een lijst van *key-value pairs*, 
    in een namespace met prefix `dpl.` (data processing log). 
    De volgende attributen zijn mogelijk in de namespace `core`:

    - `dpl.core.processing_activity_id`: URI; 
    Verwijzing naar register met meer informatie over de verwerkingsactiviteit
    - `dpl.core.data_subject_id`: ID van de Betrokkene; versleuteld. 
    Dit is bijvoorbeeld een `BSN` of `Vreemdelingennummer` 
    waarmee wordt aangeduid welke persoon Betrokkene is bij de verwerking, 
    gelet op de AVG.
```

In de attributes zien we dus de constructie om te verwijzen naar het register via `dpl.core.processing_activity_id`. En we zien met `dpl.core.data_subject_id` een constructie om te verwijzen naar het subject van de verwerking.

Prov:Entity kent een subclass [prov:Plan](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Plan): 'A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals.'

Via een 'prov:qualifiedAssociation' kan een Activiteit (dus een regel in het Logboek) geassocieerd worden met een Plan. (in dit geval een verwerkingsactiviteit in het Register).

```turtle
    :logregel_X a prov:Activity ;
    prov:qualifiedAssociation [
        a prov:Association;
        prov:hadPlan :algoritme_Z;
        rdfs:comment "logregel_X verwijst naar algoritme_Z"@nl;
    ];
    .
    :algoritme_Z a prov:Plan, prov:Entity;
    rdfs:comment "algoritme om Z te berekenen..."@nl;
    .
```

Via een 'prov:qualifiedAssociation' kan een Activiteit (dus een regel in het Logboek) ook geassocieerd worden met een betrokkene/(geo)object.

```turtle
    :logregel_X a prov:Activity ;
    prov:qualifiedAssociation [
        a prov:Association;
        prov:agent :subject_Y;
        prov:hadRole :betrokkene;
        rdfs:comment "logregel_X verwijst naar betrokkene subject_Y"@nl;
    ];
    .
    :subject_Y a prov:Agent, prov:Entity;
    rdfs:comment "subject_Y is de betrokken partij in de verwerking"@nl;
    .
```

De mapping van het technisch model van de Logboek Dataverwerking standaard naar PROV-O maakt het vervolgens makkelijker om te verwijzen naar een externe definitie van het register of subject.
