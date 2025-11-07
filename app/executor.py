import asyncio
import tempfile
import subprocess
import time

async def execute_code(code: str, test_input: str, language: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode())
        tmp.flush()
        start = time.time()

        try:
            proc = await asyncio.create_subprocess_exec(
                "python3", tmp.name,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc.communicate(input=test_input.encode())

            end = time.time()
            runtime = round(end - start, 3)
            return {
                "output": stdout.decode().strip(),
                "error": stderr.decode().strip(),
                "time": runtime
            }
        except Exception as e:
            return {"error": str(e), "output": "", "time": 0}
