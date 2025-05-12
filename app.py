from fastapi import FastAPI
from pydantic import BaseModel
from src.load_kg import load_knowledge_graph, query_kg
from src.neural_checker import neural_fact_check

app = FastAPI()
graph = load_knowledge_graph("data/knowledge_graph.ttl")

class Claim(BaseModel):
    subject: str
    predicate: str
    obj: str
    text: str

@app.post("/fact-check")
def fact_check(claim: Claim):
    kg_result = query_kg(graph, claim.subject, claim.predicate, claim.obj)
    nn_label, nn_conf = neural_fact_check(claim.text)

    return {
        "knowledge_graph_result": kg_result,
        "neural_model_result": {
            "label": nn_label,
            "confidence": nn_conf
        }
    }
