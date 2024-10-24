import streamlit as st
import recruitment_lib as glib
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain.callbacks import StreamlitCallbackHandler
import time
import pandas as pd

# Configuration and Setup
def initialize_page():
    st.set_page_config(
        page_title="HR Gen AI Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    apply_custom_styles()

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main container styles */
        .main {
            padding: 2rem;
        }
        
        /* Custom container for cards */
        .css-1r6slb0 {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* Header styles */
        .main-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Button styles */
        .stButton>button {
            background-color: #2E86C1;
            color: white;
            border: none;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #1A5276;
            transform: translateY(-2px);
        }
        
        /* File uploader styles */
        .stFileUploader {
            background-color: #f8f9fa;
            border: 2px dashed #ccc;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        
        /* Analysis result styles */
        .analysis-section {
            margin: 20px 0;
            padding: 15px;
            border-radius: 8px;
            background-color: #f8f9fa;
        }
        
        .result-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        
        /* Info message styles */
        .info-message {
            padding: 10px;
            border-radius: 8px;
            background-color: #e3f2fd;
            border-left: 5px solid #2196f3;
        }
        </style>
    """, unsafe_allow_html=True)

def display_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🤖 HR Gen AI Assistant")
        st.markdown("""
            <p style='text-align: center; color: #666; font-size: 1.1em;'>
                Powered by Amazon Bedrock & Claude 3.5
            </p>
        """, unsafe_allow_html=True)

def create_sidebar():
    with st.sidebar:
        st.header("📋 Instructions")
        st.markdown("""
        1. Upload your resume in PDF format
        2. Click 'Analyze Resume' to start
        3. View the detailed analysis and recommendations
        
        **Supported Features:**
        - Resume Analysis
        - Skill Assessment
        - Experience Evaluation
        """)
        
        st.markdown("---")
        st.markdown("### ⚙️ Settings")
        analysis_depth = st.select_slider(
            "Analysis Depth",
            options=["Quick", "Standard", "Detailed"],
            value="Standard"
        )
        return analysis_depth

def file_uploader_section():
    st.markdown("### 📄 Upload Resume")
    uploaded_file = st.file_uploader(
        "",
        type=["pdf"],
        help="Upload your resume in PDF format"
    )
    return uploaded_file

def action_buttons():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        analyze_button = st.button("🔍 Analyze Resume", use_container_width=True)
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    with col3:
        help_button = st.button("❓ Help", use_container_width=True)
    return analyze_button, clear_button, help_button

def show_loading_animation():
    with st.spinner("🔄 Analyzing your resume..."):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)

def parse_response(response):
    """Parse and validate the response from the agent."""
    try:
        # Check if response is a dictionary
        if not isinstance(response, dict):
            return None, str(response)

        # Extract output
        output = response.get('output', '')
        
        # Extract and validate intermediate steps
        intermediate_steps = response.get('intermediate_steps', [])
        
        # Create a structured analysis from the response
        analysis_data = {
            'output': output,
            'detailed_analysis': None
        }
        
        # Try to extract detailed analysis if available
        if intermediate_steps and len(intermediate_steps) > 1:
            if isinstance(intermediate_steps[1], tuple) and len(intermediate_steps[1]) > 1:
                analysis_data['detailed_analysis'] = intermediate_steps[1][1]
        
        return analysis_data, None
        
    except Exception as e:
        return None, f"Error parsing response: {str(e)}"

def display_analysis_results(response):
    analysis_data, error = parse_response(response)
    
    if error:
        st.error(f"⚠️ {error}")
        return
    
    st.success("✅ Analysis Complete!")
    
    # Display main analysis
    st.markdown("### 📊 Analysis Summary")
    
    # Display in a two-column layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="result-card">
            <h4>Key Points</h4>
            <ul>
                <li>Profile Overview</li>
                <li>Skills Assessment</li>
                <li>Experience Summary</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="result-card">
            <h4>Recommendations</h4>
            <ul>
                <li>Areas of Improvement</li>
                <li>Suggested Enhancements</li>
                <li>Next Steps</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Display detailed analysis if available
    if analysis_data['detailed_analysis'] is not None:
        with st.expander("🔍 Detailed Analysis", expanded=True):
            if isinstance(analysis_data['detailed_analysis'], pd.DataFrame):
                st.dataframe(analysis_data['detailed_analysis'])
            else:
                st.write(analysis_data['detailed_analysis'])
    
    # Display main output
    st.markdown("### 🎯 Key Findings")
    st.markdown("""
    <div class="analysis-section">
        {}
    </div>
    """.format(analysis_data['output']), unsafe_allow_html=True)

def process_pdf(uploaded_file):
    """Extract text from PDF file with error handling."""
    try:
        reader = PdfReader(uploaded_file)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return text, None
    except Exception as e:
        return None, f"Error processing PDF: {str(e)}"

def main():
    initialize_page()
    display_header()
    analysis_depth = create_sidebar()
    
    uploaded_file = file_uploader_section()
    analyze_button, clear_button, help_button = action_buttons()
    
    if help_button:
        st.info("📝 Upload a PDF resume and click on 'Analyze Resume' to get a detailed analysis of your resume.")
    
    if uploaded_file is not None and analyze_button:
        # Process PDF
        docs, error = process_pdf(uploaded_file)
        if error:
            st.error(error)
            return
            
        show_loading_animation()
        
        try:
            # Initialize agent and process
            agent = glib.initializeAgent()
            st_callback = StreamlitCallbackHandler(st.container())
            
            response = agent({
                "input": str(docs),
                "output": "output",
                "chat_history": [],
                "analysis_depth": analysis_depth
            }, callbacks=[st_callback])
            
            display_analysis_results(response)
            
        except Exception as e:
            st.error(f"⚠️ Analysis Error: {str(e)}")
            st.info("Please try again or contact support if the problem persists.")
        
    elif clear_button:
        st.cache_data.clear()
        st.experimental_rerun()
    
    if not uploaded_file:
        st.info("👆 Please upload a PDF file to begin the analysis.")

if __name__ == "__main__":
    main()