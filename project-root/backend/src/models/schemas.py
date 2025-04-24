from pydantic import BaseModel

class ImageAnalysisResponse(BaseModel):
    content: str | None
    error: str | None = None