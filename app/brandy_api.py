from fastapi import FastAPI, HTTPException
from app.brandy import generate_branding_snippet, generate_keywords
from mangum import Mangum

MAX_INPUT_LENGTH = 12


app = FastAPI()
handler = Mangum(app)


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}


@app.get("/keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/keywords_and_snippets")
async def generate_keywords_and_snippets(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"keywords": keywords, "snippet": snippet}


def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=404,
            detail=f"Input length must be less than {MAX_INPUT_LENGTH} characters",
        )
