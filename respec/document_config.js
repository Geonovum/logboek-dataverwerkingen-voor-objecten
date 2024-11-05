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

var documentConfig =
{
  title: "Standaard logboek dataverwerkingen voor (geo) objecten",
  shortName: "logboek-dataverwerkingen-voor-objecten",
  pubDomain: "logboek-dataverwerkingen-voor-objecten",
  specStatus: "wv",
  specType: "hr",
  license: "cc-by",
//  latestVersion: [
//    "https://docs.geostandaarden.nl/NL-SBB"
//  ],
//  publishDate: "2024-04-16",
//  previousPublishDate: "2024-03-01",
//  previousMaturity: "vv",
  edDraftURI: "https://geonovum.github.io/logboek-dataverwerkingen-voor-objecten/",
  authors: [
        {
            name: "Niels Hoffmann (Geonovum)"
        },
        {
            name: "Frank Terpstra (Geonovum)"
        }
  ],
  editors: [
        {
            name: "Niels Hoffmann (Geonovum)"
        },
        {
            name: "Frank Terpstra (Geonovum)"
        }
  ],
  
    github: "geonovum/logboek-dataverwerkingen-voor-objecten",
    issueBase: "https://github.com/Geonovum/logboek-dataverwerkingen-voor-objecten/issues",
    maxTocLevel: 3,
    
    labelColor: {
        def: "#045D9F",
        wv: "#FF0000",
        cv: "#045D9F",
        vv: "#045D9F",
        basis: "#80CC28",
    },
 
    nl_organisationName: "Geonovum",
    nl_organisationPublishURL: "https://docs.geostandaarden.nl",

	latestVersion: ["nl_organisationPublishURL", "pubDomain", "/", "shortName", "/"],
    thisVersion: ["nl_organisationPublishURL", "pubDomain", "/", "specStatus", "-", "specType", "-", "shortName", "-", "publishDate"],
    prevVersion: ["nl_organisationPublishURL", "pubDomain", "/", "previousMaturity", "-", "specType", "-", "shortName", "-", "previousPublishDate"],


  localBiblio: {
         SKOS: 
            {
                "authors": [
                    "Alistair Miles",
                    "Sean Bechhofer"
                ],
                "href": "https://www.w3.org/TR/skos-reference/",
                "title": "SKOS Simple Knowledge Organization System Reference",
                "status": "REC",
                "publisher": "W3C",
                "deliveredBy": [
                    {
                        "url": "https://www.w3.org/2006/07/SWD/",
                        "shortname": "swd"
                    }
                ],
                "versions": [
                    "skos-reference-20090818",
                    "skos-reference-20090615",
                    "skos-reference-20090317",
                    "skos-reference-20080829",
                    "skos-reference-20080609",
                    "skos-reference-20080125"
                ],
                "obsoletes": [
                    "swbp-skos-core-spec"
                ],
                "id": "skos-reference",
                "date": "18 August 2009"
            },
        NLAPI: {
            title: "Nederlandse API strategie",
            href: "https://docs.geostandaarden.nl/api/API-Strategie/",
            status: "Vastgesteld",
            date: "09 maart 2022",
            publisher: "Geonovum",
        },
        B1: {
            title: "Taalniveau B1",
            href: "https://www.communicatierijk.nl/vakkennis/rijkswebsites/aanbevolen-richtlijnen/taalniveau-b1",
        },
        PTOLULijst: {
            title: "Pas-Toe-Of-Leg-Uit lijst van open standaarden",
            href: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht",
            publisher: "Forum Standaardisatie",
        },
        PTOLU: {
            title: "pas-toe-of-leg-uit",
            href: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht",
            publisher: "Forum Standaardisatie",
        },
        SKOSLEX: {
            title: "Skos-lex",
            href: "http://bp4mc2.org/def/skos-lex",
            publisher: "bp4mc2",
        },
        ISO25964: {
            title: "ISO 25964",
            href: "https://www.niso.org/schemas/iso25964",
            publisher: "NISO",
        },
        WETTENNL: {
            title: "Wetten.nl",
            href: "https://linkeddata.overheid.nl/terms/",
            publisher: "KOOP",
        },
        ASSET: {
            authors: [
                "Phil Archer",
                "Gofran Shukair"
            ],
            href: "https://www.w3.org/TR/vocab-adms/#asset",
            title: "semantische asset",
            status: "NOTE",
            publisher: "W3C",
            deliveredBy: [
                {
                    "url": "https://www.w3.org/2011/gld/",
                    "shortname": "gld"
                }
            ],
            id: "vocab-adms-asset",
            date: "1 August 2013"
        },
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
        NLSBB: {
            title: "NL-SBB - Standaard voor het beschrijven van begrippen",
            href: "https://docs.geostandaarden.nl/nl-sbb/def-st-nl-sbb-20241010/",
            publisher: "Geonovum"
        },
        PROV_O: {
            title: "PROV-O: The PROV Ontology",
            href: "https://www.w3.org/TR/prov-o/",
            publisher: "W3C"
        }
  },
  preProcess: [loadTurtle],
}