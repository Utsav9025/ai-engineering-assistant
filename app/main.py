from fastapi import FastAPI

app = FastAPI(
    title="AI Knowledge Assistant",
    description="Backend API for an AI-powered knowledge assistant",
    version="0.1.0",
)

@app.get("/heath")
def health_check():
    return {" status" : "ok "}