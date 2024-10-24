import streamlit as st 
import libs as glib 
from PyPDF2 import PdfReader
import base

# Set the page configuration
st.set_page_config(page_title="Document Q&A", page_icon="img/favicon.ico", layout="wide")

# Custom CSS styling
st.markdown(
    """
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stButton>button {
            background-color: #f63366;
            color: white;
            border-radius: 5px;
        }
        .custom-title {
            font-size: 2em;
            font-weight: bold;
            color: #f63366;
            margin-bottom: 20px;
        }
        .custom-box {
            background-color: #f1f3f6;
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="custom-title">Document Q&A</div>', unsafe_allow_html=True)

# Initialize the sidebar and animation
base.init_slidebar()
base.init_animation()

# PDF Upload Section
uploaded_file = st.file_uploader("Upload a PDF document to ask questions", type=["pdf"])

# Provide sample questions for users
st.markdown("### Ask questions about the document content, for example:")
st.markdown("- Summarize the document content") 
st.markdown("- Highlight the key points of the document")

# Text input for user's question
input_text = st.text_input("Your question!")

# Initialize document list
docs = []

# Handle PDF upload and question submission
if uploaded_file is not None:
    # Preview uploaded PDF file (first few pages)
    pdf_preview_expander = st.expander("Preview Document")
    with pdf_preview_expander:
        reader = PdfReader(uploaded_file)
        preview_text = ""
        for page_num, page in enumerate(reader.pages[:2]):  # Preview first 2 pages
            preview_text += f"**Page {page_num + 1}**: {page.extract_text()}\n\n"
        st.markdown(preview_text)

    # Process the document and respond to the user's question
    if input_text:
        for page in reader.pages:
            docs.append(page.extract_text())
        
        with st.spinner('Processing document, please wait...'):
            response = glib.query_document(input_text, docs)
        
        # Display the response in a styled box
        st.markdown('<div class="custom-box">', unsafe_allow_html=True)
        st.write(response)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer message
st.markdown("<p style='color:gray;text-align:center;'>Powered by AWS</p>", unsafe_allow_html=True)