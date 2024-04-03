import streamlit as st

def login_page():
    st.markdown(
        """
        <style>
            .login-frame {
                padding: 20px;
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: #f9f9f9;
                transition: box-shadow 0.3s;
            }
            .login-frame:hover {
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1);
            }
            .login-btn {
                display: block;
                margin: 20px auto;
                padding: 10px 20px;
                background-color:lightgreen;
                color: red;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
                text-decoration: none; /* Remove underline */
                text-align: center; /* Center text */
                width: fit-content; /* Adjust width */
            }
            .login-btn:hover {
                background-color: lightblue;
            }
        </style>
        <h1 style='text-align: center;'>Welcome to the Login Page</h1>

        """,
        unsafe_allow_html=True
    )
# Center-align the GIF image
    col1, col2, col3 = st.columns([1, 1, 1])  # Create columns with appropriate widths
    with col2:  # Place the image in the middle column
        st.image("images/login.gif", width=200)

    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")

    if st.button("Login", key="login_btn"):
        if username == "kalpana" and password == "12345":
            st.success("Login Successful! Redirecting to Visualization Page...")
            st.markdown(
                "<a href='http://localhost:8501/visualization' class='login-btn'>Go to Visualization Page</a>",
                unsafe_allow_html=True
            )
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    login_page()
