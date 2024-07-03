from fastapi import FastAPI
from typing import Dict, Any
from src.pci_api import *

app = FastAPI()

@app.get("/")
def concursos_root():
    return {"https://api-pci.vercel.app/estado/{Estado}": "exemplo: /estado/MS"}     

@app.get("/estado/{item_id}")
def estado(item_id: str) -> Dict[str, Any]:
    json = dict()

    # Extract one state
    state = exam_region(soup, item_id.upper())

    for key, value in enumerate(state):
        if ( key != 0 ):
            name = state[key][0]
            for i in range(1, len(value)):
                analysis[state[0][i]] = state[key][i]
            json[name] = analysis
        analysis = dict()

    return json 