# Code snippets IMAGEM

## Starten nieuw project en het aanmaken van de eerste logs

```typescript
// Starten van de eeste span
await tracer.startActiveSpan(
  "Project aangemaakt en wordt berekend",
  async (span) => {
    // Voeg attribute toe met daarin verwijzing naar systeem-specifieke attributen
    span.setAttribute(
      "attribute",
      JSON.stringify({
        projectID: project.id,
      })
    );
    // Voeg dpl.object.processing_activity_id toe met daarin verwijzing naar het Algoritme register
    span.setAttribute(
      "dpl.object.processing_activity_id",
      "https://algoritmes.overheid.nl/nl/algoritme/digitale-tweeling-simulator-stichting-geonovum/45242755"
    );

    // Voeg dpl.core.data_subject_id met daarin verwijzen naar de id van de gebruiker binnen het IMAGEM systeem
    span.setAttribute("dpl.core.data_subject_id", user.id);

    // Sla de traceID op binnnen het project
    project.traceID = span.spanContext().traceId;

    // Binnen deze span worden functies gestart voor het aanroepen van de berekeningen
    // Spans binnen deze async functie worden automatisch samengekoppeld
    await startCalculation();

    // Verstuur de span naar de logger
    span.end();
  }
);
```

## Starten van een berekening en de response loggen

```typescript
async function startCalculation() {
  // Post naar het endpoint van de derde partij
  // Met traceparent in de header die eerder was opgeslagen binnen het project
  const response = await post(endpointUrl, {
    headers: { traceparent: `00-${project.traceID}-0000000000000000-01` },
  });

  // In de response zit een nieuw traceparent id die verwijst naar de logs bij de derde partij

  // Start een nieuwe active span om de resultaten te loggen
  tracer.startActiveSpan("Project berekend met lagen van Tygron", (span) => {
    // foreign_operation.trace_id bevat de traceparent die meegeven is via de response van de berekening
    span.setAttribute("foreign_operation.trace_id", traceparent);

    // Voor Tygron weten we waar de log benaderbaar zijn en wordt deze toegevoegd als foreign_operation.entity
    span.setAttribute(
      "foreign_operation.entity",
      `https://development.webapp.tygron.com/?action=GetLog&authenticationToken=Imagem&log=${traceparent}`
    );

    // Voeg dpl.object.processing_activity_id toe met daarin verwijzing naar het Algoritme register
    span.setAttribute(
      "dpl.object.processing_activity_id",
      "https://algoritmes.overheid.nl/nl/algoritme/modelleringssoftware-hittestress-stichting-geonovum/21577420"
    );

    // Voeg attribute toe met daarin verwijzing naar systeem-specifieke attributen
    span.setAttribute(
      "attribute",
      JSON.stringify({
        projectID: project.id,
      })
    );

    // Sluit de span
    span.end();
  });
}
```
