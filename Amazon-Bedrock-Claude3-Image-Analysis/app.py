import streamlit as st
from pathlib import Path
import os
from dotenv import load_dotenv
from analyze_images import analyze_image
import json

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Image Analyzer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .upload-text {
        font-size: 1.2rem;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

def validate_json(json_str):
    """Validate JSON format"""
    if not json_str:
        return True
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False

def main():
    # Title and description
    st.title("🔍 Image Analysis with Amazon Bedrock and Claude 3")
    
    with st.expander("ℹ️ How to use this application", expanded=True):
        st.markdown("""
        1. **Upload an image** using the file uploader below
        2. (Optional) Provide a custom JSON specification to control the analysis
        3. Click **Analyze Image** to process your image
        
        The analysis will return detailed information about the image content.
        """)
    
    # Create two columns for layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("📤 Image Upload")
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["png", "jpg", "jpeg"],
            help="Supported formats: PNG, JPG, JPEG"
        )
        
        if uploaded_file:
            st.image(uploaded_file, caption="Preview", use_column_width=True)
    
    with col2:
        st.subheader("⚙️ Analysis Settings")
        json_spec = st.text_area(
            "Custom JSON Specification (Optional)",
            placeholder='Example: {"attributes": ["colors", "objects", "text"]}',
            help="Enter a valid JSON to customize the analysis output"
        )
        
        # JSON validation
        if json_spec and not validate_json(json_spec):
            st.error("Invalid JSON format. Please check your input.")
            return
        
        # Generate analysis prompt
        prompt = f"Analyze this image in extreme detail. Please return a JSON response with the most relevant details of the image."
        if json_spec:
            prompt += f" Use this JSON specification to categorize the image: {json_spec}"
        
        # Analysis button
        analyze_button = st.button(
            "🔍 Analyze Image",
            disabled=not uploaded_file,
            help="Click to start image analysis"
        )
    
    # Results section
    if analyze_button and uploaded_file:
        with st.spinner("Analyzing image..."):
            try:
                # Save uploaded file temporarily
                save_folder = Path("./images")
                save_folder.mkdir(exist_ok=True)
                save_path = save_folder / uploaded_file.name
                
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                
                # Process image
                results = analyze_image(save_path, prompt)
                
                # Display results
                st.subheader("📊 Analysis Results")
                
                # Try to format JSON results if possible
                try:
                    if isinstance(results, str):
                        formatted_results = json.loads(results)
                        st.json(formatted_results)
                    else:
                        st.write(results)
                except json.JSONDecodeError:
                    st.write(results)
                
                # Cleanup
                os.remove(save_path)
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")

if __name__ == "__main__":
    main()