from fastapi import FastAPI, UploadFile, Form
import asyncio
from app.executor import execute_code
from app.grader import grade_submission
from app.plagiarism import check_similarity

app = FastAPI(title="Code Execution Service")

@app.post("/run")
async def run_code(
    file: UploadFile,
    language: str = Form("python"),
    expected_output: str = Form(""),
    test_input: str = Form(""),
):
    code = await file.read()
    code = code.decode()

    # 1️⃣ Execute code
    result = await execute_code(code, test_input, language)

    # 2️⃣ Grade result
    score = grade_submission(result["output"], expected_output)

    return {
        "execution": result,
        "score": score,
    }

@app.post("/check-plagiarism")
async def check_plagiarism(code1: UploadFile, code2: UploadFile):
    c1 = (await code1.read()).decode()
    c2 = (await code2.read()).decode()
    similarity = check_similarity(c1, c2)
    return {"similarity_percent": similarity}
