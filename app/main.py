from fastapi import FastAPI
from uuid import uuid4 as uuid
from typing import Union
from utils.generate_embeddings import chain, search_index,template

app = FastAPI()

@app.get("/")
async def root(question: str):
    return {"message": "Hello World"}

@app.get("/chat")
async def chat(question: str):
    answer =  chain(
            {
                "input_documents": search_index.similarity_search(question, k=4),
                "question": template.format(input=question),
            },
            return_only_outputs=True,
        )["output_text"]
    return {"answer": answer}