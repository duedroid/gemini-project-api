from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from .llm import router as llm_router


api_router_v1 = APIRouter(default_response_class=ORJSONResponse)
api_router_v1.include_router(llm_router, prefix='/llm', tags=['llm'])