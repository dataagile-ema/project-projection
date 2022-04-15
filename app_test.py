import streamlit as st
# write sub-title
#st.markdown("<h4 style='text-align: left; color: black;'>Estimat för en User Story</h4>", unsafe_allow_html=True)
st.subheader("hej")
col1, col2 = st.columns((0.5,0.5))

with col1:
    st.text_input("Min", "10", help="Min för en User Story", key="text")
with col2:
    st.text_input("Max", "50", help="Max för en User Story")


st.text_input("name3", "3")
st.text_input("namn4", "4")


# Add bottom chart
