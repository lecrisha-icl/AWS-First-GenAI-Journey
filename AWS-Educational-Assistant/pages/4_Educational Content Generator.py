import streamlit as st
import Libs as glib

# Page configuration with custom theme
st.set_page_config(
    page_title="Educational Content Generator",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.education.com/',
        'Report a bug': 'https://github.com/your-repo',
        'About': 'Educational Content Generator v1.0'
    }
)

# Enhanced CSS with modern design elements
st.markdown("""
    <style>
    /* Main container styles */
    .main {
        background-color: #FFFFFF;
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Header styles */
    .main h1 {
        color: #1E3A8A;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-align: center;
        padding-bottom: 1rem;
        border-bottom: 3px solid #3B82F6;
    }
    
    .main h2 {
        color: #2563EB;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    /* Input field styles */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #F3F4F6;
        border: 2px solid #E5E7EB;
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #3B82F6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
    }
    
    /* Select box styles */
    .stSelectbox > div > div > select {
        background-color: #F3F4F6;
        border: 2px solid #E5E7EB;
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 1rem;
        cursor: pointer;
    }
    
    /* Button styles */
    .stButton > button {
        width: 100%;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
        margin: 0.5rem 0;
    }
    
    .stButton > button:first-child {
        background-color: #2563EB;
        color: white;
    }
    
    .stButton > button:first-child:hover {
        background-color: #1D4ED8;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }
    
    .stButton > button:last-child {
        background-color: #EF4444;
        color: white;
    }
    
    .stButton > button:last-child:hover {
        background-color: #DC2626;
        box-shadow: 0 4px 6px rgba(239, 68, 68, 0.2);
    }
    
    /* Sidebar styles */
    .css-1d391kg {
        background-color: #F8FAFC;
        padding: 2rem 1rem;
    }
    
    .css-1d391kg .block-container {
        padding: 2rem 1rem;
    }
    
    /* Output container styles */
    .output-container {
        background-color: #F9FAFB;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid #E5E7EB;
    }
    
    /* Loading spinner styles */
    .stSpinner > div {
        border-color: #3B82F6;
    }
    
    /* Alert styles */
    .stAlert {
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Link styles */
    a {
        color: #2563EB;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    
    a:hover {
        color: #1D4ED8;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "clear_topic" not in st.session_state:
    st.session_state.clear_topic = ""
if "clear_subject" not in st.session_state:
    st.session_state.clear_subject = ""
if "clear_audience" not in st.session_state:
    st.session_state.clear_audience = "High School Students"
if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""

# Main content area
st.title("Educational Content Generator")
st.subheader("Create Professional Learning Materials in Seconds")

# Create two columns for the main content
left_col, right_col = st.columns([2, 1])

with left_col:
    # Input form
    with st.form(key="content_form"):
        input_topic = st.text_input(
            "Topic",
            value=st.session_state.clear_topic,
            placeholder="Enter the main topic for your lesson",
            help="Be specific about what you want to teach"
        )
        
        subject_area = st.text_input(
            "Subject Area",
            value=st.session_state.clear_subject,
            placeholder="E.g., Mathematics, Science, History",
            help="The broader subject category"
        )
        
        audience_level = st.selectbox(
            "Target Audience",
            ["High School Students", "College Students", "Professionals"],
            index=["High School Students", "College Students", "Professionals"].index(st.session_state.clear_audience),
            help="Select your target audience to adjust content complexity"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            submit_button = st.form_submit_button("Generate Content", use_container_width=True)
        with col2:
            clear_button = st.form_submit_button("Clear Form", use_container_width=True)

        if submit_button:
            if input_topic and subject_area and audience_level:
                with st.spinner("Creating your educational content..."):
                    prompt_template = f"""
                    As an expert educator in {subject_area}, create an engaging lesson on '{input_topic}' for {audience_level}.
                    Include:
                    
                    1. Introduction
                    2. Key Concepts
                    3. Practical Applications
                    4. Common Misconceptions
                    5. Summary
                    6. Further Reading
                    
                    Make the content engaging, accurate, and appropriate for the audience level.
                    """
                    
                    response_text = ""
                    for chunk in glib.call_claude_sonet_stream(prompt_template):
                        if chunk:
                            response_text += chunk
                    
                    st.session_state.generated_content = response_text
                    st.success("✨ Content generated successfully!")
            else:
                st.error("Please fill out all fields before generating content.")
                
        if clear_button:
            st.session_state.clear_topic = ""
            st.session_state.clear_subject = ""
            st.session_state.clear_audience = "High School Students"
            st.session_state.generated_content = ""
            st.experimental_rerun()

# Display generated content
if st.session_state.generated_content:
    st.markdown("### Generated Content")
    with st.container():
        st.markdown(st.session_state.generated_content)

# Sidebar content
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Educational Content Generator")
    
    st.markdown("### How to Use")
    st.info("""
    1. Enter your lesson topic
    2. Select the subject area
    3. Choose your target audience
    4. Click 'Generate Content'
    5. Review and customize the output
    """)
    
    st.markdown("### Tips for Best Results")
    st.success("""
    - Be specific with your topic
    - Consider your audience level
    - Review and adapt content as needed
    - Save generated content for future use
    """)
    
    st.markdown("### Additional Resources")
    resources = {
        "📚 Teaching Strategies": "https://www.edutopia.org/",
        "🎯 Lesson Planning": "https://www.lessonplans.com/",
        "📝 Educational Research": "https://www.education.com/"
    }
    
    for resource, link in resources.items():
        st.markdown(f"[{resource}]({link})")
    
    st.markdown("---")
    st.caption("© 2024 Educational Content Generator")