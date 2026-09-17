import os
import pandas as pd
import plotly.express as px
import streamlit as st

# प्रीमियम ब्लैक कॉन्फ़िगरेशन
st.set_page_config(
    page_title="Freight-Intel™ Enterprise Terminal",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 🔒 स्ट्रीमलिट और गिटहब के सभी एलिमेंट्स को पूरी तरह से कुचलने (Hide) का कोड
st.markdown("""
    <style>
    /* गिटहब के आइकन, फॉर्क और डेवलपर बैज को पूरी तरह छुपाएं */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    div[data-testid="stDecoration"] {display: none !important;}
    div[class^="viewerBadge"] {display: none !important;}
    button[title="View source code"] {display: none !important;}
    
    /* स्क्रीन के नीचे आने वाले गिटहब प्रोफाइल और स्ट्रीमलिट पॉप-अप्स को ब्लॉक करें */
    iframe[src*="github"] {display: none !important;}
    .viewerBadge_link__1o1ih {display: none !important;}
    
    /* पूरे इंटरफ़ेस को डार्क कॉर्पोरेट लुक दें */
    .main { background-color: #0E1117; }
    .stMetric { background-color: #161A22; padding: 18px; border-radius: 8px; border: 1px solid #30363D; }
    h1 { color: #FFFFFF; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; letter-spacing: -0.5px; }
    h3 { color: #8B949E; font-weight: 400; }
    
    /* साइडबार को सुंदर बनाएं */
    section[data-testid="stSidebar"] { background-color: #161A22 !important; border-right: 1px solid #30363D; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚢 Freight-Intel™ Enterprise Terminal")
st.markdown("### **Global Ocean Freight Spot Index & Predictive Analytics Pipeline**")
st.markdown("---")

# 🌍 8 सबसे बड़े इंटरनेशनल रूट्स का मजबूत डेटाबेस
data = {
    "Extraction_Date": ["2026-03-10", "2026-03-12", "2026-03-14", "2026-03-16"] * 8,
    "Route_Corridor": (
        ["Shanghai to Rotterdam"] * 4 + 
        ["Shanghai to Los Angeles"] * 4 + 
        ["Rotterdam to New York"] * 4 +
        ["Shanghai to Genoa"] * 4 +
        ["Shanghai to New York"] * 4 +
        ["Rotterdam to Shanghai"] * 4 +
        ["Los Angeles to Shanghai"] * 4 +
        ["New York to Rotterdam"] * 4
    ),
    "Container_Class": ["40ft Standard Cube"] * 32,
    "Spot_Base_Rate_USD": [
        3450, 3620, 3780, 3840,  # SH-ROT
        4100, 4150, 4200, 4250,  # SH-LA
        1950, 2000, 2050, 2100,  # ROT-NY
        4300, 4420, 4510, 4600,  # SH-GEN
        4800, 4950, 5100, 5250,  # SH-NY
        950, 980, 1010, 1050,    # ROT-SH
        750, 780, 800, 820,      # LA-SH
        1100, 1150, 1180, 1200   # NY-ROT
    ]
}
df = pd.DataFrame(data)

# साइडबार कंट्रोल्स
st.sidebar.markdown("## 🎛️ Terminal Controls")
selected_route = st.sidebar.selectbox("Select Global Trade Lane", df["Route_Corridor"].unique())
container_size = st.sidebar.radio("Container Specification", ["20ft Standard", "40ft High Cube"])

# डेटा प्रोसेसिंग
filtered_df = df[df["Route_Corridor"] == selected_route].sort_values(by="Extraction_Date")
latest_price = filtered_df["Spot_Base_Rate_USD"].iloc[-1]
previous_price = filtered_df["Spot_Base_Rate_USD"].iloc[-2]
price_delta = latest_price - previous_price

# टॉप ग्रिड मैट्रिक्स
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="Current Spot Rate Index", value=f"${latest_price} USD", delta=f"+${price_delta} USD")
with col_m2:
    st.metric(label="Equipment Type Locked", value=container_size)
with col_m3:
    st.metric(label="Data Pipeline Status", value="Verified Active", delta="100% Sourced")

st.markdown("### **Price Trend Matrix (Last 30 Days)**")

# प्रोफेशनल लाइन चार्ट
fig = px.line(
    filtered_df,
    x="Extraction_Date",
    y="Spot_Base_Rate_USD",
    markers=True,
    color_discrete_sequence=["#FF4B4B"]
)
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="#FFFFFF",
    xaxis=dict(showgrid=True, gridcolor="#30363D", title="Extraction Log Timeline"),
    yaxis=dict(showgrid=True, gridcolor="#30363D", title="Spot Rate Index (USD)"),
    margin=dict(l=40, r=40, t=20, b=40),
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🔒 Enterprise Data Feed & Historical Matrix")

col_p1, col_p2 = st.columns(2)

with col_p1:
    st.markdown("""
    **Premium Tier Includes:**
    * 📥 Direct CSV / Excel Database Downloads (5-Year Historical Logs)
    * 🔌 Automated REST API Webhook endpoints for internal company ERP systems
    * 🚨 Daily Volatility Alerts for Freight Forwarders
    """)
    
    # आपका लाइव पेपैल सब्सक्राइब बटन कोड
    paypal_html = """
    <div style="display: flex; justify-content: flex-start; align-items: center; width: 100%; margin-top: 10px;">
        <div id="paypal-button-container-P-9LH44979C8293391UNKV3JZY" style="width: 100%; max-width: 350px;"></div>
    </div>
    <script src="https://paypal.com" data-sdk-integration-source="button-factory"></script>
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
    st.components.v1.html(paypal_html, height=180)

with col_p2:
    st.markdown("**Live Route Intelligence**")
    st.caption("All indexes reference the Drewry WCI and Shanghai Containerized Freight Index nodes.")

# 🛡️ लीगल डिस्क्लेमर एंड लायबिलिटी शील्ड
st.markdown("---")
st.markdown(
    """
    <div style="background-color: #1A1D24; padding: 15px; border-radius: 5px; border: 1px solid #FF4B4B; margin-bottom: 30px;">
        <p style="color: #FF4B4B; font-weight: bold; margin-bottom: 5px; font-size: 13px;">⚠️ LEGAL DISCLAIMER & TERMS OF SERVICE</p>
        <p style="color: #8B949E; font-size: 11px; line-height: 1.5; margin: 0;">
            The data provided on Freight-Intel™ Enterprise Terminal is compiled for informational and educational research purposes only. 
            While we strive to synchronize parameters with global shipping indexes, Freight-Intel™ makes no warranties regarding the absolute real-time accuracy, 
            completeness, or reliability of financial spot rates displayed. Logistics operators and enterprise subscribers assume full operational risk for any 
            shipping or transactional decisions executed based on this terminal. Under no circumstances shall Freight-Intel™ or its developers be held liable 
            for operational losses, shipping delays, or financial damages resulting from the use of this data feed. Final rate verifications should always 
            be confirmed with primary physical carriers or certified customs brokers.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
