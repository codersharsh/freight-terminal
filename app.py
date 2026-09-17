import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Set up page configurations for a premium financial terminal look
st.set_page_config(
    page_title="Global Container Freight Index Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🚢 Global Container Freight Index Terminal")
st.markdown(
    "Real-time spot freight tracking rates for 40ft containers across primary global trade corridors."
)

# Load data asset pipeline
db_file = "global_freight_database.xlsx"

if os.path.exists(db_file):
    df = pd.read_excel(db_file)

    # Sidebar for filters
    st.sidebar.header("📊 Filter Operations")
    available_routes = df["Route_Corridor"].unique()
    selected_route = st.sidebar.selectbox("Select Trade Route", available_routes)

    # Filtered dataset
    filtered_df = df[df["Route_Corridor"] == selected_route].sort_values(
        by="Extraction_Date"
    )

    # Create Premium Interactive Visualizations
    fig = px.line(
        filtered_df,
        x="Extraction_Date",
        y="Spot_Base_Rate_USD",
        title=f"Spot Price Over Time: {selected_route}",
        labels={
            "Spot_Base_Rate_USD": "Rate (USD)",
            "Extraction_Date": "Scan Date",
        },
        markers=True,
    )
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    # --- PREMIUM STRUCTURAL PAYWALL LOCK ---
    st.markdown("---")
    st.subheader("📋 Advanced Route Matrix Data Feed")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.info(
            "🔒 **Premium Feature Locked:** Full historical spreadsheet access, automated CSV exports, and raw API access lines are reserved for enterprise subscribers."
        )
        st.button("🔓 Unlock Premium Terminal Access ($199/Month)")

    with col2:
        st.metric(label="Selected Route Spot Price", value=f"${filtered_df['Spot_Base_Rate_USD'].iloc[-1]} USD")
        st.caption("Updated 24 hours ago via Global Shipping Nodes.")

else:
    st.warning(
        "Database asset file not found. Please execute freight_scraper.py first to compile data."
    )
