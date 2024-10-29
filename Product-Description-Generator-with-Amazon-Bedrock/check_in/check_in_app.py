import streamlit as st
import check_in_lib as glib
import sys
import json
from PIL import Image
sys.path.append("../Libs")
import Libs as lib 

def display_environment_metrics(env_data):
    cols = st.columns(4)
    metrics = {
        "☀️ Lighting": env_data.get("lighting", "N/A"),
        "📐 Space Size": env_data.get("space_size", "N/A"),
        "👥 Occupancy": env_data.get("occupancy", "N/A"),
        "✨ Cleanliness": env_data.get("cleanliness", "N/A")
    }
    for col, (label, value) in zip(cols, metrics.items()):
        col.metric(label, value)

def display_safety_compliance(safety_data):
    cols = st.columns(3)
    metrics = {
        "🚪 Emergency Exits": safety_data.get("emergency_exits", "N/A"),
        "🧯 Safety Equipment": safety_data.get("safety_equipment", "N/A"),
        "♿ Accessibility": safety_data.get("accessibility", "N/A")
    }
    for col, (label, value) in zip(cols, metrics.items()):
        col.metric(label, value)

def display_analysis_quality(quality_data):
    cols = st.columns(3)
    metrics = {
        "📷 Image Clarity": quality_data.get("image_clarity", "N/A"),
        "👁️ Feature Visibility": quality_data.get("visibility_of_features", "N/A"),
        "✅ Analysis Confidence": quality_data.get("analysis_confidence", "N/A")
    }
    for col, (label, value) in zip(cols, metrics.items()):
        col.metric(label, value)

def check_in():
    # Custom styling
    st.markdown("""
        <style>
        .stMetricValue {
            font-size: 1.2rem !important;
        }
        .feature-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1rem 0;
        }
        .feature-tag {
            background-color: #f0f2f5;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.9rem;
            display: inline-block;
        }
        .location-header {
            background: linear-gradient(90deg, #1E88E5 0%, #1565C0 100%);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .metrics-container {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        .section-header {
            background-color: #e3f2fd;
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
        <div class="location-header">
            <h1>🏢 Location Analysis System</h1>
            <p>Advanced environment classification and analysis</p>
        </div>
    """, unsafe_allow_html=True)

    # Main layout
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("### 📸 Image Upload")
        uploaded_file = st.file_uploader(
            "Upload location image",
            type=['png', 'jpg', 'jpeg'],
            help="Upload a clear image of the location for analysis"
        )

        if uploaded_file:
            try:
                uploaded_image_preview = lib.get_bytesio_from_bytes(uploaded_file.getvalue())
                st.image(uploaded_image_preview, use_column_width=True)
                
                image = Image.open(uploaded_file)
                with st.expander("📊 Image Details"):
                    st.json({
                        "Filename": uploaded_file.name,
                        "Size": f"{uploaded_file.size / 1024:.1f} KB",
                        "Dimensions": f"{image.size[0]}x{image.size[1]} px"
                    })
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")

    with col2:
        st.markdown("### 🔍 Analysis Dashboard")
        
        analyze_button = st.button(
            "🔍 Analyze Location",
            type="primary",
            disabled=not uploaded_file,
            use_container_width=True
        )

        if analyze_button and uploaded_file:
            with st.spinner("🔄 Performing detailed analysis..."):
                try:
                    image_bytes = uploaded_file.getvalue()
                    response_stream = glib.get_response_from_model(image_bytes=image_bytes)
                    
                    full_response = ""
                    for chunk in response_stream:
                        full_response += chunk if chunk else ""
                    
                    try:
                        result = json.loads(full_response)
                        
                        # Main Classification
                        st.markdown(f"""
                            <div class="section-header">
                                <h2>📍 Classification: {result['location_type'].upper()}</h2>
                                <p>{result['primary_purpose']}</p>
                            </div>
                        """, unsafe_allow_html=True)

                        # Environment Metrics
                        st.markdown("### 🌟 Environment Assessment")
                        display_environment_metrics(result['environment'])

                        # Key Features
                        st.markdown("### 🔑 Key Features")
                        features_html = "".join([f'<span class="feature-tag">🔹 {feature}</span>' for feature in result['key_features']])
                        st.markdown(f'<div class="feature-container">{features_html}</div>', unsafe_allow_html=True)

                        # Business Indicators
                        if result.get('business_indicators'):
                            st.markdown("### 💼 Business Indicators")
                            indicators_html = "".join([f'<span class="feature-tag">📊 {indicator}</span>' for indicator in result['business_indicators']])
                            st.markdown(f'<div class="feature-container">{indicators_html}</div>', unsafe_allow_html=True)

                        # Safety Compliance
                        st.markdown("### 🛡️ Safety & Compliance")
                        display_safety_compliance(result['safety_compliance'])

                        # Analysis Quality
                        st.markdown("### 📊 Analysis Quality")
                        display_analysis_quality(result['analysis_quality'])

                        # Detailed Explanation
                        with st.expander("📝 Detailed Analysis"):
                            st.markdown(result['explain'])

                        # Download Results
                        st.download_button(
                            "📥 Download Full Analysis",
                            data=json.dumps(result, indent=2, ensure_ascii=False),
                            file_name="location_analysis.json",
                            mime="application/json",
                            help="Download the complete analysis report in JSON format"
                        )
                        
                    except json.JSONDecodeError:
                        st.error("Error parsing analysis results. Please try again.")
                        
                except Exception as e:
                    st.error(f"Analysis error: {str(e)}")
                    st.button("🔄 Retry Analysis")

        # Help section
        with st.expander("ℹ️ Analysis Guide"):
            st.markdown("""
                ### 📋 What We Analyze

                #### 🏢 Location Categories
                - **Office Spaces**: Professional work environments
                - **Restaurants/Bars**: Dining and entertainment venues
                - **Retail Stores**: Commercial shopping spaces
                - **Other Locations**: Public and miscellaneous spaces

                #### 🔍 Analysis Components
                1. **Environmental Assessment**
                   - Lighting conditions
                   - Space utilization
                   - Occupancy levels
                   - Cleanliness standards

                2. **Safety & Compliance**
                   - Emergency exit visibility
                   - Safety equipment presence
                   - Accessibility features

                3. **Business Indicators**
                   - Commercial signage
                   - Brand presence
                   - Service facilities
                   - Professional equipment

                ### 📸 Tips for Best Results
                - Use well-lit, clear images
                - Capture wide angles of the space
                - Ensure key features are visible
                - Include identifying elements
            """)

if __name__ == "__main__":
    check_in()