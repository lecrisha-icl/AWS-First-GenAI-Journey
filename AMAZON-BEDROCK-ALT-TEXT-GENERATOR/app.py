from datetime import datetime
from uuid import uuid4
import streamlit as st
import os
from pdf_image_alt_text_generator import generator
from pdf_image_alt_text_generator import download_results
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set page config
st.set_page_config(
    page_title="PDF Alt-Text Generator",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .stProgress .st-bo {
            background-color: #f0f2f6;
        }
        .success-message {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #d1fae5;
            color: #065f46;
        }
        .stButton button {
            width: 100%;
        }
        .image-container {
            border: 1px solid #e5e7eb;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session states
if "inference_started" not in st.session_state:
    st.session_state["inference_started"] = False
if "upload_uuid" not in st.session_state:
    st.session_state["upload_uuid"] = str(uuid4())
if "prompt_data" not in st.session_state:
    st.session_state["prompt_data"] = []

def set_inference_started():
    st.session_state["inference_started"] = True

def format_confidence_score(score):
    """Convert score to float and format it"""
    try:
        return float(score)
    except (ValueError, TypeError):
        return 0.0

@st.fragment
def image_box(alt_text_result):
    try:
        if alt_text_result is not None:
            with st.container(border=True):
                col1, col2 = st.columns([2, 3])
                
                # Image display with error handling
                with col1:
                    if "image" in alt_text_result:
                        st.image(
                            alt_text_result["image"],
                            width=200,
                            use_column_width="auto"
                        )
                    else:
                        st.error("⚠️ Error displaying image")
                
                # Alt text and metadata display
                with col2:
                    if "alt_text" in alt_text_result:
                        st.markdown("### Generated Alt Text")
                        st.write(alt_text_result["alt_text"])
                    else:
                        st.error("⚠️ Error generating alt text")
                    
                    # Create info columns
                    info_cols = st.columns(2)
                    with info_cols[0]:
                        if "score" in alt_text_result:
                            score = format_confidence_score(alt_text_result['score'])
                            st.write("**Confidence Score:**")
                            st.write(f"{score:.2f}")
                    with info_cols[1]:
                        if "page" in alt_text_result:
                            st.write("**Page Number:**")
                            st.write(int(alt_text_result['page']) + 1)
                    
                    # Metadata expansion
                    if "metadata" in alt_text_result:
                        with st.expander("View API Usage Details"):
                            st.json(alt_text_result["metadata"]["usage"])
        else:
            logger.warning("No alt text result for record")
    except Exception as e:
        logger.error(f"Error in image_box: {e}")
        st.error(f"Error processing image: {str(e)}")

def main():
    # Header section
    st.title("📄 PDF Alt-Text Generator")
    st.markdown("""
        Transform your PDF images with AI-powered alt text generation using Amazon Bedrock.
        Perfect for improving document accessibility!
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Controls")
        if st.button("🔄 Start New Session", use_container_width=True):
            st.session_state.clear()
            st.cache_data.clear()
            st.session_state["upload_uuid"] = str(uuid4())
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 📋 Instructions")
        st.markdown("""
            1. Upload your PDF file
            2. Wait for image extraction
            3. Click 'Start Inference' to generate alt text
            4. Download the results
        """)
    
    # Main content area
    file = st.file_uploader(
        "Choose a PDF file to process",
        type="pdf",
        key=st.session_state["upload_uuid"],
        disabled=st.session_state["inference_started"],
        help="Upload a PDF file containing images for alt text generation"
    )

    if file is not None and st.session_state["prompt_data"] is not None:
        try:
            if not st.session_state["prompt_data"]:
                with st.status("Processing PDF...", expanded=True) as status:
                    # File upload
                    status.update(label="📤 Uploading file...")
                    generator.save_pdf_file(file)
                    
                    # Data extraction
                    status.update(label="🔍 Extracting images...")
                    data, image_map = generator.load_pdf(file.name)
                    input_pdf = os.path.join("files", file.name).replace(" ", "_")
                    
                    # Data preparation
                    status.update(label="⚙️ Preparing data for AI model...")
                    st.session_state["prompt_data"] = generator.prep_data_for_model(
                        data, image_map
                    )
                    status.update(label="✅ PDF processed successfully!", state="complete")

            if st.session_state["prompt_data"]:
                st.markdown(f"### 📊 Processing Details")
                st.info(f"Found **{len(st.session_state['prompt_data'])}** images in the PDF")
                
                # Inference section
                if st.button(
                    "🚀 Start Alt Text Generation",
                    disabled=st.session_state["inference_started"],
                    on_click=set_inference_started,
                    type="primary",
                    use_container_width=True
                ):
                    try:
                        with st.spinner("Generating alt text for images..."):
                            st.session_state["full_result"] = generator.run_inference(
                                st.session_state["prompt_data"], image_box
                            )
                        st.success("✨ Alt text generation completed!")
                        logger.debug("Inference completed successfully")
                    except Exception as e:
                        logger.error(f"Inference error: {e}")
                        st.error(f"Failed to generate alt text: {str(e)}")
                
                # Download section
                if "full_result" in st.session_state and st.session_state["full_result"]:
                    try:
                        st.markdown("### 📥 Download Results")
                        st.session_state["alt_text_pdf"] = download_results.generate_pdf(
                            st.session_state["full_result"]
                        )
                        
                        if "alt_text_pdf" in st.session_state and st.session_state["alt_text_pdf"]:
                            with open(st.session_state["alt_text_pdf"], "rb") as output_file:
                                st.download_button(
                                    label="📑 Download PDF with Alt Text",
                                    data=output_file,
                                    file_name="alt-text-output.pdf",
                                    mime="application/pdf",
                                    use_container_width=True
                                )
                    except Exception as e:
                        logger.error(f"Download preparation error: {e}")
                        st.error("Failed to prepare download. Please try again.")

        except Exception as e:
            logger.error(f"Main process error: {e}")
            st.error(f"An error occurred: {str(e)}")
    else:
        st.info("👆 Please upload a PDF file to begin")

if __name__ == "__main__":
    main()