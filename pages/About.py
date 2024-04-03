import streamlit as st

def about_page():
    # Center-align the GIF image
    col1, col2, col3 = st.columns([1, 1, 1])  # Create columns with appropriate widths
    with col2:  # Place the image in the middle column
        st.image("images/about.gif", width=200)
    
    # Introduction section
    st.header("Welcome!")
    st.write("Welcome to the Transportation & Traffic Dashboard, your one-stop solution for gaining valuable insights into traffic management and transportation planning in Bangalore!")

    # Project purpose section with emoji and colored text
    st.subheader("🚗 Project Purpose")
    st.markdown("<p style='color:#006600;'>The purpose of this project is to address the pressing challenges faced by urban commuters in Bangalore due to traffic congestion and inefficient transportation systems. By providing comprehensive data analysis and visualization tools, our dashboard aims to empower commuters, city planners, and policymakers with the information they need to make informed decisions and improve the city's transportation infrastructure.</p>", unsafe_allow_html=True)

    # Why it's needed section with emoji and colored text
    st.subheader("🌍 Why It's Needed")
    st.markdown("<p style='color:#003399;'>Bangalore, as one of India's fastest-growing cities, is experiencing rapid urbanization and population growth, leading to increased traffic congestion, longer commute times, and environmental pollution. Effective transportation management is essential for ensuring the city's sustainable development and improving the quality of life for its residents.</p>", unsafe_allow_html=True)

    # Key features section with emoji and bullet points
    st.subheader("🔑 Key Features")
    st.markdown("""
    - **Real-Time Traffic Updates**: Stay informed about current traffic conditions, road closures, and accidents to plan your commute more efficiently.
    - **Historical Data Analysis**: Explore trends and patterns in historical traffic data to understand traffic flow and congestion hotspots over time.
    - **Predictive Analytics**: Utilize predictive models to forecast future traffic trends and optimize route planning for upcoming journeys.
    - **Public Engagement**: Engage with citizens by providing interactive tools and visualizations to gather feedback and suggestions for improving transportation services.
    """)

    # Benefits section with emoji and bullet points
    st.subheader("💡 Benefits")
    st.markdown("""
    - **Time Savings**: By avoiding congested areas and optimizing routes, commuters can save valuable time during their daily travels.
    - **Safety Improvements**: Analyzing accident data and identifying safety hazards can help enforce traffic regulations and reduce the risk of accidents on the road.
    - **Environmental Impact**: Promoting carpooling and bike-sharing programs can reduce carbon emissions and contribute to a cleaner and greener environment.
    """)

    # Importance of Accident Awareness section
    st.subheader("🚨 Importance of Accident Awareness")
    st.write("It's crucial for commuters to be aware of traffic accidents and their causes. By understanding common accident scenarios and risk factors, individuals can take proactive measures to avoid dangerous situations and contribute to overall road safety.")

    # Adherence to Traffic Rules section
    st.subheader("🚦 Adherence to Traffic Rules")
    st.write("Following traffic rules and regulations is essential for maintaining order on the roads and preventing accidents. By obeying speed limits, traffic signals, and lane markings, motorists can reduce the likelihood of collisions and ensure smooth traffic flow.")

    # Significance of Fines Collected section
    st.subheader("💰 Significance of Fines Collected")
    st.write("The fines collected for traffic violations play a significant role in promoting compliance with traffic laws and regulations. By enforcing penalties for infractions such as speeding, reckless driving, and parking violations, authorities can deter unsafe behavior and improve road safety for all.")

        # Powered by Streamlit section with emoji and colored text
    st.subheader("🚀 Powered by Streamlit")
    st.markdown("<p style='color:#990000;'>This project is powered by Streamlit, a powerful Python framework for building interactive web applications with ease. Streamlit provides a user-friendly interface, extensive customization options, and seamless integration with data analysis libraries such as Pandas and Plotly, making it the perfect choice for creating dynamic and attractive data dashboards.</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#990000;'>With Streamlit, we can create visually stunning visualizations, incorporate interactive widgets for user input, and deploy our dashboard as a web application with just a few lines of code, enabling us to deliver an engaging and immersive experience to our users.</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#990000;'>Join us on this journey towards transforming Bangalore's transportation landscape and creating a smarter, more sustainable city for all! 🌍</p>", unsafe_allow_html=True)

        # Additional information and symbols related to Streamlit
    st.markdown("<p style='font-size:20px; text-align: left;'>For inquiries ✉️ and collaborations ➡️ please contact us at <a href='https://streamlit.io/'>streamlit.io</a>.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px; text-align: left;'>For updates 🐦 and announcements ➡️ Follow Streamlit on Twitter <a href='https://twitter.com/streamlit'>@streamlit</a> </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px; text-align: left;'>To learn  🔗 more about the team and projects ➡️ Connect with Streamlit on LinkedIn <a href='https://www.linkedin.com/company/streamlit/'>here</a> </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px; text-align: left;'>To engage with other users 💬 and share your feedback ➡️ Join the Streamlit community forum <a href='https://discuss.streamlit.io'>here</a></p>", unsafe_allow_html=True)

def main():
    # Set page title and background color
    st.set_page_config(page_title="Transportation & Traffic Dashboard - About", page_icon="🚦", layout="wide", initial_sidebar_state="expanded")

    # Sidebar navigation
    page = st.sidebar.selectbox("Select Page", ["About"])

    if page == "About":
        about_page()

if __name__ == "__main__":
    main()