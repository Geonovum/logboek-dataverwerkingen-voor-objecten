// ReSpec kent geen Turtle-highlighting en respec-nlgov biedt geen toegang tot
// de highlight-worker. Daarom highlighten we ```turtle-blokken zelf met
// highlight.js na de ReSpec-verwerking; de hljs-stijlen van ReSpec gelden ook
// voor deze blokken.
async function highlightTurtle(_config, document) {
  const blocks = document.querySelectorAll("pre code.turtle");
  if (blocks.length === 0) {
    return;
  }

  const { default: hljs } = await import(
    "https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11.11.1/es/core.min.js"
  );
  const grammar = await fetch(
    "https://cdn.jsdelivr.net/gh/redmer/highlightjs-turtle@v2.1.0/src/languages/turtle.js"
  ).then(response => response.text());
  const defineTurtle = new Function(`${grammar}\nreturn hljsDefineTurtle;`)();
  hljs.registerLanguage("turtle", defineTurtle);

  for (const block of blocks) {
    block.innerHTML = hljs.highlight(block.textContent, { language: "turtle" }).value;
    block.classList.add("hljs");
  }
}

let respecConfig = {
  useLogo: true,
  useLabel: true,

  title: "Onderzoek logboek dataverwerkingen voor (geo) objecten",
  specStatus: "basis",
  specType: "hr",
  pubDomain: "ldv",
  shortName: "logboek-dataverwerkingen-voor-objecten",
  license: "cc-by",

  //-- publishDate is verplicht en bepaalt de map op docs.geostandaarden.nl.
  //-- Werk deze bij vlak voor het aanmaken van een release.
  publishDate: "2026-09-24",
  publishVersion: [],

  edDraftURI: "https://geonovum.github.io/logboek-dataverwerkingen-voor-objecten/",

  editors: [
    {
      name: "Niels Hoffmann",
      company: "Geonovum",
      companyURL: "https://www.geonovum.nl",
    },
    {
      name: "Frank Terpstra",
      company: "Geonovum",
      companyURL: "https://www.geonovum.nl",
    }
  ],

  authors: [
    {
      name: "Niels Hoffmann",
      company: "Geonovum",
      companyURL: "https://www.geonovum.nl",
    },
    {
      name: "Frank Terpstra",
      company: "Geonovum",
      companyURL: "https://www.geonovum.nl",
    }
  ],

  github: "https://github.com/Geonovum/logboek-dataverwerkingen-voor-objecten",
  maxTocLevel: 3,

  postProcess: [
    ...(organisationConfig.postProcess ?? []),
    localizeGitHubHeaderLinks,
    highlightTurtle
  ],

  localBiblio: {
        
        LDV: {
            title: "Logboek Dataverwerkingen",
            href: "https://logius-standaarden.github.io/logboek-dataverwerkingen/",
            publisher: "Logius"
        },
        JB_LDV: {
            title: "Juridisch Beleidskader - Logboek Dataverwerking",
            href: "https://logius-standaarden.github.io/publicatie/api/Logboek_Juridisch/",
            publisher: "Logius"
        },
        NL_SBB: {
            title: "NL-SBB - Standaard voor het beschrijven van begrippen",
            href: "https://docs.geostandaarden.nl/nl-sbb/def-st-nl-sbb-20241010/",
            publisher: "Geonovum"
        },
        DCAT_AP_NL: {
            title: "DCAT-AP-NL - Nederlands profiel voor DCAT",
            href: "https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/",
            publisher: "Geonovum"
        },
        PROV_O: {
            title: "PROV-O: The PROV Ontology",
            href: "https://www.w3.org/TR/prov-o/",
            publisher: "W3C"
        },
        PROV_DM: {
            title: "PROV-DM: The PROV Data Model",
            href: "https://www.w3.org/TR/prov-dm/",
            publisher: "W3C"
        },
        DPV: {
            title: "Data Privacy Vocabulary",
            href: "https://w3c.github.io/dpv/2.1/dpv/",
            publisher: "W3C Community Group"
        },
        GDPR: {
            title: "General Data Protection Regulation",
            href: "https://eur-lex.europa.eu/eli/reg/2016/679/oj",
            publisher: "EU"
        },
        DPROD: {
            title: "Data Product Ontology (DPROD)",
            href: "https://ekgf.github.io/dprod/",
            publisher: "Enterprise Knowledge Graph Forum, Object Management Group® (OMG®)"
        },
  },
};

function localizeGitHubHeaderLinks(_config, document) {
  if (document.documentElement.lang !== "nl") {
    return;
  }

  const issueLink = document.querySelector(
    '.head dl a[href$="/issues/"], .head dl a[href$="/issues"]'
  );
  if (issueLink) {
    issueLink.textContent = "Alle issues";
  }
}
