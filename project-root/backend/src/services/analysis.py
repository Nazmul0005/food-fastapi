import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

class ImageAnalyzer:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY") # Debugging line to check if the key is loaded
        if not self.api_key:
            raise ValueError("Google API Key not found")
        
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp-image-generation", 
            google_api_key=self.api_key
        )

    async def analyze_image(self, image_bytes: str, prompt: str) -> str:
        try:
            image_message = {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_bytes}"},
            }
            text_message = {"type": "text", "text": prompt}
            message = HumanMessage(content=[text_message, image_message])
            response = self.llm.invoke([message])
            return response.content
        except Exception as e:
            raise Exception(f"Analysis failed: {str(e)}")