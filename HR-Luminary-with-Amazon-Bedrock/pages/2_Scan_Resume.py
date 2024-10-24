import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
import recruitment_lib as glib
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain.callbacks import StreamlitCallbackHandler
import time

# Configure the page
st.set_page_config(
    page_title="HR GenAI Assistant",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

def local_css():
    """Apply custom CSS styling"""
    st.markdown("""
        <style>
            /* Main container styling */
            .main {
                padding: 2rem;
                max-width: 1200px;
                margin: 0 auto;
            }
            
            /* Card styling */
            .stCard {
                border-radius: 1rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 1.5rem;
                margin: 1rem 0;
                background-color: white;
            }
            
            /* Button styling */
            .stButton button {
                background-color: #7792E3;
                border-radius: 0.5rem;
                padding: 0.5rem 1rem;
                font-weight: 500;
                transition: all 0.3s ease;
            }
            .stButton button:hover {
                background-color: #5A73B3;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            
            /* File uploader styling */
            .uploadedFile {
                border: 2px dashed #7792E3;
                border-radius: 0.5rem;
                padding: 1rem;
                background-color: #f8f9fa;
            }
            
            /* Progress bar */
            .stProgress > div > div {
                background-color: #7792E3;
            }
            
            /* Typography */
            h1, h2, h3 {
                color: #1E3A8A;
                font-weight: 600;
            }
            
            /* Custom divider */
            .custom-divider {
                width: 100%;
                height: 2px;
                background: linear-gradient(90deg, #7792E3 0%, rgba(119, 146, 227, 0) 100%);
                margin: 1rem 0;
            }
        </style>
    """, unsafe_allow_html=True)

def show_header():
    """Display the application header"""
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        colored_header(
            label="HR GenAI Assistant",
            description="Powered by AWS and LangChain",
            color_name="blue-70"
        )

def show_sidebar():
    """Configure and display the sidebar"""
    with st.sidebar:
        st.markdown("### About")
        st.info("""
        This HR Assistant uses advanced AI to analyze resumes 
        and provide detailed insights. Upload your PDF resume 
        to get started.
        """)
        
        st.markdown("### Features")
        st.write("✓ Resume Analysis")
        st.write("✓ Key Skills Extraction")
        st.write("✓ Experience Summary")
        
        st.markdown("### Instructions")
        st.warning("""
        1. Upload a PDF resume
        2. Wait for processing
        3. Review the AI-generated analysis
        """)

def process_pdf(uploaded_file):
    """Process the uploaded PDF file and return extracted text"""
    docs = []
    with st.spinner("Reading PDF..."):
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            docs.append(page.extract_text())
    return docs

def display_results(response):
    """Display the analysis results in a structured format"""
    st.markdown("---")
    st.markdown("### 📋 Analysis Results")
    
    # Create tabs for different sections
    tab1, tab2 = st.tabs(["Summary", "Details"])
    
    with tab1:
        st.markdown(f"#### Key Points")
        st.write(response)
    
    with tab2:
        st.markdown("#### Full Analysis")
        st.json({
            "document_length": len(response),
            "analysis_timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "full_text": response
        })

def main():
    """Main application function"""
    local_css()
    show_header()
    show_sidebar()
    
    # Main content area
    st.markdown("### Upload Resume")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload your resume in PDF format",
        key="resume_uploader"
    )
    
    if uploaded_file:
        # File info display
        st.success(f"File '{uploaded_file.name}' successfully uploaded!")
        
        # Process the file
        docs = process_pdf(uploaded_file)
        
        # Create a callback handler for Streamlit
        with st.container():
            st_callback = StreamlitCallbackHandler(st.container())
            
            # Get and display the analysis
            with st.spinner("Analyzing resume..."):
                response = glib.summary_resume_stream(docs, st_callback)
                display_results(response)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: gray;'>Powered by AWS GenAI</p>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()