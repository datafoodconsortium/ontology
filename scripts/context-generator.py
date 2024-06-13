import re, argparse

parser = argparse.ArgumentParser(description="Generate JSON-LD context from an ontology file")

# add argument that should end with .rdf
parser.add_argument('input', type=str, help='Input file path (should end with .rdf)')

# add argument that should end with .json
parser.add_argument('output', type=str, help='Output file path (should end with .json)')

assert parser.parse_args().input.endswith('.rdf'), "Input file should end with .rdf"
assert parser.parse_args().output.endswith('.json'), "Output file should end with .json"

args = parser.parse_args()

input_filepath = args.input

with open(input_filepath, "r") as ontology_f:
    ontology_text = ontology_f.read()

ontology_text = ontology_text.split("\n")

with open(args.output, "w") as export_context_f:

    export_context_f.write("""{
    "@context": {
    \t"rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    \t"skos" : "http://www.w3.org/2004/02/skos/core#",
    \t"dfc": "https://github.com/datafoodconsortium/ontology/releases/latest/download/DFC_FullModel.owl#",
    \t"dc": "http://purl.org/dc/elements/1.1/#",
    \t"dfc-b": "https://github.com/datafoodconsortium/ontology/releases/latest/download/DFC_BusinessOntology.owl#",
    \t"dfc-t": "https://github.com/datafoodconsortium/ontology/releases/latest/download/DFC_TechnicalOntology.owl#",
    \t"dfc-m": "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/measures.rdf#",
    \t"dfc-pt": "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#",
    \t"dfc-f": "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/facets.rdf#",
    \t"dfc-v": "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/vocabulary.rdf#",
    \t"ontosec": "http://www.semanticweb.org/ontologies/2008/11/OntologySecurity.owl#\"""")

    for line in ontology_text:
        if re.findall(r"<owl:ObjectProperty (\S+)>", line):
            line = re.sub("<owl:ObjectProperty rdf:about=\"", "", line)
            line = re.sub("\">", "", line)
            line = re.sub("/>", "", line)
            line = re.sub("\"", "", line)
            line = re.sub("https://github.com/datafoodconsortium/ontology/releases/latest/download/DFC_BusinessOntology.owl#", "dfc-b:", line)
            line = re.sub("\t", "", line)
            line = re.sub("    ", "", line)
            if not bool(re.search('http(\S+)', line)):
                export_context_f.write(",\n")
                export_context_f.write(f"\t\t\"{line}")
                export_context_f.write("\": {\n")
                export_context_f.write("\t\t\t\"@type\": \"@id\"\n")
                export_context_f.write("\t\t}")
    
    export_context_f.write(""",
		"dfc-t:represent": {
			"@type": "@id"
		},
		"dfc-t:hasPivot": {
			"@type": "@id"
		},
		"dfc-t:hostedBy": {
			"@type": "@id"
		},
		"dfc-t:owner": {
			"@type": "@id"
		}""")

    export_context_f.write("\n\t}\n}")
                                       