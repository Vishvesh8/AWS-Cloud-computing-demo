import uvicorn
from fastapi import APIRouter, Depends, FastAPI
from starlette.middleware.cors import CORSMiddleware


from pydantic import BaseModel

from celery.result import AsyncResult

####################################################
class ner_data:
    text : str
#####################################################

router = APIRouter()


app = FastAPI()


@app.get('/')
async def root():
    return "Welcome to AWS Cloud computing demo!"



import spacy

nlp = spacy.load("en_core_web_sm")

@app.post('/named-entity-recognition/')
async def ner(data: ner_data):
    doc = nlp(data.text)
    return_string = ""
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        return_string = return_string + str(ent.text) + " -> " + str(ent.label_) + "\n"

    return return_string
