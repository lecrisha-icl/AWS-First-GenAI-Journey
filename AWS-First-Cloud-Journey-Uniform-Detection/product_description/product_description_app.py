import streamlit as st
import product_description_lib as glib
import sys
sys.path.append("../Libs")
import Libs as lib
import json
from PIL import Image

def display_json_section(data, section_name):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                st.markdown(f"**{key.replace('_', ' ').title()}:**")
                display_json_section(value, key)
            else:
                st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                st.markdown("---")
                display_json_section(item, section_name)
            else:
                st.markdown(f"- {item}")

def product_description():
    # Custom CSS
    st.markdown("""
        <style>
        .main-header {
            background: linear-gradient(to right, #1E88E5, #1565C0);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
        }
        .section-header {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        .result-container {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
            margin-top: 2rem;
        }
        .feature-tag {
            background-color: #e3f2fd;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            margin: 0.2rem;
            display: inline-block;
        }
        .stTextArea textarea {
            height: 200px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
        <div class="main-header">
            <h1>🎯 Product Description Generator</h1>
            <p>Generate compelling product descriptions with AI-powered market analysis</p>
        </div>
    """, unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("### 📸 Product Image")
        uploaded_file = st.file_uploader(
            "Upload product image",
            type=['png', 'jpeg', 'jpg'],
            help="Upload a clear image of your product"
        )

        if uploaded_file:
            try:
                image = Image.open(uploaded_file)
                uploaded_image_preview = lib.get_bytesio_from_bytes(uploaded_file.getvalue())
                st.image(uploaded_image_preview, use_column_width=True)
                
                with st.expander("📊 Image Details"):
                    st.json({
                        "Filename": uploaded_file.name,
                        "Size": f"{uploaded_file.size / 1024:.1f} KB",
                        "Dimensions": f"{image.size[0]}x{image.size[1]} px"
                    })
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")

        st.markdown("### 🎯 PRIZM Segmentation")
        prizm = st.text_area(
            "Update PRIZM segmentation data",
            value=lib.prizm,
            help="Enter your PRIZM segmentation data for targeted marketing"
        )

    with col2:
        st.markdown("### 📝 Description Generator")
        
        generate_button = st.button(
            "🚀 Generate Description",
            type="primary",
            disabled=not uploaded_file,
            help="Click to generate product description",
            use_container_width=True
        )

        if generate_button and uploaded_file:
            with st.spinner("🔄 Generating comprehensive product description..."):
                try:
                    image_bytes = uploaded_file.getvalue()
                    response_stream = glib.get_response_from_model(
                        prompt_content="",
                        image_bytes=image_bytes,
                        prizm=prizm
                    )
                    
                    # Process stream
                    full_response = ""
                    for chunk in response_stream:
                        if chunk:
                            full_response += chunk
                    
                    try:
                        result = json.loads(full_response)
                        
                        st.markdown("### 📊 Product Analysis Results")
                        
                        # Product Overview
                        st.markdown(f"""
                            <div class="section-header">
                                <h3>🏷️ {result['product_name']}</h3>
                                <p>{result['marketing_description']['short_description']}</p>
                            </div>
                        """, unsafe_allow_html=True)

                        # Target Segment
                        st.markdown("### 👥 Target Audience")
                        display_json_section(result['target_segment'], 'target_segment')

                        # Key Features
                        st.markdown("### ✨ Key Features")
                        for feature in result['key_features']:
                            st.markdown(f"""
                                <div class="feature-tag">
                                    <strong>{feature['feature']}</strong>: {feature['benefit']}
                                </div>
                            """, unsafe_allow_html=True)

                        # Technical Specs
                        with st.expander("🔧 Technical Specifications"):
                            display_json_section(result['technical_specs'], 'technical_specs')

                        # Marketing Description
                        with st.expander("📢 Marketing Description"):
                            display_json_section(result['marketing_description'], 'marketing_description')

                        # Pricing & Positioning
                        with st.expander("💰 Pricing & Market Positioning"):
                            display_json_section(result['pricing_positioning'], 'pricing_positioning')

                        # Download options
                        col1, col2 = st.columns(2)
                        with col1:
                            st.download_button(
                                "📥 Download Full Analysis",
                                data=json.dumps(result, indent=2, ensure_ascii=False),
                                file_name="product_analysis.json",
                                mime="application/json"
                            )
                        with col2:
                            st.download_button(
                                "📄 Download Description",
                                data=result['marketing_description']['detailed_description'],
                                file_name="product_description.txt",
                                mime="text/plain"
                            )

                    except json.JSONDecodeError as e:
                        st.error("Error parsing generated description. Please try again.")
                        
                except Exception as e:
                    st.error(f"Error generating description: {str(e)}")
                    st.button("🔄 Retry Generation")

        # Help section
        with st.expander("ℹ️ Usage Guide"):
            st.markdown("""
                ### How to Get the Best Results

                1. **Image Quality**
                   - Use high-resolution product images
                   - Include multiple angles if possible
                   - Ensure good lighting and clear detail
                
                2. **PRIZM Data**
                   - Include detailed demographic information
                   - Specify target market segments
                   - Add relevant lifestyle indicators
                
                3. **Description Generation**
                   - Review and verify technical specifications
                   - Customize marketing tone as needed
                   - Download and edit final copy as needed
                
                ### Features
                
                - Comprehensive product analysis
                - Target audience identification
                - Technical specification extraction
                - Marketing copy generation
                - Pricing strategy suggestions
                - Competitive positioning
            """)

if __name__ == "__main__":
    product_description()