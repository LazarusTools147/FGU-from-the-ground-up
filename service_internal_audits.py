import streamlit as st

def get_desc():
    return "Thorough review of internal safety documentation, policies, and procedures."

def render(svc_name):
    st.subheader(svc_name)
    st.write(f"**Description:** {get_desc()}")
    st.write("**Estimated Price:** £400 - £700 / audit")
    
    if st.button("Get Quote", key=f"quote_{svc_name}"):
        st.session_state.quote_subject = svc_name
        st.session_state.page = "Contact Us"
        st.rerun()