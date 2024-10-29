import streamlit as st
import sys
from pathlib import Path
sys.path.append("./check_uniform")
from check_uniform_lib import get_response_from_model
import json
from PIL import Image
import io

def check_uniform():
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .title-container {
            background-color: #232F3E;
            padding: 2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
        }
        .upload-container {
            border: 2px dashed #cccccc;
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            margin: 1rem 0;
        }
        .result-container {
            background-color: #f5f5f5;
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 2rem;
        }
        .stButton > button {
            background-color: #FF9900;
            color: white;
            font-weight: bold;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #FF8000;
        }
        .info-box {
            background-color: #E6F3FF;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
        <div class="title-container">
            <h1>AWS First Cloud Journey Uniform Detection</h1>
            <p>Verify if someone is wearing an AWS First Cloud Journey shirt using AI</p>
        </div>
    """, unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("### 📸 Upload Image")
        st.markdown("""
            <div class="info-box">
            ℹ️ Supported formats: JPG, JPEG, PNG<br>
            📏 Recommended size: Up to 5MB<br>
            🎯 Best results: Well-lit, clear front view
            </div>
        """, unsafe_allow_html=True)
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Drop your image here or click to browse",
            type=['jpg', 'jpeg', 'png'],
            help="Upload a clear image showing the person and their clothing"
        )

        if uploaded_file:
            # Preview container
            st.markdown("### 🖼️ Preview")
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)
            
            # Image details
            file_details = {
                "📄 Filename": uploaded_file.name,
                "📦 Size": f"{uploaded_file.size / 1024:.1f} KB",
                "🖼️ Dimensions": f"{image.size[0]}x{image.size[1]} px"
            }
            st.json(file_details)

    with col2:
        st.markdown("### 🎯 Detection Results")
        
        # Analysis button
        analyze_button = st.button(
            "🔍 Analyze Image",
            disabled=not uploaded_file,
            help="Click to start uniform detection"
        )

        if analyze_button and uploaded_file:
            with st.spinner("🔄 Analyzing image..."):
                try:
                    # Get image bytes
                    image_bytes = uploaded_file.getvalue()
                    
                    # Get response from model
                    response_stream = get_response_from_model(image_bytes)
                    
                    # Process response
                    with st.container():
                        st.markdown("#### 📊 Analysis Results")
                        
                        # Create a placeholder for the result
                        result_placeholder = st.empty()
                        
                        # Process the stream
                        full_response = ""
                        for chunk in response_stream:
                            if chunk:
                                full_response += chunk
                        
                        try:
                            result = json.loads(full_response)
                            
                            # Display result with formatting
                            status = "✅" if "wearing" in result["isConfirm"].lower() else "❌"
                            
                            result_placeholder.markdown(f"""
                                <div class="result-container">
                                    <h4>{status} Detection Result</h4>
                                    <p><strong>Status:</strong> {result['isConfirm']}</p>
                                    <p><strong>Explanation:</strong> {result['explain']}</p>
                                </div>
                            """, unsafe_allow_html=True)
                            
                            # Add download button for results
                            st.download_button(
                                label="📥 Download Results",
                                data=json.dumps(result, indent=2),
                                file_name="detection_results.json",
                                mime="application/json"
                            )
                            
                        except json.JSONDecodeError:
                            st.error("Error parsing results. Please try again.")
                            
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.button("🔄 Retry Analysis")

        # Help section
        with st.expander("❓ Help & Tips"):
            st.markdown("""
                ### How to get the best results:
                1. Ensure the person's face and upper body are clearly visible
                2. Use well-lit images
                3. Avoid blurry or dark photos
                4. Make sure the AWS First Cloud Journey logo/text is visible if present
                
                ### What we check for:
                - Presence of faces in the image
                - AWS First Cloud Journey shirt design
                - AWS certification badges
                - Image quality and clarity
                
                ### Having issues?
                - Try uploading a different image
                - Ensure the image meets size requirements
                - Check if the person's clothing is clearly visible
            """)

if __name__ == "__main__":
    check_uniform()