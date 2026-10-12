from fastapi import FastAPI

app = FastAPI(
    title="TestOps AI",
    description="AI-assisted test automation and failure prediction",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}