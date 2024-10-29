import streamlit as st
import content_moderation.content_moderation_lib as glib
import sys
sys.path.append("../Libs")
import Libs as lib
import json
from PIL import Image

def content_moderation():
    # Custom CSS
    st.markdown("""
        <style>
        .status-safe {
            background-color: #d4edda;
            border-color: #28a745;
            padding: 1rem;
            border-radius: 10px;
        }
        .status-flag {
            background-color: #fff3cd;
            border-color: #ffc107;
            padding: 1rem;
            border-radius: 10px;
        }
        .status-block {
            background-color: #f8d7da;
            border-color: #dc3545;
            padding: 1rem;
            border-radius: 10px;
        }
        .issue-tag {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            margin: 0.2rem;
            background-color: #f8f9fa;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🛡️ Content Moderation")

    # Image upload
    uploaded_file = st.file_uploader(
        "Upload image for moderation",
        type=['png', 'jpeg', 'jpg'],
        help="Upload an image to check for prohibited content"
    )

    if uploaded_file:
        try:
            # Display image
            image = Image.open(uploaded_file)
            uploaded_image_preview = lib.get_bytesio_from_bytes(uploaded_file.getvalue())
            st.image(uploaded_image_preview, use_column_width=True)
            
            # Analysis button
            if st.button("🔍 Analyze Content", type="primary", use_container_width=True):
                with st.spinner("Analyzing content..."):
                    try:
                        # Get moderation results
                        image_bytes = uploaded_file.getvalue()
                        response_stream = glib.get_response_from_model("", image_bytes)
                        
                        # Collect full response
                        full_response = ""
                        for chunk in response_stream:
                            if chunk:
                                full_response += chunk
                        
                        # Parse JSON response
                        result = json.loads(full_response)
                        
                        # Display results
                        status_class = {
                            "SAFE": "status-safe",
                            "FLAG": "status-flag",
                            "BLOCK": "status-block"
                        }.get(result["status"], "status-flag")
                        
                        st.markdown(f"""
                            <div class="{status_class}">
                                <h3>Status: {result["status"]}</h3>
                                <p>Confidence: {result["confidence"]}</p>
                                <p>Recommended Action: {result["action"]}</p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Display detected issues
                        if any(issue["detected"] for issue in result["issues"].values()):
                            st.markdown("### 🚨 Detected Issues")
                            
                            # Political issues
                            if result["issues"]["political"]["detected"]:
                                st.markdown("#### Political Content:")
                                for issue in result["issues"]["political"]["type"]:
                                    st.markdown(f'<span class="issue-tag">🚫 {issue}</span>', unsafe_allow_html=True)
                            
                            # Adult content
                            if result["issues"]["adult_content"]["detected"]:
                                st.markdown("#### Adult Content:")
                                for issue in result["issues"]["adult_content"]["type"]:
                                    st.markdown(f'<span class="issue-tag">🔞 {issue}</span>', unsafe_allow_html=True)
                            
                            # Other issues
                            if result["issues"]["other"]["detected"]:
                                st.markdown("#### Other Issues:")
                                for issue in result["issues"]["other"]["type"]:
                                    st.markdown(f'<span class="issue-tag">⚠️ {issue}</span>', unsafe_allow_html=True)
                        
                        # Explanation
                        st.markdown("### 📝 Analysis Explanation")
                        st.info(result["explanation"])
                        
                        # Download report
                        st.download_button(
                            "📥 Download Report",
                            data=json.dumps(result, indent=2),
                            file_name="moderation_report.json",
                            mime="application/json"
                        )
                        
                    except json.JSONDecodeError as e:
                        st.error(f"Error parsing results: {str(e)}")
                    except Exception as e:
                        st.error(f"Error during analysis: {str(e)}")
                        st.button("🔄 Retry")
                        
        except Exception as e:
            st.error(f"Error loading image: {str(e)}")

    # Help section
    with st.expander("ℹ️ About Content Moderation"):
        st.markdown("""
            ### What We Check For:

            #### 🚫 Political Sensitivity
            - Yellow flag with three red stripes
            - Nine-dash line claims
            - Disputed territories
            - Political symbols

            #### 🔞 Adult Content
            - Explicit material
            - Age-restricted content
            - Inappropriate imagery

            #### ⚠️ Other Issues
            - Violence
            - Hate symbols
            - Harassment
            
            ### Status Levels:
            - **SAFE**: Content is appropriate
            - **FLAG**: Needs review
            - **BLOCK**: Violates guidelines
        """)

if __name__ == "__main__":
    content_moderation()