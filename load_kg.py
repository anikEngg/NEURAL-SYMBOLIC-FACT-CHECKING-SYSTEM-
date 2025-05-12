from rdflib import Graph

def load_knowledge_graph(path: str):
    g = Graph()
    g.parse(path, format="ttl")
    return g

def query_kg(graph, subject, predicate, obj):
    s, p, o = subject.lower(), predicate.lower(), obj.lower()
    for triple in graph:
        if all([
            s in triple[0].lower(),
            p in triple[1].lower(),
            o in triple[2].lower()
        ]):
            return True
    return False
