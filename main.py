from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import API

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://195.20.233.61:4891"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestAsk(BaseModel):
    text: str


@app.post('/')
def receive(item: RequestAsk):
    chatbot = API.ChatBot()
    response = dict()
    response['response'] = chatbot.receive_answer(item.text)["choices"][0]["text"].split("\n")[1:]
    return response


@app.get('/')
def receive():
    response = dict()
    response['message'] = 'API Running!'
    return response
