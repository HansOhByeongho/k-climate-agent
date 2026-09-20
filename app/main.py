from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="k-climate-agent",version="0.3.0")
class Query(BaseModel): query:str
@app.get("/health")
def health(): return {"status":"ok","project":"k-climate-agent","version":"0.3.0"}
@app.post("/analyze")
def analyze(req:Query): return {"domain":"climate","query":req.query,"checks":["emissions","energy","climate risk","adaptation/mitigation"],"status":"prototype"}
