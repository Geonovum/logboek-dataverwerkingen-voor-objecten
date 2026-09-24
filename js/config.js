async function loadTurtle() {
  //this is the function you call in 'preProcess', to load the highlighter
  const worker = await new Promise(resolve => {
    require(["core/worker"], ({ worker }) => resolve(worker));
  });
  const action = "highlight-load-lang";
  const langURL =
    "https://cdn.jsdelivr.net/gh/redmer/highlightjs-turtle/src/languages/turtle.js";
  const propName = "hljsDefineTurtle"; // This funtion is defined in the highlighter being loaded
  const lang = "turtle"; // this is the class you use to identify the language
  worker.postMessage({ action, langURL, propName, lang });
  return new Promise(resolve => {
    worker.addEventListener("message", function listener({ data }) {
      const { action: responseAction, lang: responseLang } = data;
      if (responseAction === action && responseLang === lang) {
        worker.removeEventListener("message", listener);
        resolve();
      }
    });
  });
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

  preProcess: [loadTurtle],

  postProcess: [
    ...(organisationConfig.postProcess ?? []),
    localizeGitHubHeaderLinks
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
