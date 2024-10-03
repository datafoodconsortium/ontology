import argparse

import numpy as np
import rdflib

QUERY_CONCEPTS = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    SELECT ?s ?p ?o
    WHERE {
        {
            ?s a skos:Concept .
        } UNION {
            ?s a skos:Collection .
        }
        ?s ?p ?o .
    }
"""

def clean_key(key):
    key_split = key.split("#")
    namespace = "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/measures.rdf#"

    old_uri = key_split[1]
    new_uri = old_uri[0].lower() + old_uri[1:]

    key = namespace + new_uri
    return new_uri

def create_dict_cleaned_uri(graph_file):
    # Create a Graph object
    graph = rdflib.Graph()
    # Read the TTL file into the graph
    graph.parse(graph_file, format='ttl')

    # Run the query
    results = graph.query(QUERY_CONCEPTS)

    concepts = {}
    for row in results:
        concepts[str(row.s)] = np.append(concepts.get(str(row.s), np.array([])), (row.p, row.o))

    dict_old_uri_to_clean = {
        key.split("#")[1] : clean_key(key) for key in concepts.keys()
    }

    return dict_old_uri_to_clean

def apply_mapping(line, old_to_new):
    for old, new in old_to_new.items():
        line = line.replace(":" + old, ":" + new)
    return line

parser = argparse.ArgumentParser(description="Generate updated taxonomy file with camelCase URIs and deprecated old URIs")

parser.add_argument('input', type=str, help='Input file path (should end with .ttl)')
parser.add_argument('output', type=str, help='Output file path (should end with .ttl')

args = parser.parse_args()

GRAPH_FILE         = args.input
CLEANED_GRAPH_FILE = args.output

dict_old_uri_to_clean = create_dict_cleaned_uri(GRAPH_FILE)

with open(GRAPH_FILE, 'r') as read_file:
    with open(CLEANED_GRAPH_FILE, 'w') as write_file:
        old_paragraph, new_paragraph = "", ""
        old_uri, new_uri             = "", ""

        for line in read_file.readlines():
            # Prefixes
            if line[0] == "@":
                write_file.write(line)

            # Update URIs and prepare exactMatch
            elif ":" in line:
                if "owl:Ontology" not in line and "github" not in line and "prefLabel" not in line and "Class" not in line:
                    line = line.replace(".", ";")
                # print(line)
                old_paragraph += line
                new_paragraph += apply_mapping(line, dict_old_uri_to_clean)

                if "skos:Concept;" in line or "skos:Collection;" in line:
                    old_uri = line.split(" ")[0]
                    new_uri = apply_mapping(old_uri, dict_old_uri_to_clean)

            # Write the paragraph
            elif len(line) == 1:
                write_file.write("\n")
                if "skos:Concept;" in old_paragraph or "skos:Collection;" in old_paragraph:

                    old_paragraph += "  skos:exactMatch " + new_uri + " ;\n"
                    new_paragraph += "  skos:exactMatch " + old_uri + " .\n"

                    old_paragraph += "  owl:deprecated true .\n\n"

                    write_file.write(old_paragraph)
                    write_file.write(new_paragraph)
                    
                    old_paragraph, new_paragraph = "", ""
                    old_uri, new_uri             = "", ""
                else:
                    write_file.write(new_paragraph)
                    
                    old_paragraph, new_paragraph = "", ""
                    old_uri, new_uri             = "", ""
            else:
                old_paragraph += line
                new_paragraph += line
