import streamlit as st
import pandas as pd
from PIL import Image
import os

# --- Page Config ---
st.set_page_config(
    page_title="Retail Sales Forecasting",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Minimal CSS Styling for Senior Analyst Feel ---
st.markdown("""
    <style>
    .main {
        background-color: #0F1117;
        color: #E0E0E0;
    }
    .stMetric {
        background-color: #1A1D2E;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #2A2D3E;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("Retail Sales Forecasting")
    st.markdown("---")
    st.markdown("""
    **Executive Summary Dashboard**
    
    This dashboard presents findings from the Store Sales Time Series Forecasting project.
    
    **Scope:**
    - 54 Stores across Ecuador
    - 33 Product Families
    - 16-Day Forecast Horizon
    
    *Note: Visualizations are pre-computed based on the optimal Baseline Model (0.40562 RMSLE).*
    """)
    st.markdown("---")

# --- Main Content ---
st.title("Retail Sales Forecasting Dashboard")

# --- KPI Row ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Best Model RMSLE", value="0.40562", delta="-0.39 vs Advanced", delta_color="inverse")
with col2:
    st.metric(label="Total Stores Forecasted", value="54")
with col3:
    st.metric(label="Product Families", value="33")
with col4:
    st.metric(label="Forecast Horizon", value="16 Days")

st.markdown("---")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["Historical Trends", "Forecast Accuracy", "Business Insights"])

# Helper function to load images safely
def load_image(image_name):
    path = os.path.join("outputs", image_name)
    if os.path.exists(path):
        return Image.open(path)
    return None

# --- Tab 1: Historical Trends ---
with tab1:
    st.header("Historical Trends & Seasonality")
    
    col1_1, col1_2 = st.columns([2, 1])
    
    with col1_1:
        img_trend = load_image("sales_seasonal_decomposition.png")
        if img_trend:
            st.image(img_trend, use_container_width=True)
        else:
            st.warning("Trend image not found.")
            
    with col1_2:
        st.subheader("Seasonal Peaks")
        st.markdown("""
        Ecuador's retail calendar shows three distinct demand peaks:
        - **Nov–Dec**: Christmas + year-end (+35–50%)
        - **April**: Easter + school season (+15–25%)
        - **July**: Mid-year school supplies (+10–18%)
        
        **Action:** Increase stock levels by at least 30% starting Nov 1st.
        """)
        
    st.markdown("---")
    st.header("Store Cluster Revenue Intensity")
    img_cluster = load_image("store_cluster_heatmap.png")
    if img_cluster:
        st.image(img_cluster, use_container_width=True)
    else:
        st.warning("Cluster heatmap not found.")

# --- Tab 2: Forecast Accuracy ---
with tab2:
    st.header("Forecast vs Actuals (Top 3 Families)")
    
    img_forecast = load_image("forecast_vs_actual_top3.png")
    if img_forecast:
        st.image(img_forecast, use_container_width=True)
    else:
        st.warning("Forecast image not found.")
        
    st.markdown("---")
    st.header("Model Performance Tracking")
    
    # Static markdown table as per modeling_journey.md
    st.markdown("""
    | Model | Kaggle Public Score (RMSLE) | Status | Notes |
    |---|---|---|---|
    | **Baseline (Per-Family LGBM)** | **0.40562** | ✅ **Best approach** | Clean features, no data leakage |
    | Fixed Lag Ensemble | 0.74898 | ❌ Underperforming | Test lag features corrupted |
    | Advanced (XGB + LGBM) | 0.79880 | ❌ Underperforming | Corrupted lags + logic bug |
    """)

# --- Tab 3: Business Insights ---
with tab3:
    st.header("Strategic Business Insights")
    
    # Row 1
    col3_1, col3_2 = st.columns(2)
    with col3_1:
        st.subheader("1. What drives sales predictions?")
        img_feat = load_image("feature_importance.png")
        if img_feat:
            st.image(img_feat, use_container_width=True)
        st.markdown("**Insight:** Recent rolling means and short-term lags dominate predictive power over simple calendar features.")
        
    with col3_2:
        st.subheader("2. Macro Impact: Oil Prices")
        img_oil = load_image("oil_vs_sales.png")
        if img_oil:
            st.image(img_oil, use_container_width=True)
        st.markdown("**Insight:** Positive correlation. High oil prices boost the national economy and retail spending (and vice versa).")
        
    st.markdown("---")
    
    # Row 2
    col3_3, col3_4 = st.columns(2)
    with col3_3:
        st.subheader("3. The Holiday Lift")
        img_hol = load_image("holiday_effect.png")
        if img_hol:
            st.image(img_hol, use_container_width=True)
        st.markdown("**Insight:** National holidays significantly boost sales. The weekend effect is less pronounced than expected in this market.")
        
    with col3_4:
        st.subheader("4. Inventory Risk: Product Volatility")
        img_vol = load_image("family_volatility.png")
        if img_vol:
            st.image(img_vol, use_container_width=True)
        st.markdown("""
        **Action Plan by Volatility Tier:**
        - 🔴 **High (CV > 1.5):** School Supplies, Books (Need +50% safety stock)
        - 🟡 **Medium (CV 1.0-1.5):** Cleaning, Personal Care (Need +20% safety stock)
        - 🟢 **Low (CV < 1.0):** Grocery I, Dairy (Keep lean inventory)
        """)
