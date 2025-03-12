# Extensie (geo)objecten

Het loggen van (geo)objecten is een bijzonder ruim en daarmee flexibel onderwerp. Er zijn zeer veel mogelijke scenario's, afhankelijk van de gebruikte data, 
het type analyse of algoritme en het gewenste volwassenheidsniveau.

We nemen een paar uitgangspunten op om de scope te verduidelijken.

<aside class="note">

Deze uitgangspunten moeten nog getoetst worden in de praktijk.

De kans is groot dat theorie en praktijk uit elkaar blijven lopen. Bijvoorbeeld voor wat betreft het abstractieniveau waarop een algoritme in een algoritmeregister is 
beschreven en de daadwerkelijke implementatie in een systeem en de (technische) mogelijkheiden om logging te implementeren.

</aside>

1. Input/output poorten conform het idee van 'Dataproducten' als uitgangspunt voor de afbakening van het proces wat wordt gelogd.
2. API specificatie van een proces (als het goed is gelijk aan 1.)


---

- dpl.object.processing_activity_id (verwijzing naar het algoritmeregister)
- dpl.objects.dataproduct [
    - dataproduct_id 
    - dataproduct_def
    - feature [
        - feature_id
        - feature_def
    ]
    - feature_attribute [
        - attribute_name
        - attribute_value
    ]
]

---