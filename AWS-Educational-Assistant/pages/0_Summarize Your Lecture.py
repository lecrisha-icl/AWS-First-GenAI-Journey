import streamlit as st
from PyPDF2 import PdfReader
import Libs as glib

# Page configuration
st.set_page_config(
    page_title="PDF Summarizer Pro",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with enhanced styling
st.markdown("""
    <style>
        /* Main container */
        .main {
            padding: 2rem;
        }
        
        /* Header styles */
        .header {
            background: linear-gradient(90deg, #6A9CFD 0%, #FFB8D0 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .title {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            color: white;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .subtitle {
            font-size: 1.2rem;
            text-align: center;
            color: white;
            opacity: 0.9;
        }
        
        /* Upload section */
        .upload-container {
            background: #FFFFFF;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            margin-bottom: 2rem;
        }
        
        .upload-box {
            border: 2px dashed #6A9CFD;
            border-radius: 10px;
            padding: 3rem;
            text-align: center;
            background: #F8FAFF;
            transition: all 0.3s ease;
        }
        
        .upload-box:hover {
            border-color: #FFB8D0;
            background: #FFF5F8;
        }
        
        /* Summary output */
        .summary-container {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .summary-header {
            font-size: 1.5rem;
            font-weight: 600;
            color: #6A9CFD;
            margin-bottom: 1rem;
        }
        
        .summary-content {
            background: #F8FAFF;
            padding: 1.5rem;
            border-radius: 8px;
            font-size: 1.1rem;
            line-height: 1.6;
            color: #2C3E50;
        }
        
        /* Progress bar */
        .stProgress > div > div > div > div {
            background-color: #6A9CFD;
        }
        
        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #6A9CFD 0%, #FFB8D0 100%);
            color: white;
            border: none;
            padding: 0.75rem 2rem;
            border-radius: 25px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(106, 156, 253, 0.3);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            color: #6A9CFD;
            font-size: 0.9rem;
        }
        
        /* Alerts and messages */
        .stAlert {
            border-radius: 8px;
            padding: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
    <div class="header">
        <h1 class="title">PDF Summarizer Pro</h1>
        <p class="subtitle">Transform your documents into concise, intelligent summaries</p>
    </div>
""", unsafe_allow_html=True)

# Main content
with st.container():
    # Left column for upload and controls
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="upload-container">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload your PDF document",
            type="pdf",
            help="Supported format: PDF files up to 200MB"
        )
        
        if uploaded_file:
            file_details = {
                "Filename": uploaded_file.name,
                "File size": f"{uploaded_file.size / 1024 / 1024:.2f} MB"
            }
            st.json(file_details)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: #F8FAFF; padding: 1.5rem; border-radius: 10px;">
                <h3 style="color: #6A9CFD;">Features</h3>
                <ul style="color: #2C3E50;">
                    <li>Quick and accurate summarization</li>
                    <li>Support for lengthy documents</li>
                    <li>AI-powered analysis</li>
                    <li>Export options available</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# Process the uploaded file
if uploaded_file is not None:
    try:
        with st.spinner('Processing your document...'):
            # Progress bar
            progress_bar = st.progress(0)
            
            # Read PDF
            reader = PdfReader(uploaded_file)
            docs = []
            
            # Process pages with progress bar
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    docs.append(text)
                progress_bar.progress((i + 1) / len(reader.pages))
            
            st.success(f"Successfully processed {len(docs)} pages")
        
        # Generate summary
        with st.spinner('Generating summary...'):
            st.markdown('<div class="summary-container">', unsafe_allow_html=True)
            st.markdown('<h2 class="summary-header">Document Summary</h2>', unsafe_allow_html=True)
            
            summary = ""
            for chunk in glib.summary_stream(docs):
                if chunk:
                    summary += chunk + " "
            
            st.markdown(f'<div class="summary-content">{summary}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Export options
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )
    
    except Exception as e:
        st.error(f"Error processing the PDF: {str(e)}")
        st.markdown("""
            <div style="background: #FFF5F5; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                <h4 style="color: #FF5757;">Troubleshooting Tips:</h4>
                <ul>
                    <li>Ensure the PDF is not password protected</li>
                    <li>Check if the file is corrupted</li>
                    <li>Try reducing the file size if it's too large</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("👆 Upload a PDF document to get started")

# Footer
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ using Streamlit and AI</p>
        <p style="font-size: 0.8rem; color: #6A9CFD80;">Version 1.0.0</p>
    </div>
""", unsafe_allow_html=True)