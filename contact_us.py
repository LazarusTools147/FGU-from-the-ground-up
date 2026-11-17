import streamlit as st

def render():
    st.title("Contact Us")
    st.write("Get in touch with FGU Consultancy for quotes and inquiries.")
    
    # Pre-fill subject if redirected from a Get Quote button
    default_subject = ""
    if 'quote_subject' in st.session_state:
        default_subject = f"Quote Request: {st.session_state.quote_subject}"
        
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject", value=default_subject)
        message = st.text_area("Message", "Please provide details about your project or required services...")
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thank you! Your message has been sent. We will be in touch shortly.")
            if 'quote_subject' in st.session_state:
                del st.session_state.quote_subject