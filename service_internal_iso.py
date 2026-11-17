import streamlit as st

def get_desc():
    return "Preparation, gap analysis, and compliance advice for internal ISO standards."

def render(svc_name):
    st.subheader(svc_name)
    st.write(f"**Description:** {get_desc()}")
    st.write("**Estimated Price:** £1,200 - £2,500 / project")
    
    if st.button("Get Quote", key=f"quote_{svc_name}"):
        st.session_state.quote_subject = svc_name
        st.session_state.page = "Contact Us"
        st.rerun()