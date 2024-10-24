import streamlit as st
import recruitment_lib as glib
from langchain.callbacks import StreamlitCallbackHandler
from typing import List, Dict, Union, Any
import time

def init_session_state():
    """Initialize session state variables"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'is_processing' not in st.session_state:
        st.session_state.is_processing = False

def create_message_container(message: str, role: str):
    """
    Create a chat message container with proper styling
    Args:
        message: The message content
        role: 'user' or 'assistant'
    """
    avatar = "👤" if role == "user" else "🤖"
    with st.chat_message(role, avatar=avatar):
        st.markdown(message)

def display_sample_questions():
    """Display sample questions in the sidebar"""
    with st.expander("📝 Sample Questions", expanded=True):
        questions = [
            "Write a CV for software developers with 5 years of experience in web development with ReactJS and .NET Core",
            "List 10 questions for React developers",
            "Top 10 questions for JavaScript",
            "Create a job description for a Senior Full Stack Developer",
            "What are the best practices for conducting technical interviews?"
        ]
        for q in questions:
            if st.button(q, key=f"sample_{hash(q)}", use_container_width=True):
                return q
    return None

def apply_custom_style():
    """Apply custom CSS styling"""
    st.markdown("""
        <style>
            .chat-message {
                padding: 1rem;
                margin: 0.5rem 0;
                border-radius: 0.5rem;
                animation: fadeIn 0.3s ease-in;
            }
            
            .main {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
            }
            
            .stButton button {
                background-color: #1e3a8a;
                color: white;
                border-radius: 8px;
                padding: 0.75rem 1.5rem;
                font-weight: 600;
                transition: all 0.3s ease;
            }
            
            .stButton button:hover {
                background-color: #1c3480;
                transform: translateY(-1px);
            }
            
            .stTextInput input {
                border: 2px solid #e5e7eb;
                border-radius: 8px;
                padding: 0.75rem;
            }
            
            .chat-container {
                margin-bottom: 70px;
            }
        </style>
    """, unsafe_allow_html=True)

def get_chat_response(user_input: str) -> str:
    """
    Get response from the chat model
    Args:
        user_input: The user's input text
    Returns:
        str: The model's response
    """
    try:
        st_callback = StreamlitCallbackHandler(st.container())
        response = glib.get_rag_chat_response(user_input, st_callback)
        
        # Handle different response types
        if isinstance(response, tuple):
            return str(response[-1])  # Get last element of tuple
        elif isinstance(response, dict):
            return str(response.get('output', response))
        else:
            return str(response)
            
    except Exception as e:
        st.error(f"Error getting response: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."

def main():
    # Initialize session state
    init_session_state()
    
    # Page configuration
    st.set_page_config(
        page_title="HR Gen AI Assistant",
        page_icon="🤖",
        layout="wide"
    )
    
    # Apply custom styling
    apply_custom_style()

    # Header
    st.title("🤖 HR Gen AI Assistant")
    st.markdown("Your AI-powered HR and recruitment companion")

    # Sidebar
    with st.sidebar:
        st.header("💡 Quick Actions")
        selected_question = display_sample_questions()
        
        st.markdown("---")
        st.markdown("### 📊 Chat Statistics")
        st.markdown(f"Messages: {len(st.session_state.chat_history)}")
        
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    # Main chat container
    chat_container = st.container()
    with chat_container:
        # Display chat history
        for message in st.session_state.chat_history:
            create_message_container(message['content'], message['role'])

    # Input area
    st.markdown("---")
    input_col1, input_col2 = st.columns([6, 1])
    
    with input_col1:
        user_input = st.text_input(
            "Ask me anything about HR and recruitment...",
            key="user_input",
            value=selected_question if selected_question else "",
            placeholder="Type your question here..."
        )

    with input_col2:
        submit_button = st.button("Send 📤", use_container_width=True)

    # Process input when submitted
    if (submit_button or selected_question) and (user_input or selected_question):
        if not st.session_state.is_processing:
            try:
                st.session_state.is_processing = True
                
                # Get user message
                user_message = user_input or selected_question
                
                # Add user message to chat history
                st.session_state.chat_history.append({
                    'role': 'user',
                    'content': user_message
                })
                
                # Get and process response
                with st.spinner("Thinking... 🤔"):
                    response = get_chat_response(user_message)
                
                # Add assistant response to chat history
                st.session_state.chat_history.append({
                    'role': 'assistant',
                    'content': response
                })
                
                # Rerun to update the display
                st.rerun()
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            finally:
                st.session_state.is_processing = False

if __name__ == "__main__":
    main()