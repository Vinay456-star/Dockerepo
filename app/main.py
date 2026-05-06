from fastapi import FastAPI # type: ignore
from elasticsearch import Elasticsearch # type: ignore

app = FastAPI()

# 🔥 connect to Elasticsearch on host
es = Elasticsearch("http://host.docker.internal:9200")

@app.get("/")
def home():
    return {"message": "FastAPI + Elasticsearch running"}

@app.post("/add")
def add_doc(name: str):
    es.index(index="users", document={"name": name})
    return {"status": "added"}

@app.get("/search")
def search(q: str):
    result = es.search(index="users", query={
        "match": {"name": q}
    })
    return result