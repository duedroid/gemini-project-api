from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.llm import CompletionsRequest
from app.services.llm_gemini import generate_content_stream


router = APIRouter()


@router.post("/completions")
async def llm_completions(data: CompletionsRequest):
    return StreamingResponse(generate_content_stream(data.message), media_type="text/event-stream")