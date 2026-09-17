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
       # --- PREMIUM STRUCTURAL PAYWALL LOCK ---
    st.markdown("---")
    st.subheader("📋 Advanced Route Matrix Data Feed")

    col1, col2 = st.columns()

    with col1:
        st.info(
            "🔒 **Premium Feature Locked:** Full historical spreadsheet access, automated CSV exports, and raw API access lines are reserved for enterprise subscribers."
        )
        
        # आपका लाइव पेपैल बटन कोड यहाँ सुरक्षित रूप से एम्बेड किया गया है
        paypal_html = """
        <div style="display: flex; justify-content: center; align-items: center; width: 100%;">
            <div id="paypal-button-container-P-9LH44979C8293391UNKV3JZY" style="width: 100%; max-width: 350px;"></div>
        </div>
        <script src="https://www.paypal.com/sdk/js?client-id=BAAxGBo37rypMsToJifP6HuZDBzftBm3ElcGDe3Gy2Hn9ci4VJhihHIGheLMZhlNye1mLi3Uvw63__R9wM&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
        <script>
          paypal.Buttons({
              style: {
                  shape: 'rect',
                  color: 'gold',
                  layout: 'vertical',
                  label: 'subscribe'
              },
              createSubscription: function(data, actions) {
                return actions.subscription.create({
                  plan_id: 'P-9LH44979C8293391UNKV3JZY'
                });
              },
              onApprove: function(data, actions) {
                alert("Subscription Successful! Your ID is: " + data.subscriptionID);
              }
          }).render('#paypal-button-container-P-9LH44979C8293391UNKV3JZY');
        </script>
        """
        
        # यह फंक्शन आपके पेपैल बटन को स्ट्रीमलिट वेबसाइट पर रेंडर करेगा
        st.components.v1.html(paypal_html, height=180)

    with col2:
        st.metric(label="Selected Route Spot Price", value=f"${filtered_df['Spot_Base_Rate_USD'].iloc[-1]} USD")
        st.caption("Updated 24 hours ago via Global Shipping Nodes.")

else:
    st.warning(
        "Database asset file not found. Please execute freight_scraper.py first to compile data."
    )
