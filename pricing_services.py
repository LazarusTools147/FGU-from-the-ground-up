import streamlit as st
import service_site_management
import service_hs_management
import service_hs_consultancy
import service_internal_iso
import service_external_iso
import service_site_audits
import service_internal_audits

def render():
    st.title("Pricing & Services")
    
    search_term = st.text_input("Search Services...", "")
    
    services_map = {
        "Site Management Coverage": service_site_management,
        "H&S Management Coverage": service_hs_management,
        "H&S Consultancy Services": service_hs_consultancy,
        "Internal ISO Compliance": service_internal_iso,
        "External ISO Compliance": service_external_iso,
        "Site Safety Audits": service_site_audits,
        "Internal Safety Audits": service_internal_audits
    }
    
    # Filter based on search term in the name or description
    filtered_services = {}
    for name, module in services_map.items():
        if search_term.lower() in name.lower() or search_term.lower() in module.get_desc().lower():
            filtered_services[name] = module
            
    if not filtered_services:
        st.warning("No services found matching your search.")
    else:
        tabs = st.tabs(list(filtered_services.keys()))
        
        for idx, (name, module) in enumerate(filtered_services.items()):
            with tabs[idx]:
                module.render(name)