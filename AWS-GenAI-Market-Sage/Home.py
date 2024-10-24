import streamlit as st
import streamlit as st

pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon="🏠"),
    st.Page("pages/document_summary.py", title="Document Summary", icon="✍"),
    st.Page("pages/document_answer.py", title="Document Q&A", icon="🙋‍♀️"),
    st.Page("pages/stock_analytics.py", title="Stock Technical Analysis", icon="🧑‍💻"),
    st.Page("pages/stock_advisor.py", title="Stock Information Lookup", icon="🤠"),
    st.Page("pages/stock_agent.py", title="Stock Assistant", icon="👨‍🏫"),
])
pg.run()