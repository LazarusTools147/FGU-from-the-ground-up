import streamlit as st

def get_desc():
    return "Expert advice on health and safety protocols tailored specifically to your business needs."

def render(svc_name):
    st.subheader(svc_name)
    st.write(f"**Description:** {get_desc()}")
    st.write("**Estimated Price:** £75 - £150 / hour")
    
    if st.button("Get Quote", key=f"quote_{svc_name}"):
        st.session_state.quote_subject = svc_name
        st.session_state.page = "Contact Us"
        st.rerun()