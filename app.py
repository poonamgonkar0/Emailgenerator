import streamlit as st
from backend import email_generator

st.set_page_config(page_title = "Email_Generator",page_icon="letter.png")

st.title("Email_Generator")
st.subheader("Powered by Open AI")


purpose= st.text_input("Enter purpose of your email")
recipient= st.text_input("Enter recipient of your email")
tone=st.selectbox("select tone",["Formal","Casual","SemiFormal"])
button=st.button("Generate Email")

st.spinner("Generating Email.....")
if button :
    if purpose and recipient and tone :
        result=email_generator(purpose,recipient,tone)
        st.success("Generate Email successfull")
        st.text_area(result)
        
    else:
        st.warning()
