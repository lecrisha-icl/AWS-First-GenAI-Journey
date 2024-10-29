import streamlit as st
import sys
from pathlib import Path
import json
import io
from PIL import Image
import time

# Add Libs path
sys.path.append(str(Path("../Libs")))
import Libs as lib

def load_image(image_bytes):
    """Load and validate image from bytes."""
    try:
        image = Image.open(io.BytesIO(image_bytes))
        return image
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def process_detection(text_prompt, image_bytes):
    """Process object detection with error handling."""
    try:
        with st.spinner("Analyzing image..."):
            response = lib.get_response_from_model(text_prompt, image_bytes)
            return response
    except Exception as e:
        st.error(f"Error during detection: {str(e)}")
        return None

def main():
    # Custom CSS
    st.markdown("""
        <style>
        .upload-text {
            font-size: 1.2rem;
            font-weight: 500;
            margin-bottom: 1rem;
        }
        .stButton > button {
            width: 100%;
            margin-top: 1rem;
        }
        .results-container {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #f8f9fa;
            margin-top: 1rem;
        }
        .image-preview {
            border: 2px dashed #ccc;
            border-radius: 0.5rem;
            padding: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("🔍 Object Detection and Analysis")
    
    # Create two columns for input
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Input Your Query")
        input_text = st.text_area(
            "What would you like to detect or analyze?",
            placeholder="E.g., 'Count the number of people in the image' or 'Describe the objects in the scene'",
            height=100
        )
        
        # Example queries
        with st.expander("📋 Example Queries"):
            st.markdown("""
            - Count number of pigs in the image
            - Describe the main objects in the scene
            - Generate Katalon code to test the page
            - List all visible animals
            - Analyze the spatial arrangement of objects
            """)

    with col2:
        st.markdown("### 🖼️ Upload Image")
        uploaded_file = st.file_uploader(
            "Upload an image (PNG or JPEG)",
            type=['png', 'jpeg', 'jpg'],
            key="image_uploader"
        )

        if uploaded_file:
            try:
                image_bytes = uploaded_file.getvalue()
                image_preview = load_image(image_bytes)
                
                if image_preview:
                    with st.container():
                        st.markdown("#### Preview")
                        st.image(image_preview, use_column_width=True)
                        
                        # Image details
                        file_details = {
                            "Filename": uploaded_file.name,
                            "File size": f"{len(image_bytes)/1024:.1f} KB",
                            "Image size": f"{image_preview.size[0]}x{image_preview.size[1]} px"
                        }
                        st.write("📄 File Details:", file_details)
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
                image_bytes = None

    # Analysis button and results
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button(
            "🔍 Analyze Image",
            disabled=not (uploaded_file and input_text),
            type="primary"
        )

    if analyze_button and uploaded_file and input_text:
        try:
            # Create a container for results
            with st.container():
                st.markdown("### 📊 Analysis Results")
                response_stream = process_detection(input_text, image_bytes)
                
                if response_stream:
                    with st.expander("🔍 Detailed Results", expanded=True):
                        st.write_stream(response_stream)
                        
                        # Add option to download results
                        st.download_button(
                            label="📥 Download Results",
                            data=str(response_stream),
                            file_name="detection_results.txt",
                            mime="text/plain"
                        )
        except Exception as e:
            st.error(f"An error occurred during analysis: {str(e)}")
            st.button("🔄 Retry Analysis")

    # Help section
    with st.expander("❓ Help & Tips"):
        st.markdown("""
        ### How to use:
        1. Enter your question or analysis request in the text area
        2. Upload an image you want to analyze
        3. Click 'Analyze Image' to get results
        
        ### Tips:
        - Use clear, specific questions
        - Ensure images are well-lit and clear
        - Larger images may take longer to process
        
        ### Supported Formats:
        - PNG
        - JPEG/JPG
        """)

if __name__ == "__main__":
    main()