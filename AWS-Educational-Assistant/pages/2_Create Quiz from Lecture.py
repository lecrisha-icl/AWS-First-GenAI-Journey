import streamlit as st
from PyPDF2 import PdfReader
import Libs as glib

class QuizApp:
    def __init__(self):
        self.configure_page()
        self.apply_styling()
        self.initialize_session_state()
        
    def configure_page(self):
        st.set_page_config(
            page_title="AI Quiz Generator",
            page_icon="📚",
            layout="wide",
            initial_sidebar_state="expanded"
        )
    
    def apply_styling(self):
        st.markdown("""
            <style>
            /* Main Container Styling */
            .main {
                background-color: #f8f9fa;
                padding: 2rem;
            }
            
            /* Header Styling */
            .header-container {
                background: linear-gradient(135deg, #4285F4, #34A853);
                padding: 2rem;
                border-radius: 10px;
                margin-bottom: 2rem;
                text-align: center;
                color: white;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            
            /* Card Styling */
            .stCard {
                background-color: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
                margin-bottom: 1rem;
            }
            
            /* Button Styling */
            .stButton button {
                background: linear-gradient(135deg, #4285F4, #357AE8);
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 5px;
                font-weight: 500;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .stButton button:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            
            /* File Uploader Styling */
            .uploadedFile {
                border: 2px dashed #4285F4;
                border-radius: 10px;
                padding: 2rem;
                text-align: center;
                background-color: #f8f9fa;
            }
            
            /* Sidebar Styling */
            .css-1d391kg {
                background-color: #f1f3f4;
            }
            .sidebar-item {
                padding: 0.75rem 1rem;
                margin: 0.25rem 0;
                border-radius: 5px;
                transition: background-color 0.2s;
                cursor: pointer;
            }
            .sidebar-item:hover {
                background-color: #e8eaed;
            }
            
            /* Status Messages */
            .success-message {
                background-color: #34A853;
                color: white;
                padding: 1rem;
                border-radius: 5px;
                margin: 1rem 0;
            }
            .error-message {
                background-color: #EA4335;
                color: white;
                padding: 1rem;
                border-radius: 5px;
                margin: 1rem 0;
            }
            
            /* Questions Display */
            .question-container {
                background-color: white;
                padding: 1.5rem;
                border-radius: 8px;
                margin: 1rem 0;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            }
            
            /* Footer Styling */
            .footer {
                background-color: #f1f3f4;
                padding: 1rem;
                text-align: center;
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                font-size: 0.875rem;
                color: #5f6368;
            }
            
            /* Loading Animation */
            .loading {
                display: inline-block;
                width: 50px;
                height: 50px;
                border: 3px solid rgba(0,0,0,.3);
                border-radius: 50%;
                border-top-color: #4285F4;
                animation: spin 1s ease-in-out infinite;
            }
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            </style>
        """, unsafe_allow_html=True)
    
    def initialize_session_state(self):
        if 'generated_questions' not in st.session_state:
            st.session_state.generated_questions = None
            
    def render_sidebar(self):
        with st.sidebar:
            st.markdown("### Navigation")
            menu_items = {
                "📊 Dashboard": "View analytics and insights",
                "👥 Virtual Classrooms": "Manage your virtual classes",
                "📚 Courses": "Browse and manage courses",
                "📝 Quizzes": "Create and manage quizzes",
                "📊 Results": "View student results",
                "⚙️ Settings": "Configure your preferences"
            }
            
            for item, description in menu_items.items():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f"<div class='sidebar-item'>{item}</div>", unsafe_allow_html=True)
                
    def render_header(self):
        st.markdown("""
            <div class="header-container">
                <h1>📚 AI Quiz Generator</h1>
                <p>Transform your lecture materials into engaging multiple-choice questions</p>
            </div>
        """, unsafe_allow_html=True)
    
    def handle_file_upload(self):
        st.markdown("<div class='stCard'>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload your lecture material (PDF)",
            type="pdf",
            help="Select a PDF file containing your lecture content"
        )
        st.markdown("</div>", unsafe_allow_html=True)
        return uploaded_file
    
    def process_pdf(self, uploaded_file):
        try:
            reader = PdfReader(uploaded_file)
            docs = [page.extract_text() for page in reader.pages]
            
            with st.spinner("🤖 Generating questions..."):
                response = glib.create_questions(docs)
                response_text = ''.join([str(item) for item in response if item is not None])
                
            if response_text:
                st.markdown("""
                    <div class="success-message">
                        ✅ Questions generated successfully!
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<div class='question-container'>", unsafe_allow_html=True)
                formatted_response = response_text.replace('\n', '<br>')
                st.markdown(f"{formatted_response}", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📥 Download Questions"):
                        st.download_button(
                            "Download Questions as Text",
                            response_text,
                            file_name="generated_questions.txt",
                            mime="text/plain"
                        )
                with col2:
                    if st.button("🔄 Generate More Questions"):
                        st.experimental_rerun()
            else:
                st.markdown("""
                    <div class="error-message">
                        ❌ Failed to generate questions. Please try again with a different document.
                    </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    def render_footer(self):
        st.markdown("""
            <div class="footer">
                © 2024 AWS Quiz System | Made with ❤️ by Your Team
            </div>
        """, unsafe_allow_html=True)
    
    def run(self):
        self.render_sidebar()
        self.render_header()
        
        uploaded_file = self.handle_file_upload()
        
        if uploaded_file:
            self.process_pdf(uploaded_file)
        
        self.render_footer()

if __name__ == "__main__":
    app = QuizApp()
    app.run()