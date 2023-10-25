import streamlit as st
from ml_app import run_ml_app

def main():
    st.title("Main App")

    menu = ['Home','Machine Learning']

    choice = st.sidebar.selectbox("Home", menu)

    if choice == "Home":
        st.subheader("This is my Homepage")
    elif choice == "Machine Learning":
        run_ml_app()

if __name__ == '__main__':
    main()