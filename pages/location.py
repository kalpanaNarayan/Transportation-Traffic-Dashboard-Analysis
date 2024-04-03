import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import folium
from streamlit_folium import folium_static
from datetime import datetime
import time

def main_location():
    # # Set page configuration
    # st.set_page_config(page_title="Bangalore Traffic Dashboard", page_icon="🚦", layout="wide")
        # Define page title, icon, and layout
    page_title = "Bangalore Traffic Dashboard"
    page_icon = "🚦"
    layout = "wide"

    # Set page title, icon, and layout using HTML and Markdown
    st.markdown(f'<title>{page_title}</title>', unsafe_allow_html=True)
    st.markdown(f'<link rel="shortcut icon" href="data:image/png;base64,{page_icon}">', unsafe_allow_html=True)
    st.markdown(f'<style>body {{ margin: 0; }}</style>', unsafe_allow_html=True)
    st.markdown(f'<style> .reportview-container .main .block-container{{ max-width: 100%; padding-top: 2rem; padding-right: 2rem; padding-left: 2rem; padding-bottom: 3rem; }}</style>', unsafe_allow_html=True)

    st.title("Bangalore🚌Traffic🗺️Dashboard ")

    st.subheader("Live Traffic Map 📍")

    # Create a map centered around Bangalore
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=11)

    # Add markers for traffic signals
    signal_locations = [(12.9716, 77.5946), (12.9619, 77.5937), (12.9791, 77.5913)]
    signal_icons = ['🚦', '🚥', '⛔']
    signal_statuses = ['High Traffic', 'Medium Traffic', 'Low Traffic']

    for loc, icon, status in zip(signal_locations, signal_icons, signal_statuses):
        folium.Marker(location=loc, popup=status, icon=folium.Icon(color='red')).add_to(m)

    folium_static(m)

    st.subheader("📊 Traffic Density Analysis")

    # Generate random data for traffic density
    df = pd.DataFrame({
        'Area': [f"Area {i}" for i in range(1, 101)],
        'Density': np.random.randint(1, 100, 100)
    })

    # Display traffic density table
    st.write("Top 10 Areas with High Traffic Density:")
    st.dataframe(df.sort_values(by='Density', ascending=False).head(10))

    # Bar plot for traffic density
    fig = go.Figure(data=[go.Bar(
        x=df['Area'],
        y=df['Density'],
        marker=dict(color=df['Density'], colorscale='Viridis', colorbar=dict(title='Density'))
    )])
    fig.update_layout(
        title="Traffic Density by Area",
        xaxis_title="Area",
        yaxis_title="Density"
    )
    st.plotly_chart(fig)

    st.subheader("🚌 Transportation Routes")

    # User selection options for transportation routes
    selected_route = st.selectbox("Select Transportation Route", ["Route 1", "Route 2", "Route 3"])

    st.write(f"You have selected: {selected_route}")

    st.subheader("📈 3D Traffic Plot")

    # Generate random data for 3D scatter plot
    df = pd.DataFrame({
        'X': np.random.rand(100),
        'Y': np.random.rand(100),
        'Z': np.random.rand(100),
        'Color': np.random.rand(100)  # Random color values
    })

    fig = go.Figure(data=[go.Scatter3d(
        x=df['X'],
        y=df['Y'],
        z=df['Z'],
        mode='markers',
        marker=dict(
            size=8,
            color=df['Color'],  
            colorscale=[
                [0, 'purple'],  
                [0.5, 'skyblue'],
                [1, 'pink']
            ],
            opacity=0.8,
            symbol='circle' ,
            line=dict(width=2, color='black')
        ),
        text='Random Data',  
        hoverinfo='text'
    )])

    fig.update_layout(
        scene=dict(
            xaxis=dict(title='X'),
            yaxis=dict(title='Y'),
            zaxis=dict(title='Z')
        ),
        title="3D Traffic Density Analysis (Scatter Plot)"
    )

    st.plotly_chart(fig)


    st.subheader("⏰ TIME and DATE")
    st.markdown("") 
    st.markdown("")  

# Display animated clock GIF
    clock_image_url = "https://upload.wikimedia.org/wikipedia/commons/7/7a/Alarm_Clock_GIF_Animation_High_Res.gif"
    st.image(clock_image_url, width=200)

        # Display current time
    current_time = datetime.now().strftime("%H:%M:%S")
    st.subheader(f"Time: {current_time}")

    # Display current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    st.subheader(f"Date: {current_date}")

    # Display "Thank You Page" text with custom styling
    st.markdown(
        """
        <div style="display: flex; align-items:center ; height: 200px;">
            <style>
                .big-text {
                    font-size: 36px;
                    font-weight: bold;
                    color: purple;  /* Change color as needed */
                    font-family: 'Arial', sans-serif;  /* Change font family as needed */
                }
            </style>
            <p class="big-text">Thank You 🎉</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main_location()
