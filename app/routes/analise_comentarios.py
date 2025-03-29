from fastapi import APIRouter
from app.services.ai_service import analisarcomentario
from app.schemas.str import StringListRequest

router = APIRouter()

@router.post("/evaluate", response_model=)
def analisar_Comentarios(request: StringListRequest):

    return CreditService.evaluate_credit(request)
