import streamlit as st
a=st.number_input("Enter a number")
b=st.number_input("enter another number")
if st.button("Add"): 
    st.success(a+b)
elif st.button("Subtract"):
    st.success(a-b)
elif st.button("Multiply"):
    st.success(a*b)
elif st.button("Divide"):
    st.success(a/b)
