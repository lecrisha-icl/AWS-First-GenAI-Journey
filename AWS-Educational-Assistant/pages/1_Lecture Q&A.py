import streamlit as st
import Libs as glib
from PyPDF2 import PdfReader

def initialize_session_state():
    """Initialize session state variables"""
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'current_doc' not in st.session_state:
        st.session_state.current_doc = None

def apply_custom_css():
    """Apply custom CSS styling"""
    st.markdown("""
        <style>
            /* Main container styling */
            .main {
                background-color: #f8f9fa;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            
            /* Header styling */
            .header {
                background: linear-gradient(90deg, #6A9CFD, #7BB2FF);
                color: white;
                padding: 2rem;
                border-radius: 10px;
                text-align: center;
                margin-bottom: 2rem;
            }
            
            .header h1 {
                font-size: 2.5rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
            }
            
            .header p {
                font-size: 1.2rem;
                opacity: 0.9;
            }
            
            /* Card styling */
            .card {
                background: white;
                padding: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
                margin-bottom: 1rem;
            }
            
            /* Input styling */
            .stTextInput > div > div > input {
                background-color: white;
                padding: 0.75rem;
                border: 2px solid #e9ecef;
                border-radius: 8px;
                font-size: 1rem;
            }
            
            /* Button styling */
            .stButton > button {
                background: linear-gradient(90deg, #6A9CFD, #7BB2FF);
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                font-weight: 600;
                transition: transform 0.2s;
            }
            
            .stButton > button:hover {
                transform: translateY(-2px);
            }
            
            /* File uploader styling */
            .uploadedFile {
                border: 2px dashed #6A9CFD;
                border-radius: 8px;
                padding: 1rem;
                text-align: center;
            }
            
            /* Chat message styling */
            .chat-message {
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 0.5rem;
            }
            
            .user-message {
                background-color: #e9ecef;
                margin-left: 2rem;
            }
            
            .bot-message {
                background-color: #f8f9fa;
                margin-right: 2rem;
                border-left: 4px solid #6A9CFD;
            }
            
            /* Footer styling */
            .footer {
                text-align: center;
                padding: 1rem;
                color: #6c757d;
                font-size: 0.9rem;
            }
        </style>
    """, unsafe_allow_html=True)

def main():
    # Initialize session state
    initialize_session_state()
    
    # Page configuration
    st.set_page_config(
        page_title="Education Document Q&A",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Header section
    st.markdown("""
        <div class="header">
            <h1>📚 Education Document Q&A</h1>
            <p>Upload your educational document and get instant answers to your questions!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload Your PDF Document",
            type="pdf",
            help="Please upload a PDF document to begin asking questions."
        )
        
        if uploaded_file:
            st.success("✅ Document uploaded successfully!")
            # Process the document
            if uploaded_file != st.session_state.current_doc:
                with st.spinner("Processing document..."):
                    reader = PdfReader(uploaded_file)
                    docs = [page.extract_text() for page in reader.pages]
                    st.session_state.current_doc = uploaded_file
                    st.session_state.docs = docs
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quick action buttons
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Quick Actions")
        quick_questions = {
            "📝 Summarize": "Summarize the document",
            "🎯 Main Points": "What are the main points of the document?",
            "🔑 Key Concepts": "Explain the key concepts discussed"
        }
        
        for label, question in quick_questions.items():
            if st.button(label):
                st.session_state.current_question = question
                
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Ask Your Question")
        input_text = st.text_input(
            "",
            value=getattr(st.session_state, 'current_question', ''),
            placeholder="Type your question here...",
            key="question_input"
        )
        
        if st.button("Submit Question", use_container_width=True):
            if not uploaded_file:
                st.error("Please upload a document first!")
            elif not input_text:
                st.warning("Please enter a question!")
            else:
                with st.spinner('Finding the answer...'):
                    response = glib.query_document(input_text, st.session_state.docs)
                    st.session_state.history.append({
                        "question": input_text,
                        "answer": response
                    })
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display chat history
        if st.session_state.history:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Conversation History")
            for item in st.session_state.history:
                st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>Question:</strong> {item["question"]}
                    </div>
                    <div class="chat-message bot-message">
                        <strong>Answer:</strong> {item["answer"]}
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div class="footer">
            <p>Developed with ❤️ by AWS Vietnam team</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()