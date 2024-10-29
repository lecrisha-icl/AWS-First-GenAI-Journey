import streamlit as st
import sys
sys.path.append("./check_uniform")
sys.path.append("./check_in")
sys.path.append("./product_description")
sys.path.append("./content_moderation")

# Set page config at the very beginning
st.set_page_config(
    page_title="AWS First GenAI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import after page config
from check_uniform_app import check_uniform 
from check_in_app import check_in 
from product_description_app import product_description 
from content_moderation_app import content_moderation 
from Main import main

# Enhanced Custom CSS with White Sidebar
st.markdown("""
    <style>
        /* Global Styles */
        [data-testid="stSidebar"] {
            background-color: white;
            padding-top: 2rem;
            border-right: 1px solid #eaeaef;
        }
        
        .main {
            padding: 2rem;
            background-color: #f8f9fa;
        }
        
        /* Header Styles */
        h1, h2, h3 {
            color: #232F3E;
            font-family: 'Amazon Ember', sans-serif;
            margin-bottom: 1rem;
        }
        
        /* Sidebar Styles */
        [data-testid="stSidebarNav"] {
            padding-top: 1rem;
            background-color: white;
        }
        
        .sidebar-text {
            color: #232F3E !important;
            font-family: 'Amazon Ember', sans-serif;
        }
        
        /* Button Styles */
        .stButton > button {
            background-color: #FF9900;
            color: #232F3E;
            border: none;
            border-radius: 4px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #EC7211;
            transform: translateY(-1px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        /* SelectBox Styles */
        .stSelectbox > div > div {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 0.5rem;
        }
        
        /* Card-like containers */
        .css-1r6slb0 {
            background-color: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 1rem;
        }
        
        /* Tool Selection Menu */
        [data-testid="stSelectbox"] {
            background-color: white;
            border: 1px solid #eaeaef;
            border-radius: 8px;
            padding: 0.5rem;
            margin-bottom: 1rem;
        }
        
        /* Info Box */
        .stInfo {
            background-color: #f8f9fa !important;
            color: #232F3E !important;
            border: 1px solid #eaeaef !important;
            border-radius: 8px;
        }
        
        /* Divider */
        hr {
            border-top: 1px solid #eaeaef;
            margin: 1rem 0;
        }
        
        /* Tool Description */
        .tool-description {
            color: #666;
            font-size: 0.9em;
            margin-top: 0.5rem;
        }
        
        /* Quick Action Buttons */
        .quick-action {
            margin: 0.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with white background
with st.sidebar:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg", width=50)
    with col2:
        st.markdown("<h2 style='color: #232F3E; margin-top: 10px;'>First GenAI</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tools menu with enhanced icons and descriptions
    tools = {
        "🏠 Home": {
            "function": main,
            "description": "Dashboard & Overview"
        },
        "👕 Check Uniform": {
            "function": check_uniform,
            "description": "Uniform Compliance Analysis"
        },
        "✅ Check In": {
            "function": check_in,
            "description": "Automated Check-in Process"
        },
        "📝 Product Description": {
            "function": product_description,
            "description": "AI-Powered Content Generation"
        },
        "⚖️ Content Moderation": {
            "function": content_moderation,
            "description": "Smart Content Filtering"
        }
    }
    
    selected_tool = st.selectbox(
        "Select Tool",
        tools.keys(),
        format_func=lambda x: f"{x}",
        key="tool_selector"
    )
    
    # Show tool description
    st.markdown(
        f"<div class='tool-description'>{tools[selected_tool]['description']}</div>", 
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # About section
    st.markdown("<h3 style='color: #232F3E;'>About</h3>", unsafe_allow_html=True)
    st.info("""
        **AWS First GenAI Assistant**
        
        Powered by:
        • Amazon Bedrock
        • Claude 3.5
        • LangChain
        • Streamlit
        
        Built for enhanced productivity
    """)
    
    # Quick Actions
    st.markdown("<h3 style='color: #232F3E;'>Quick Actions</h3>", unsafe_allow_html=True)
    if st.button("🔄 New Session", use_container_width=True, key="new_session"):
        st.session_state.clear()
    if st.button("📚 View Docs", use_container_width=True, key="view_docs"):
        st.markdown("[Documentation](https://aws.amazon.com/bedrock/)", unsafe_allow_html=True)

# Main content area
try:
    tools[selected_tool]["function"]()
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("🔄 Retry")

# Enhanced footer
st.markdown("---")
footer_cols = st.columns([2, 2, 2, 1])
with footer_cols[0]:
    st.markdown("**📧 support@example.com**")
with footer_cols[1]:
    st.markdown("**[📚 Documentation](https://aws.amazon.com/bedrock/)**")
with footer_cols[2]:
    st.markdown("**[💬 Community](https://aws.amazon.com/)**")
with footer_cols[3]:
    st.markdown("**v1.0.0**")