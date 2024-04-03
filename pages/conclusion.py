import streamlit as st
import os

def conclusion_page():
    st.title("Conclusion")

    conclusion_text = """
    In conclusion, the Transportation & Traffic 🚦Dashboard offers valuable insights into traffic management and transportation planning in Bangalore. By analyzing 🚗 historical traffic data, understanding transportation modes' usage and popularity, and utilizing traffic predictions and real-time updates, commuters can plan their routes more efficiently, avoiding congested areas and minimizing travel time. Keeping citizens informed about transportation 🚧 news, infrastructure projects, and traffic incidents promotes transparency and enhances public engagement. Analyzing accident data and fines collected helps identify safety hazards and enforce traffic regulations, ultimately improving road safety for all. As Bangalore continues to grow and evolve, it is crucial to invest in sustainable transportation solutions and prioritize projects that enhance mobility and accessibility. 
    By working together and leveraging data-driven insights, we can create a more efficient, safer, and sustainable🛣️ transportation system for Bangalore's residents and visitors. 🚗🌟

    Additionally, embracing innovative technologies such as AI-driven traffic management systems and smart infrastructure can further revolutionize Bangalore's transportation landscape. By integrating IoT sensors into roads and vehicles, we can gather real-time data on traffic flow, air quality, and road conditions, allowing for dynamic adjustments and optimized routing. Moreover, initiatives like carpooling and bike-sharing programs can reduce carbon emissions and alleviate traffic congestion, contributing to a greener and more sustainable cityscape. Together, with a collective effort and a vision for the future, we can pave the way towards a vibrant, interconnected, and resilient urban environment for generations to come. 🚀🌳🌇
"""


    # Center-align the paragraph
    st.markdown(f'<p style="text-align: justify;">{conclusion_text}</p>', unsafe_allow_html=True)

    # Add a heading for feedback
    st.header("Feedback")

    # Add a feedback button
    with st.form("Feedback Form"):
        feedback_name = st.text_input("Your Name", key="feedback_name")
        feedback_comments = st.text_area("Comments", key="feedback_comments")
        feedback_rating = st.selectbox("Rate the dashboard", ["😞 Poor", "😐 Fair", "😊 Good", "😃 Very Good", "🌟 Excellent"], key="feedback_rating")
        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            # Check if all fields are filled
            if not (feedback_name and feedback_comments and feedback_rating):
                st.warning("Please fill out all fields before submitting.")
            else:
                # Process feedback
                st.success("Your Response Has Been Recorded ✔️")
                save_feedback_data(feedback_name, feedback_comments, feedback_rating)

                # Display bursting crackers
                st.balloons()

                # Show the thank you message
                st.markdown('<div style="background-color: #f4f4f4; border-radius: 10px; padding: 20px; text-align: center; animation: pulse 1s infinite;"><h2 style="color: green;">Thank you for your feedback!</h2><style>@keyframes pulse {0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); }}</style></div>', unsafe_allow_html=True)

def save_feedback_data(name, comments, rating):
    data_folder = "feedback_data.txt"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    file_path = os.path.join(data_folder, 'feedback_data.txt')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"Name: {name}\nComments: {comments}\nRating: {rating}\n\n")

def main():
    st.set_page_config(page_title="Transportation & Traffic Dashboard")

    # Sidebar navigation
    page = st.sidebar.selectbox("Select Page", ["Conclusion"])

    if page == "Conclusion":
        conclusion_page()

if __name__ == "__main__":
    main()
