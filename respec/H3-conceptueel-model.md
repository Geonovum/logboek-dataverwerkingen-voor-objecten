# Conceptueel model

Om de interoperabiliteit tussen de standaard Logboek dataverwerkingen en andere systemen te verbeteren kijken we naar de mapping van het gebruikte model (op basis van open telemetry) naar PROV-O.
  
De kern van het [[PROV_O]] model bestaat uit een Activiteit, een Entiteit en een Agent.

![prov-dm](./respec/media/prov-dm.png)

[Illustratie van het prov kernmodel](https://www.w3.org/TR/prov-dm/#prov-core-structures)

Om een goede mapping te kunnen maken tussen de standaard Logboek dataverwerkingen  en PROV-O volstaat het kernmodel niet. We kijken daarom naar de complete ontologie om alle constructies goed te kunnen mappen.

De basis van de standaard kent het Logboek (met de [interface](https://logius-standaarden.github.io/logboek-dataverwerkingen/#interface) beschrijving), de Applicatie die naar het Logboek schrijft en het Register waarnaar verwezen wordt ter verantwoording van de verwerkingsactiviteit.

![ldv](./respec/media/architecture-grenzen.svg)

[Illustratie uit de Logboek dataverwerkingen standaard, componenten in context](https://logius-standaarden.github.io/logboek-dataverwerkingen/#fig-componenten-in-context)

Het Logboek is in essentie een lijst van (PROV-O) Activiteiten. Het resultaat van die activiteit (oftewel de PROV-O Entity) is de gewijzigde data in de applicatie. Een PROV-O Agent is hier zowel de betrokkene, of het object waar de datawijziging over gaat, en de actor die de wijziging doorvoert.
Zowel Agent als Entity komen daarmee niet rechtstreeks in het kernmodel van het logboek voor.

Als we een laag dieper kijken naar de [interface](https://logius-standaarden.github.io/logboek-dataverwerkingen/#interface) beschrijving vinden we daar echter wel aanknopingspunten voor een verdere mapping.

## Logboek Interface (Normatieve standaard)

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

    - `dpl.core.processing_activity_id`: URI; Verwijzing naar Register 
    met meer informatie over de Verwerkingsactiviteit
    - `dpl.core.data_subject_id`: Unieke identificerende code van de Betrokkene; versleuteld. 
    Hiermee wordt aangeduid welke persoon Betrokkene is bij de verwerking, gelet op de AVG.
    - `dpl.core.data_subject_id_type`: Type van het veld data_subject_id. 
    Dit is bijvoorbeeld BSN, Personeelsnummer of Vreemdelingennummer, 
    of een URI naar een Register waar het veld meer precies wordt geduid.
```

In de attributes zien we dus de constructie om te verwijzen naar het register via `dpl.core.processing_activity_id`. En we zien met `dpl.core.data_subject_id` een constructie om te verwijzen naar het subject van de verwerking, en met `dpl.core.data_subject_id_type` een nadere duiding van het soort subject.

Prov:Entity kent een subclass [prov:Plan](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Plan): 'A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals.'

Via een 'prov:qualifiedAssociation' kan een Activiteit (dus een regel in het Logboek) geassocieerd worden met een Plan. (in dit geval een verwerkingsactiviteit in het Register).

```turtle
    :logregel_X a prov:Activity ;
    prov:qualifiedAssociation [
        a prov:Association;
        prov:hadPlan :verwerkingsactiviteit_Z;
        rdfs:comment "logregel_X verwijst naar verwerkingsactiviteit_Z"@nl;
    ];
    .

    :Verwerkingsactiviteit_Z a prov:Plan, prov:Entity;
    rdfs:comment "Verwerkingsactiviteit in het verwerkingenregister..."@nl;
    .
```

Via een 'prov:qualifiedAssociation' kan een Activiteit (dus een regel in het Logboek) ook geassocieerd worden met een betrokkene.

```turtle
    :logregel_X a prov:Activity ;
    prov:qualifiedAssociation [
        a prov:Association;
        prov:agent :subject_Y;
        prov:hadRole :betrokkene;
        rdfs:comment "logregel_X verwijst naar betrokkene subject_Y"@nl;
    ];
    .

    :subject_Y a prov:Entity;
    rdfs:comment "subject_Y is de betrokken persoon in de verwerking"@nl;
    .

    :betrokkene a prov:Role;
    rdfs:comment "extra rolduiding (type) van de betrokken in het kader van de verwerkingsactiviteit"@nl;
    .
```

De mapping van het technisch (opentemetry) model van de standaard Logboek dataverwerkingen naar PROV-O maakt het vervolgens makkelijker om de loggegevens interoperabel te maken met andere systemn.

## Logboek Interface (objecten)

Net zoals de core standaard attributen definieert in de `dpl.core` namespace, definieren we attributen voor (geo)objecten in de `dpl.objects` namespace. Ook deze zijn op een vergelijkbare wijze te mappen naar PROV-O.

Via een 'prov:qualifiedAssociation' kan een Activiteit (dus een regel in het Logboek) geassocieerd worden met een Plan. (in dit geval een algoritme in  in het algoritmeregister).

```turtle
    :logregel_A a prov:Activity ;
    prov:qualifiedAssociation [
        a prov:Association;
        prov:hadPlan :algoritme_B;
        rdfs:comment "logregel_A verwijst naar algoritme_B"@nl;
    ];
    .

    :algoritme_B a prov:Plan, prov:Entity;
    rdfs:comment "algoritme B in het algoritmeregister..."@nl;
    .
```

Via een 'prov:qualifiedAssociation' kan een Activiteit (dus een regel in het Logboek) ook geassocieerd worden met een (Geo)object.

```turtle
    :logregel_A a prov:Activity ;
    prov:qualifiedAssociation [
        a prov:Association;
        prov:agent :list_of_objects;
        prov:hadRole :input_for_activity;
        rdfs:comment "logregel_A verwijst naar betreffende list_of_objects"@nl;
    ];
    .

    :list_of_objects a prov:Entity;
    rdfs:comment "list_of_objects is de lijst van objecten in de verwerking"@nl;
    .

    :input_for_activity a prov:Role;
    rdfs:comment "extra rolduiding (verwijzing naar definitie) van de betrokken objecten in het kader van het algoritme"@nl;
    .
```


## voorbeeld uitwerking

Onderstaand een voorbeeld van een log vanuit opentelemetry:

```bash
Span #77                                                                                                                                                                                        
Trace ID       : 63bbb396834c646c0598f7cd9118504d                                                                                                                                           
Parent ID      :                                                                                                                                                                            
ID             : 27d458ec67e6fb68                                                                                                                                                           
Name           : LocalOutlierFactor
Kind           : Internal
Start time     : 2024-11-29 10:50:54.162958793 +0000 UTC
End time       : 2024-11-29 10:50:55.123923577 +0000 UTC
Status code    : Ok                                                                                                                                                                      
Status message : 
    Attributes:                                                                                                                                                                                     
    -> dpl.objects.processing_association_id: Str(http://localhost:5000/processes/localoutlier)
    -> dpl.objects.data_association_id: Slice([201,203,204,205,206])
    -> dpl.objects.data_association_def: Str(http://localhost:5000/collections/knmi_meetstations/queryables?f=json)                                                          
```

Een voorbeeld in RDF zou er als volgt uit kunnen zien:

