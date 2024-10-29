import streamlit as st
import content_moderation.content_moderation_lib as glib
import sys
sys.path.append("../Libs")
import Libs as lib
import json
from PIL import Image
import tempfile
from pathlib import Path

def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS format"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

def display_timestamps(timestamps, issues):
    """Display timestamps with corresponding issues"""
    if timestamps and issues:
        for time, issue in zip(timestamps, issues):
            st.markdown(f"🕒 **{format_timestamp(float(time))}**: {issue}")

def content_moderation():
    # Custom CSS
    st.markdown("""
        <style>
        .status-safe { background-color: #d4edda; border-color: #28a745; padding: 1rem; border-radius: 10px; }
        .status-flag { background-color: #fff3cd; border-color: #ffc107; padding: 1rem; border-radius: 10px; }
        .status-block { background-color: #f8d7da; border-color: #dc3545; padding: 1rem; border-radius: 10px; }
        .issue-tag { display: inline-block; padding: 0.3rem 0.8rem; border-radius: 15px; margin: 0.2rem; background-color: #f8f9fa; }
        .video-container { border: 1px solid #ddd; padding: 1rem; border-radius: 10px; margin: 1rem 0; }
        .timestamp-container { background-color: #f8f9fa; padding: 0.5rem; border-radius: 5px; margin: 0.5rem 0; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🛡️ Content Moderation")

    # Content type selector
    content_type = st.radio("Select content type:", ["Image", "Video"], horizontal=True)
    
    # File uploader based on content type
    allowed_types = ['mp4', 'mov', 'avi', 'mkv'] if content_type == "Video" else ['png', 'jpeg', 'jpg']
    uploaded_file = st.file_uploader(
        f"Upload {content_type.lower()} for moderation",
        type=allowed_types,
        help=f"Upload a {content_type.lower()} to check for prohibited content"
    )

    if uploaded_file:
        try:
            if content_type == "Image":
                # Display image
                image = Image.open(uploaded_file)
                uploaded_preview = lib.get_bytesio_from_bytes(uploaded_file.getvalue())
                st.image(uploaded_preview, use_column_width=True)
            else:
                # Display video
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    video_path = tmp_file.name
                
                st.markdown('<div class="video-container">', unsafe_allow_html=True)
                st.video(video_path)
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Analysis button
            if st.button("🔍 Analyze Content", type="primary", use_container_width=True):
                with st.spinner(f"Analyzing {content_type.lower()}..."):
                    try:
                        # Get moderation results
                        content_bytes = uploaded_file.getvalue()
                        response_stream = glib.get_response_from_model(
                            "", 
                            content_bytes,
                            content_type.lower()
                        )
                        
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
                                st.markdown("#### 🏴 Political Content:")
                                for issue in result["issues"]["political"]["type"]:
                                    st.markdown(f'<span class="issue-tag">🚫 {issue}</span>', unsafe_allow_html=True)
                                if content_type == "Video":
                                    st.markdown('<div class="timestamp-container">', unsafe_allow_html=True)
                                    display_timestamps(
                                        result["issues"]["political"]["timestamp"],
                                        result["issues"]["political"]["type"]
                                    )
                                    st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Adult content
                            if result["issues"]["adult_content"]["detected"]:
                                st.markdown("#### 🔞 Adult Content:")
                                for issue in result["issues"]["adult_content"]["type"]:
                                    st.markdown(f'<span class="issue-tag">🔞 {issue}</span>', unsafe_allow_html=True)
                                if content_type == "Video":
                                    st.markdown('<div class="timestamp-container">', unsafe_allow_html=True)
                                    display_timestamps(
                                        result["issues"]["adult_content"]["timestamp"],
                                        result["issues"]["adult_content"]["type"]
                                    )
                                    st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Other issues
                            if result["issues"]["other"]["detected"]:
                                st.markdown("#### ⚠️ Other Issues:")
                                for issue in result["issues"]["other"]["type"]:
                                    st.markdown(f'<span class="issue-tag">⚠️ {issue}</span>', unsafe_allow_html=True)
                                if content_type == "Video":
                                    st.markdown('<div class="timestamp-container">', unsafe_allow_html=True)
                                    display_timestamps(
                                        result["issues"]["other"]["timestamp"],
                                        result["issues"]["other"]["type"]
                                    )
                                    st.markdown('</div>', unsafe_allow_html=True)
                        
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
            st.error(f"Error loading {content_type.lower()}: {str(e)}")
        finally:
            if content_type == "Video" and 'video_path' in locals():
                Path(video_path).unlink(missing_ok=True)

    # Help section
    with st.expander("ℹ️ About Content Moderation"):
        st.markdown("""
            ### What We Check For:

            #### 🚫 Political Sensitivity
            - Yellow flag with three red stripes
            - Nine-dash line claims
            - Disputed territories
            - Political symbols and gestures

            #### 🔞 Adult Content
            - Explicit material
            - Age-restricted content
            - Inappropriate imagery or actions

            #### ⚠️ Other Issues
            - Violence or violent actions
            - Hate symbols
            - Harassment behavior
            - Dangerous activities
            
            ### Status Levels:
            - **SAFE**: Content is appropriate
            - **FLAG**: Needs review
            - **BLOCK**: Violates guidelines
            
            ### Video Analysis Features:
            - Frame-by-frame analysis
            - Audio content check
            - Timeline markers for issues
            - Scene transition analysis
        """)

if __name__ == "__main__":
    content_moderation()