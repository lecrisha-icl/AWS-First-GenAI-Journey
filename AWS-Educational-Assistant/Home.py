import streamlit as st
import Libs as glib

# Configure the Streamlit page with additional settings
st.set_page_config(
    page_title="AWS Educational Assistant",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://aws.amazon.com/documentation/',
        'Report a bug': "mailto:support@example.com",
        'About': "AWS Educational Assistant - Developed by AWS Vietnam Team"
    }
)

# Enhanced CSS with animations and better visual hierarchy
st.markdown("""
<style>
    /* Global Styles */
    .main {
        background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
        font-family: 'Arial', sans-serif;
        padding: 2rem;
    }
    
    /* Header Styles */
    .title {
        font-size: 3.5em;
        background: linear-gradient(45deg, #232F3E, #FF9900);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        animation: fadeIn 1s ease-in;
    }
    
    .description {
        text-align: center;
        font-size: 1.3em;
        color: #444;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Chat Interface Styles */
    .stTextInput {
        border-radius: 10px;
        border: 2px solid #ddd;
        padding: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput:focus {
        border-color: #FF9900;
        box-shadow: 0 0 10px rgba(255, 153, 0, 0.2);
    }
    
    .st-chat-message {
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        animation: slideIn 0.3s ease-out;
    }
    
    .st-chat-message.user {
        background-color: #e9f5ff;
        border-left: 4px solid #232F3E;
    }
    
    .st-chat-message.bot {
        background-color: #fff8e6;
        border-right: 4px solid #FF9900;
    }
    
    /* Example Section Styles */
    .examples {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    .examples h3 {
        color: #232F3E;
        margin-bottom: 1rem;
    }
    
    .examples ul {
        list-style-type: none;
        padding: 0;
    }
    
    .examples li {
        margin: 0.8rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
        border-left: 3px solid #FF9900;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .examples li:hover {
        transform: translateX(5px);
        background: #fff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Footer Styles */
    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #666;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #ddd;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideIn {
        from { transform: translateY(10px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Page Header
st.markdown('<div class="title">AWS Educational Assistant</div>', unsafe_allow_html=True)
st.markdown('''
    <div class="description">
        Your intelligent companion for learning AWS services and best practices.
        Get instant answers to your AWS-related questions!
    </div>
''', unsafe_allow_html=True)

# Example questions with enhanced interactivity
example_questions = [
    "What is AWS Lambda, and how does it work?",
    "Can you explain the benefits of using Amazon S3?",
    "How to set up a VPC in AWS?",
    "What are the best practices for securing AWS environments?",
    "Explain AWS IAM roles and policies",
    "How does Amazon RDS handle database backups?"
]

st.markdown("""
<div class="examples">
    <h3>📚 Example Questions</h3>
    <p>Click on any example to get started:</p>
</div>
""", unsafe_allow_html=True)

# Create clickable examples
cols = st.columns(2)
for i, question in enumerate(example_questions):
    with cols[i % 2]:
        if st.button(question, key=f"example_{i}"):
            st.session_state.input_text = question

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input with improved UI
input_text = st.text_input(
    "Ask your AWS question here:",
    value=st.session_state.get('input_text', ''),
    placeholder="Type your question and press Enter...",
    key="main_input"
)

# Process user input and display response
if input_text:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": input_text})
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Generate and display bot response
    with st.spinner("Thinking..."):
        response_placeholder = st.empty()
        response = ""
        
        # Stream the response
        response_stream = glib.call_claude_sonet_stream(input_text)
        for chunk in response_stream:
            if chunk:
                response += chunk
                response_placeholder.markdown(f"{response}")
        
        # Add bot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})

# Footer
st.markdown("""
<div class="footer">
    <p>Developed with ❤️ by AWS Vietnam Team</p>
    <p>For support, please contact: KhaVan</p>
</div>
""", unsafe_allow_html=True)