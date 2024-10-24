import streamlit as st
import recruitment_lib as glib
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain.callbacks import StreamlitCallbackHandler
import time

# Configuration and Settings
def initialize_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_resume' not in st.session_state:
        st.session_state.current_resume = None

def set_page_config():
    st.set_page_config(
        page_title="AI Resume Analyzer",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def load_custom_css():
    st.markdown("""
        <style>
        /* Modern color scheme */
        :root {
            --primary-color: #2E7D32;
            --secondary-color: #e8f5e9;
            --accent-color: #4CAF50;
            --text-color: #424242;
            --background-color: #ffffff;
        }

        /* Container styling */
        .stApp {
            background-color: var(--background-color);
        }

        /* Custom card container */
        .custom-card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Header styling */
        .main-header {
            color: var(--primary-color);
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 2rem;
            padding: 1rem;
            background: linear-gradient(120deg, var(--secondary-color), #ffffff);
            border-radius: 10px;
        }

        /* Chat message styling */
        .chat-message {
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 5px;
            animation: fadeIn 0.5s ease-in;
        }

        .user-message {
            background-color: var(--secondary-color);
            margin-left: 2rem;
        }

        .assistant-message {
            background-color: #f5f5f5;
            margin-right: 2rem;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* File uploader improvements */
        .upload-container {
            border: 2px dashed var(--accent-color);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            background-color: var(--secondary-color);
            transition: all 0.3s ease;
        }

        .upload-container:hover {
            border-color: var(--primary-color);
            background-color: #f0f7f0;
        }

        /* Button styling */
        .stButton > button {
            background-color: var(--accent-color);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            border: none;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: var(--primary-color);
            transform: translateY(-2px);
        }

        /* Loading animation */
        .loading-spinner {
            text-align: center;
            padding: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def display_header():
    st.markdown('<h1 class="main-header">🤖 AI Resume Analyzer</h1>', unsafe_allow_html=True)

def file_uploader_section():
    with st.container():
        st.markdown('<div class="upload-container">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"],
            help="Drag and drop or click to upload a PDF resume"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        return uploaded_file

def display_sample_questions():
    with st.expander("📝 Sample Questions", expanded=False):
        questions = [
            "What are the candidate's main technical skills?",
            "Summarize their work experience in the last 3 years",
            "What programming languages do they know?",
            "Evaluate their experience with cloud technologies",
            "Does this person have leadership experience?"
        ]
        for q in questions:
            st.markdown(f"- {q}")

def chat_interface():
    # Chat input
    with st.container():
        input_text = st.text_input(
            "Ask a question about the resume:",
            key="chat_input",
            placeholder="Type your question here..."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            submit_button = st.button("Submit", use_container_width=True)
        with col2:
            clear_button = st.button("Clear Chat", use_container_width=True)
            
        return input_text, submit_button, clear_button

def process_resume(uploaded_file):
    if uploaded_file != st.session_state.current_resume:
        with st.spinner("Processing resume..."):
            reader = PdfReader(uploaded_file)
            docs = []
            for page in reader.pages:
                docs.append(page.extract_text())
            st.session_state.current_resume = uploaded_file
            st.session_state.current_docs = docs
            st.success("Resume processed successfully!")
            return docs
    return st.session_state.current_docs

def display_chat_history():
    for i, (question, answer) in enumerate(st.session_state.chat_history):
        st.markdown(f'<div class="chat-message user-message">🤔 **You:** {question}</div>', 
                   unsafe_allow_html=True)
        st.markdown(f'<div class="chat-message assistant-message">🤖 **Assistant:** {answer}</div>', 
                   unsafe_allow_html=True)

def main():
    # Initialize
    initialize_session_state()
    set_page_config()
    load_custom_css()
    
    # Layout
    display_header()
    
    # Sidebar
    with st.sidebar:
        st.markdown("### About")
        st.markdown("""
        This AI-powered tool analyzes resumes and answers your questions about candidates.
        Upload a PDF resume and ask questions to get insights.
        """)
        st.divider()
        display_sample_questions()
    
    # Main content
    uploaded_file = file_uploader_section()
    
    if uploaded_file:
        docs = process_resume(uploaded_file)
        input_text, submit_button, clear_button = chat_interface()
        
        if clear_button:
            st.session_state.chat_history = []
            st.experimental_rerun()
        
        if submit_button and input_text:
            with st.spinner("Analyzing..."):
                st_callback = StreamlitCallbackHandler(st.container())
                response = glib.query_resume(input_text, docs, st_callback)
                st.session_state.chat_history.append((input_text, response))
        
        display_chat_history()
    
    else:
        st.info("👆 Please upload a resume to begin the analysis.")

if __name__ == "__main__":
    main()