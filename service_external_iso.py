import streamlit as st

def get_desc():
    return "Guidance and representation through external ISO audits and certification processes."

def render(svc_name):
    st.subheader(svc_name)
    st.write(f"**Description:** {get_desc()}")
    st.write("**Estimated Price:** £1,500 - £3,000 / project")
    
    if st.button("Get Quote", key=f"quote_{svc_name}"):
        st.session_state.quote_subject = svc_name
        st.session_state.page = "Contact Us"
        st.rerun()