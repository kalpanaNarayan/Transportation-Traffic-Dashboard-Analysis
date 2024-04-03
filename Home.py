import streamlit as st
from pages import login,visualization,contact,conclusion,location

def home_page():
    st.markdown('<h1 style="text-align: center;">Welcome to the Transportation 🚗 & Traffic Dashboard 🚦</h1>', unsafe_allow_html=True)

    # Center-align the image
    col1, col2, col3 = st.columns([1, 2, 1])  # Create columns with appropriate widths
    with col2:  # Place the image in the middle column
        st.image("images/img6.jpg", caption="Transportation & Traffic", width=300)

    # Add descriptive text with emojis
    st.markdown("""
    ### 🚥 Explore Traffic Patterns
    View historical traffic data and analyze trends to better understand traffic patterns in Bangalore.
    - Analyze traffic data by time of day, day of the week, or month to identify peak traffic hours.
    - Visualize traffic flow and congestion hotspots on interactive maps.
    - Explore historical data to understand seasonal variations and long-term trends.

    ### 🚌 Understand Transportation Modes
    Dive into data regarding different modes of transportation to gain insights into their usage and popularity.
    - Compare usage statistics between public transport, private vehicles, and alternative modes like bicycles.
    - Explore factors influencing mode choice, such as distance traveled, travel time, and cost.
    - Understand the impact of infrastructure improvements on mode choice and travel behavior.

    ### 🗺️ Plan Your Route
    Utilize traffic predictions and analysis to plan your route more efficiently and avoid congested areas.
    - Access real-time traffic updates and road closure information.
    - Use predictive modeling to anticipate traffic conditions for future planning.
    - Incorporate public transportation options and alternative routes into your travel plans.

    ### 📰 Stay Updated
    Get the latest news and updates related to transportation and traffic management in Bangalore.
    - Stay informed about upcoming infrastructure projects and their impact on traffic.
    - Receive alerts about traffic incidents, road closures, and alternate routes to avoid delays.
    - Access real-time data feeds for traffic conditions, construction updates, and public transportation schedules.

    ### 🚨 Analyze Accidents
    Analyze accident cases in Bangalore to identify trends and patterns.
    - Explore the factors contributing to accidents, such as weather conditions, road conditions, and driver behavior.
    - Identify high-risk areas and intersections to prioritize safety improvements and enforcement efforts.
    - Evaluate the effectiveness of traffic safety initiatives and interventions in reducing accidents and injuries.

    ### 🚌 Bus Routes
    Explore bus routes and transportation infrastructure in Bangalore.
    - Access information on bus routes, schedules, and stops to plan your journey.
    - Analyze ridership data and passenger demographics to understand bus usage patterns and demand.
    - Evaluate the accessibility and coverage of public transportation services across different neighborhoods and communities.

    ### 💰 Fines Collected
    Analyze fines collected for traffic violations in Bangalore.
    - Examine trends in traffic citations and enforcement activities to assess compliance and deterrence.
    - Identify common traffic violations and enforcement hotspots to prioritize enforcement efforts.
    - Evaluate the effectiveness of traffic enforcement strategies in reducing violations and improving road safety.

    ### 🚗 Traffic Analysis
    Conduct a comprehensive analysis of traffic in Bangalore.
    - Analyze traffic volume, speed, and congestion levels on major roadways and intersections.
    - Evaluate the impact of transportation infrastructure projects and policy interventions on traffic flow and mobility.
    - Use data visualization and spatial analysis techniques to identify traffic patterns and inform transportation planning and management decisions.
    """)

    # Display an introductory video
    st.video("images/video.mp4")

    # Center-align the button
    col1, col2, col3 = st.columns([3,4, 1])  
    with col2:
        if st.button("Get Started 🚀", key="get_started_btn"):
            st.write("Let's explore Transportation & Traffic Dashboard!", unsafe_allow_html=True)
            st.markdown("""
            <div style="text-align:left">
                <span style="background-color:#f0f0f0; padding:8px 16px; border-radius:5px; cursor:pointer;">Not registered yet?</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
    <div style="text-align:left; margin-top:10px;">
        <a href="http://localhost:8501/login">
            <span style="background-color:#0066ff; color:#ffffff; padding:8px 16px; border-radius:5px; cursor:pointer;">Login or Sign Up</span>
        </a>
    </div>
""", unsafe_allow_html=True)




# def login_page():
#     st.title("Login Page")
#     st.write("This is the login page content.")

# def visualizations_page():
#     st.title("Visualizations Page")
#     st.write("This is the visualizations page. Add your visualization content here.")

# def contact_page():
#     st.title("Contact Page")
#     st.write("You can contact us here.")

def main():
    st.set_page_config(page_title="Multi-Page Web App")

    # Sidebar navigation
    page = st.sidebar.selectbox("Select Page", ["Home", "Login", "Visualizations", "Location","Contact","Conclusion"])

    if page == "Home":
        home_page()
    elif page == "Login":
        login.login_page()
    elif page == "Visualization":
        visualization.visualize_road_accidents_data() 
    elif page == "Road Accidents":
        visualization.visualize_road_accidents_data()
    elif page == "Bus Routes":
        visualization.visualize_bus_routes_data()
    elif page == "BTP Cases":
        visualization.visualize_btp_cases_data()
    elif page == "Location":
        location.main_location()   
    elif page == "Conclusion":
        conclusion.conclusion_page()     
    elif page == "Contact":
        contact.contact_page() 
    else:
        if not is_user_logged_in():
            st.warning("Please log in to access other pages.")
            login.login_page()
            return
        # Display visualization options
        st.subheader("Select Dataset to Visualize")
        dataset = st.selectbox("Select Dataset", ["Road Accidents", "Bus Routes", "BTP Cases"])
        
        if dataset == "Road Accidents":
            visualization.visualize_road_accidents_data()
        elif dataset == "Bus Routes":
            visualization.visualize_bus_routes_data()
        elif dataset == "BTP Cases":
            visualization.visualize_btp_cases_data()   
        elif page == "Contact":
            contact.contact_page()
        elif page == "Location":
            location.main_location()  

def is_user_logged_in():
    return True  

if __name__ == "__main__":
    main()