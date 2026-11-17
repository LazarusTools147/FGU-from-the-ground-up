import streamlit as st
import intro_page
import pricing_services
import contact_us
import about_me

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation
st.sidebar.title("FGU Consultancy")
pages = ["Home", "Pricing & Services", "Contact Us", "About Me"]

# Render radio button matching session state
selected_page = st.sidebar.radio("Navigate", pages, index=pages.index(st.session_state.page))

# Update session state and rerun if navigation changes
if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

# Route to the correct page module
if st.session_state.page == "Home":
    intro_page.render()
elif st.session_state.page == "Pricing & Services":
    pricing_services.render()
elif st.session_state.page == "Contact Us":
    contact_us.render()
elif st.session_state.page == "About Me":
    about_me.render()