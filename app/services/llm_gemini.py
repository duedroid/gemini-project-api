import asyncio

import orjson
import google.generativeai as genai


model = genai.GenerativeModel(model_name="gemini-1.5-flash")


async def generate_content_stream(input_message: str):
    response = model.generate_content(input_message, stream=True)
    for chunk in response:
        data = orjson.dumps({"message": chunk.text, "status": "stream"}).decode()
        yield f"data: {data}\n\n"
        await asyncio.sleep(0.01)

    yield 'data: {"status": "end"}\n\n'