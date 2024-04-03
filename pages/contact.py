import streamlit as st

def contact_page():
    st.title("Contact Us")

    st.markdown("Feel free to reach out to us with any questions, feedback, or inquiries. We're here to help!")

    st.header("Send us a Message")
    name = st.text_input("Your Name", max_chars=50)
    email = st.text_input("Your Email", max_chars=50)
    message = st.text_area("Message", height=200)

    if st.button("Send Message"):
        if name.strip() == "" or email.strip() == "" or message.strip() == "":
            st.error("Please fill out all fields.")
        else:
            # Code to send the message
            st.success("Message sent successfully!")

    st.header("Contact Information")
    st.markdown("You can also reach us via email or phone.")
    st.markdown("📧 Email: Transport_traffic@example.com")
    st.markdown("📞 Phone: +1234567890")

    st.header("Follow Us on Social Media")
    st.markdown("Stay connected with us on social media for updates, news, and more!")
    st.markdown("🐦 [Twitter](https://twitter.com/example)")
    st.markdown("📘 [Facebook](https://facebook.com/example)")
    st.markdown("📸 [Instagram](https://instagram.com/example)")

    st.header("Location")
    st.markdown("📍 Our Office Address:")
    st.markdown("#23, Bangalore City, India Country")

if __name__ == "__main__":
    contact_page()
