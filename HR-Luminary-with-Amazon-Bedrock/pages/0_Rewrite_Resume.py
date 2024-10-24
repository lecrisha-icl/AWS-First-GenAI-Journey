import streamlit as st
import recruitment_lib as glib
from langchain.callbacks import StreamlitCallbackHandler
import time
from datetime import datetime
from typing import Dict, List
import json

class SessionState:
    """Handle session state management"""
    @staticmethod
    def initialize_state():
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'current_analysis' not in st.session_state:
            st.session_state.current_analysis = None

class UIConfig:
    """UI Configuration and Styling"""
    @staticmethod
    def setup_page():
        st.set_page_config(
            page_title="HR Gen AI Assistant",
            page_icon="👨‍💼",
            layout="wide",
            initial_sidebar_state="expanded"
        )

    @staticmethod
    def load_css():
        st.markdown("""
            <style>
                .main { background-color: #f8f9fa; padding: 2rem; }
                .stTextArea textarea {
                    border: 1px solid #dee2e6;
                    border-radius: 0.5rem;
                    padding: 1rem;
                    font-size: 1rem;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                }
                .stButton > button {
                    background-color: #0066cc;
                    color: white;
                    border: none;
                    border-radius: 0.5rem;
                    padding: 0.75rem 1.5rem;
                    font-size: 1rem;
                    font-weight: 500;
                    transition: all 0.3s ease;
                    width: 100%;
                }
                .stButton > button:hover {
                    background-color: #0052a3;
                    transform: translateY(-1px);
                }
                .card {
                    background-color: white;
                    padding: 1.5rem;
                    border-radius: 0.5rem;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    margin-bottom: 1rem;
                }
                .response-container {
                    background-color: #f8f9fa;
                    padding: 1.5rem;
                    border-radius: 0.5rem;
                    border-left: 4px solid #0066cc;
                    margin-top: 1rem;
                }
            </style>
        """, unsafe_allow_html=True)

class Sidebar:
    """Sidebar Component"""
    @staticmethod
    def render():
        with st.sidebar:
            st.image("https://via.placeholder.com/150", caption="HR GenAI Assistant")
            st.markdown("### Settings")
            
            settings = {
                'analysis_type': st.selectbox(
                    "Choose Analysis Type",
                    ["Resume Review", "Job Description Analysis", "Interview Question Generation"]
                ),
                'language': st.selectbox(
                    "Output Language",
                    ["English", "Spanish", "French", "German", "Chinese"]
                ),
                'detail_level': st.slider(
                    "Detail Level",
                    min_value=1,
                    max_value=5,
                    value=3,
                    help="Adjust the depth of analysis"
                )
            }
            return settings

class AnalysisTab:
    """Analysis Tab Component"""
    def __init__(self):
        self.callback = StreamlitCallbackHandler(st.container())

    def perform_analysis(self, input_text: str) -> str:
        try:
            return glib.rewrite_resume(input_text, self.callback)
        except Exception as e:
            st.error(f"Analysis Error: {str(e)}")
            return None

    def save_analysis(self, input_text: str, analysis_result: str):
        st.session_state.chat_history.append({
            "input": input_text,
            "output": analysis_result,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def render(self):
        st.markdown("""
            <div class="card">
                <h3>Resume Analysis Tool</h3>
                <p>Paste your resume below for AI-powered analysis and recommendations.</p>
            </div>
        """, unsafe_allow_html=True)

        input_text = st.text_area(
            "Resume Text",
            height=200,
            placeholder="Paste your resume or job description here..."
        )

        col1, col2, col3 = st.columns([1, 1, 1])
        
        analyze_button = col1.button("Analyze Content", use_container_width=True)
        clear_button = col2.button("Clear", use_container_width=True)
        save_button = col3.button("Save Analysis", use_container_width=True)

        if analyze_button and input_text:
            with st.spinner("Analyzing your content..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)

                analysis_result = self.perform_analysis(input_text)
                if analysis_result:
                    st.markdown("""
                        <div class="response-container">
                            <h4>Analysis Results</h4>
                            <div class="analysis-content">
                    """, unsafe_allow_html=True)
                    
                    st.markdown(analysis_result)
                    st.session_state.current_analysis = {
                        "input": input_text,
                        "output": analysis_result
                    }
                    st.success("Analysis completed successfully!")

        if save_button and st.session_state.current_analysis:
            self.save_analysis(
                st.session_state.current_analysis["input"],
                st.session_state.current_analysis["output"]
            )
            st.success("Analysis saved successfully!")

        if clear_button:
            st.session_state.current_analysis = None
            st.experimental_rerun()

class HistoryTab:
    """History Tab Component"""
    @staticmethod
    def render():
        if st.session_state.chat_history:
            for idx, item in enumerate(reversed(st.session_state.chat_history)):
                with st.expander(f"Analysis {len(st.session_state.chat_history) - idx} - {item['timestamp']}"):
                    st.text("Input:")
                    st.code(item['input'])
                    st.text("Analysis:")
                    st.markdown(item['output'])
        else:
            st.info("No analysis history available yet.")

class HelpTab:
    """Help Tab Component"""
    @staticmethod
    def render():
        st.markdown("""
            <div class="card">
                <h3>How to Use</h3>
                <ol>
                    <li>Choose the type of analysis from the sidebar</li>
                    <li>Paste your content in the text area</li>
                    <li>Adjust the detail level if needed</li>
                    <li>Click 'Analyze Content' to start</li>
                    <li>View results and save if needed</li>
                </ol>
                <p>For additional support, contact our team at support@example.com</p>
            </div>
        """, unsafe_allow_html=True)

def main():
    # Initialize session state
    SessionState.initialize_state()
    
    # Setup page configuration
    UIConfig.setup_page()
    UIConfig.load_css()
    
    # Render sidebar
    settings = Sidebar.render()
    
    # Main content
    st.title("🤖 HR GenAI Assistant")
    st.markdown("### AI-Powered Recruitment Solutions")
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Resume Analysis", "History", "Help"])
    
    with tab1:
        analysis_tab = AnalysisTab()
        analysis_tab.render()
    
    with tab2:
        history_tab = HistoryTab()
        history_tab.render()
    
    with tab3:
        help_tab = HelpTab()
        help_tab.render()
    
    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 1rem; color: #666;'>
            <p>Powered by AWS Bedrock and Amazon GenAI</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()