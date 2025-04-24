from fastapi import APIRouter, HTTPException, UploadFile, File
from .models.schemas import ImageAnalysisResponse
from .services.analysis import ImageAnalyzer
import base64
from io import BytesIO
from PIL import Image

router = APIRouter()
analyzer = ImageAnalyzer()

@router.post("/analyze", response_model=ImageAnalysisResponse)
async def analyze_image(file: UploadFile = File(...)):
    try:
        # Read and validate the image
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        
        # Convert image to JPEG format and base64
        img_byte_arr = BytesIO()
        if image.format == 'PNG':
            image = image.convert('RGB')
        image.save(img_byte_arr, format='JPEG')
        img_bytes_b64 = base64.b64encode(img_byte_arr.getvalue()).decode()

        # Fixed prompt
        prompt = "Analyze this food image. Estimate the total calories and list the main ingredients needed to make this dish."
        
        # Analyze image
        content = await analyzer.analyze_image(img_bytes_b64, prompt)
        return ImageAnalysisResponse(content=content)
    except Exception as e:
        return ImageAnalysisResponse(content=None, error=str(e))