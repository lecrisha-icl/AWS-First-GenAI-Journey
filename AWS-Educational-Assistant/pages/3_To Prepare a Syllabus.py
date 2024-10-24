import streamlit as st
import Libs as glib
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Syllabus Assistant Pro",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with modern design elements
st.markdown("""
    <style>
        /* Main container styling */
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }
        
        /* Typography */
        .title {
            color: #1f3d7a;
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .subtitle {
            color: #4a5568;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 400;
            margin-bottom: 2rem;
        }
        
        /* Card styling */
        .card {
            background-color: #f8fafc;
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            margin-bottom: 1rem;
        }
        
        /* Input area styling */
        .stTextArea textarea {
            border-radius: 8px;
            border: 2px solid #e2e8f0;
            padding: 1rem;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }
        
        .stTextArea textarea:focus {
            border-color: #4299e1;
            box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.2);
        }
        
        /* Button styling */
        .stButton > button {
            background-color: #1f3d7a;
            color: white;
            padding: 0.75rem 2rem;
            border-radius: 8px;
            border: none;
            font-weight: 600;
            transition: all 0.3s ease;
            width: 100%;
            max-width: 300px;
        }
        
        .stButton > button:hover {
            background-color: #2c5282;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        /* Success message styling */
        .success-message {
            background-color: #c6f6d5;
            color: #2f855a;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        /* Error message styling */
        .error-message {
            background-color: #fed7d7;
            color: #c53030;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        /* Footer styling */
        .footer {
            text-align: center;
            padding: 2rem 0;
            color: #718096;
            font-size: 0.875rem;
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background-color: #1f3d7a;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with additional information
with st.sidebar:
    st.markdown("### 📖 About")
    st.info("""
    The Syllabus Assistant Pro helps educators create and improve their course syllabi 
    using advanced analysis and best practices in educational design.
    """)
    
    st.markdown("### 🎯 Features")
    st.success("""
    - Content Analysis
    - Structure Recommendations
    - Best Practices Integration
    - Language Enhancement
    """)
    
    st.markdown("### 💡 Tips")
    st.warning("""
    - Be specific with course objectives
    - Include clear assessment criteria
    - Define expectations clearly
    - Add contact information
    """)

# Main content
st.markdown('<h1 class="title">📚 Syllabus Assistant Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Transform your syllabus with AI-powered insights and recommendations</p>', unsafe_allow_html=True)

# Create tabs for different sections
tab1, tab2 = st.tabs(["Create/Edit Syllabus", "View Guidelines"])

with tab1:
    # Input section with improved styling
    st.markdown('<div class="card">', unsafe_allow_html=True)
    input_text = st.text_area(
        "Enter your syllabus content below:",
        height=300,
        placeholder="Paste your syllabus content here...",
        help="You can paste your entire syllabus or specific sections you want to improve."
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Options and settings
    col1, col2 = st.columns(2)
    with col1:
        analysis_type = st.selectbox(
            "Select Analysis Type",
            ["Comprehensive Review", "Structure Analysis", "Language Enhancement", "Accessibility Check"]
        )
    with col2:
        focus_areas = st.multiselect(
            "Focus Areas",
            ["Course Objectives", "Assessment Methods", "Policies", "Schedule", "Resources"],
            default=["Course Objectives"]
        )
    
    # Process button with loading state
    if st.button("Analyze and Improve Syllabus", key="process_button"):
        if input_text:
            with st.spinner("🔄 Processing your syllabus..."):
                try:
                    # Create progress bar
                    progress_bar = st.progress(0)
                    for i in range(100):
                        # Update progress bar
                        progress_bar.progress(i + 1)
                    
                    # Get suggestions
                    response = glib.suggest_writing_document(input_text)
                    suggestions = ' '.join([part for part in response if part is not None])
                    
                    # Display results in an organized manner
                    st.markdown("### 📊 Analysis Results")
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown("#### Key Recommendations")
                    st.markdown(suggestions)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Add download button for results
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    st.download_button(
                        label="Download Analysis Report",
                        data=suggestions,
                        file_name=f"syllabus_analysis_{timestamp}.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.markdown(
                        f'<div class="error-message">❌ An error occurred: {str(e)}</div>',
                        unsafe_allow_html=True
                    )
        else:
            st.markdown(
                '<div class="error-message">⚠️ Please input your syllabus content to proceed.</div>',
                unsafe_allow_html=True
            )

with tab2:
    st.markdown("### 📋 Syllabus Best Practices")
    st.info("""
    A well-designed syllabus should include:
    1. Clear course objectives and learning outcomes
    2. Detailed assessment criteria and grading policies
    3. Course schedule with important dates
    4. Required materials and resources
    5. Contact information and office hours
    6. Academic integrity policies
    7. Accessibility statements
    """)

# Footer
st.markdown("---")
st.markdown(
    '<div class="footer">© 2024 Syllabus Assistant Pro | Designed to enhance educational excellence</div>',
    unsafe_allow_html=True
)