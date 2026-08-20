from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    filename: str

app = FastAPI(
    title="AI Knowledge Assistant",
    description="Backend API for an AI-powered knowledge assistant",
    version="0.1.0",
)
documents = [
    {
        "id": 1,
        "filename": "machine_learning.pdf"
    },
    {
        "id": 2,
        "filename": "nlp_notes.pdf"
    },
    {
        "id": 3, 
        "filename": "rag.pdf"
    }
]
@app.get("/documents")
def get_documents():
    return documents
@app.get("/heath")
def health_check():
    return {" status" : "ok "}

@app.post("/documents")
def create_document(document: DocumentCreate):
    new_document = {
        "id" : len(documents) + 1,
        "filename" : document.filename
    }
    documents.append(new_document)
    return document

@app.get("/documents/{document_id}")
def get_document(document_id:int):
    for document in documents:
        if document["id"] == document_id:
            return document

@app.delete("/documents/{document_id}")
def delete_document(document_id: int):
    for document in documents:
        if document["id"] == document_id:
            documents.remove(document)
            return {"message" : "Document deleted successfully"}
    raise HTTPException(
        status_code = 404,
        detail = "Document not found"
    )
            
