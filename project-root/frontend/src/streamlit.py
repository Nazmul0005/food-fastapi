import streamlit as st
import requests
import io
import base64
from PIL import Image

API_URL = "http://localhost:8000/api/v1/analyze"

st.title("Food Image Analyzer")
st.write("Upload a picture of food, and the AI will estimate its calories and ingredients.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

    st.write("Analyzing the image...")

    # Make API request with file upload
    try:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL, files=files)
        result = response.json()
        
        if result.get("content"):
            st.subheader("Analysis Result:")
            st.write(result["content"])
        else:
            st.error(f"Analysis failed: {result.get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Request failed: {str(e)}")

# Add instructions
st.sidebar.header("How to Run")
st.sidebar.info(
    "1. Start the backend server:\n"
    "   ```bash\n"
    "   cd backend\n"
    "   uvicorn src.main:app --reload\n"
    "   ```\n\n"
    "2. Start the Streamlit frontend:\n"
    "   ```bash\n"
    "   cd frontend\n"
    "   streamlit run src/streamlit.py\n"
    "   ```"
)