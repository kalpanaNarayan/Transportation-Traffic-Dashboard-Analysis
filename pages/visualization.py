import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Function to load and visualize data for road accidents
def visualize_road_accidents_data():
    # Load the data from the CSV file
    data = pd.read_csv('data/road-accidents.csv')

    # Streamlit app
    st.title("🚗 Road Accidents Visualization")

    # Display the dataset
    st.subheader("📊 Dataset")
    st.write(data)

    # User input for selecting the columns to plot
    plot_options = ["Fatal Road Accidents", "Non-Fatal Road Accidents", "Total"]
    plot1_option = st.selectbox("Select the first column for the first plot:", plot_options)
    plot2_option = st.selectbox("Select the second column for the second plot:", plot_options, index=1)

    # Ensure selected columns exist in DataFrame
    if plot1_option not in data.columns:
        st.error(f"❌ Column '{plot1_option}' not found in dataset.")
        return

    if plot2_option not in data.columns:
        st.error(f"❌ Column '{plot2_option}' not found in dataset.")
        return

    # Create the 3D scatter plots
    fig1 = px.scatter_3d(data, x='Year', y=plot1_option, z='Total', color='Total',
                        color_continuous_scale='Viridis', opacity=0.7,
                        title=f"📈 3D Scatter Plot: Year vs {plot1_option} vs Total",
                        labels={'Year': 'Year', plot1_option: plot1_option, 'Total': 'Total'})

    fig2 = px.scatter_3d(data, x='Year', y=plot2_option, z='Total', color='Total',
                        color_continuous_scale='Plasma', opacity=0.7,
                        title=f"📊 3D Scatter Plot: Year vs {plot2_option} vs Total",
                        labels={'Year': 'Year', plot2_option: plot2_option, 'Total': 'Total'})

    # Display the plots
    st.subheader("📈 3D Scatter Plot: Year vs Fatal Road Accidents vs Total")
    st.plotly_chart(fig1)

    st.subheader("📊 3D Scatter Plot: Year vs Non-Fatal Road Accidents vs Total")
    st.plotly_chart(fig2)

# Function to load and visualize data for bus routes
def visualize_bus_routes_data():
    # Load the data from the CSV file
    data = pd.read_csv('data/bus_routes.csv')

    # Streamlit app
    st.title("🚌 Bus Routes Visualization")

    # Display the dataset
    st.subheader("📊 Dataset")
    st.write(data)

    # Create scatter plot for Depots and Mobile_Number, colored by Name
    fig1 = px.scatter(data, x='Depots', y='Mobile_Number', color='Name', title="🚍 Scatter Plot: Depots vs Mobile Number (colored by Name)")

    # Display the plot
    st.plotly_chart(fig1)

# Function to visualize BTP cases data
def visualize_btp_cases_data():
    # Load the data from the CSV file
    data = pd.read_csv('data/btp-cases-fines-collected-under-various-acts-2011-2023.csv')

    # Streamlit app
    st.title("🚦 BTP Cases Visualization")

    # Display the dataset
    st.subheader("📊 Dataset")
    st.write(data)

    # User input for selecting columns
    x_column = st.selectbox("Select X-axis Column", data.columns)
    y_column = st.selectbox("Select Y-axis Column", data.columns)
    z_column = st.selectbox("Select Z-axis Column", data.columns)

    # Create 3D scatter plot based on user selection
    fig = create_3d_scatter_plot(data, x_column, y_column, z_column)

    # Display the plot
    st.plotly_chart(fig)

# Function to create 3D scatter plot
def create_3d_scatter_plot(data, x_column, y_column, z_column):
    fig = go.Figure(data=[go.Scatter3d(
        x=data[x_column],
        y=data[y_column],
        z=data[z_column],
        mode='markers',
        marker=dict(
            size=8,
            color=data['YEAR'],  # Color by Year column
            colorscale='Viridis',  # Choose a colorscale
            opacity=0.8
        ),
        text=data['YEAR'],  # Hover text
        hoverinfo='text'
    )])

    fig.update_layout(scene=dict(
        xaxis_title=x_column,
        yaxis_title=y_column,
        zaxis_title=z_column
    ))

    return fig

# Streamlit app
def main():
    st.set_page_config(page_title="🚥 Multi-Page Web App")

    # Sidebar navigation
    page = st.sidebar.selectbox("Select Page", ["🚗 Road Accidents", "🚌 Bus Routes", "🚦 BTP Cases"])

    if page == "🚗 Road Accidents":
        visualize_road_accidents_data()
    elif page == "🚌 Bus Routes":
        visualize_bus_routes_data()
    elif page == "🚦 BTP Cases":
        visualize_btp_cases_data()

# Entry point of the script
if __name__ == "__main__":
    main()
