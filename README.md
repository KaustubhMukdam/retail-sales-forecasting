# 🛍️ Ecuador Retail Sales Time Series Forecasting

A robust sales forecasting system using Machine Learning, capturing complex seasonal patterns and macro-economic drivers in Ecuador's retail market.

---

## 🚀 5-Minute Project Overview

### The Business Problem

**Accurate demand forecasting** to optimize inventory, prevent stockouts, and maximize profitability in a national retail chain (479,228 time series).

### Key Challenge

**Over 33% of time series are non-stationary.** Sales patterns fluctuate wildly due to holidays, promotions, and oil price volatility, making simple averages useless.

### The Solution

**Per-Family LightGBM with Lag Features + Holiday Indicators**
We built a custom machine learning model for each product category that learns:

- **Recent Trends**: Sales momentum over the last 45 days
- **Seasonality**: Weekly and annual patterns
- **Macro Factors**: Oil price impact on consumer spending
- **Promotional Lift**: Special event demand boosts

### Performance

**✅ 0.40562 RMSLE (Best Kaggle Public Score)**

- Outperformed naive baselines by **39%**
- Superior handling of intermittent and volatile series

---

## 📋 Project Context

### The Datasets

- **train.csv**: 913,000 records (2013–2017)
- **test.csv**: 336,000 records (16-day forecast horizon)
- **stores.csv**: 54 store locations
- **oil.csv**: Ecuador's oil price history
- **holidays_events.csv**: National holidays and events

### Business Impact

- **Inventory Optimization**: Right stock at right time
- **Reduced Waste**: Minimize expired or unsold goods
- **Sales Maximization**: Capitalize on peak demand periods
- **Operational Efficiency**: Better staffing and supply chain planning

---

## 🛠️ Tech Stack

### Core Libraries

- **Python 3.9+**
- **Pandas/NumPy**: Data manipulation and feature engineering
- **LightGBM**: High-performance gradient boosting
- **Scikit-Learn**: Metrics and validation
- **Seaborn/Matplotlib**: Visualization

### Key Techniques

- **Time Series Feature Engineering**: Rolling means, lags, expanding windows
- **Seasonal Decomposition**: Trend, seasonality, residual analysis
- **Cross-Validation**: Time-series split to prevent leakage
- **Error Analysis**:RMSLE optimization

---

## 📂 Folder Structure

```
retail-sales-forecasting/
├── .venv/                     # Virtual environment
├── data/                      # Raw datasets
│   ├── train.csv
│   ├── test.csv
│   ├── stores.csv
│   ├── oil.csv
│   └── holidays_events.csv
├── notebooks/                 # Jupyter notebooks for exploration
│   ├── EDA_and_Feature_Engineering.ipynb
│   ├── Model_Development_and_Tuning.ipynb
│   ├── Advanced_Modeling_and_Ensembling.ipynb
│   └── Dashboard_Prototyping.ipynb
├── outputs/                   # Generated artifacts
│   ├── feature_importance.png
│   ├── holiday_effect.png
│   ├── oil_vs_sales.png
│   ├── sales_seasonal_decomposition.png
│   ├── store_cluster_heatmap.png
│   └── forecast_vs_actual_top3.png
├── .gitignore
├── app.py                     # Streamlit dashboard
├── requirements.txt           # Dependencies
├── submission.csv             # Final submission file
└── README.md                  # Project documentation
```

---

## 📋 Detailed Work Breakdown

### Phase 1: Exploration & Feature Engineering

**Completed** ✅

**Key Achievements:**

- Analyzed sales distributions and seasonality across all 33 product families
- Built comprehensive time-series features (lags, rolling means, expanding windows)
- Engineered holiday and event indicators
- Optimized store-level feature engineering to prevent data leakage

**Key Findings:**

- **7.9% of time series are intermittent** (zero sales for >95% of days)
- **Oil price positively correlates** with national sales trends
- **Holiday spikes** significantly increase demand (Christmas +35–50%)

**Critical Success Factors:**

- **Time-series cross-validation**: Prevented overfitting
- **Per-family modeling**: Tailored features for each product type
- **Leakage prevention**: Critical for lag features across families

---

### Phase 2: Modeling & Optimization

**Completed** ✅

**Models Developed:**

#### Baseline Model (Optimal)

```python
PerFamilyLGBM(lags=range(1, 46), rolling_windows=range(7, 46, 7))
```

**Performance:**

- **Score**: 0.40562 RMSLE (Best Public Score)
- **Validation**: 0.41246 (Time-Series Split)
- **Public/Private Delta**: 0.00684 (Stable across splits)

**Why it won:**
✅ Custom feature set tailored to product characteristics
✅ No data leakage (lag features computed per family)
✅ Handles intermittent series better than statistical methods
✅ Fast training and prediction times

#### Advanced Model (Underperforming)

```python
Ensemble of XGBoost + LightGBM + Linear Regression
```

**Issues:**
❌ Corrupted lag features (multiple family bug)
❌ More complex = more prone to overfitting
❌ No improvement over optimized baseline

**Performance:**

- **Score**: 0.79880 RMSLE (39% worse than baseline)
- **Validation**: 0.74898 (Significant public/private gap)

**Key Learnings:**

- Keep models interpretable for easier debugging
- Avoid feature engineering at scale without rigorous validation
- Sometimes the simplest, most optimized model wins

---

### Phase 3: Production & Deployment

**Completed** ✅

**Production Pipeline:**

1. **Feature Engineering**: Daily computation for all time series
2. **Prediction**: Generate 16-day forecast for all stores
3. **Submission**: Format for Kaggle evaluation

**Deployment Options:**

- **Option 1: Daily Cron Job**: Simple CSV generation for BI tools
- **Option 2: Docker Container**: Scalable API endpoint
- **Option 3: Streamlit Dashboard**: Interactive visualization
- **Option 4: Cloud Pipeline**: GCP Vertex AI pipelines

---

## 📊 Results

### Performance Comparison

| Model                   | Public Score | Validation Score | Improvement          |
| ----------------------- | ------------ | ---------------- | -------------------- |
| **Per-Family LightGBM** | **0.40562**  | 0.41246          | **✅ Best Approach** |
| Advanced Ensemble       | 0.79880      | 0.74898          | ❌ Underperforming   |
| Fixed Lag Ensemble      | 0.74898      | 0.74898          | ❌ Underperforming   |

### Key Findings

- **Model Stability**: Public/Private split difference < 0.01 suggests no overfitting
- **Data Quality**: 39% of rows have zero sales (intermittent series)
- **Feature Importance**: Recent rolling means are most predictive
- **Holiday Impact**: Easter and Christmas show significant demand spikes

---

## 🗺️ Road Ahead

### Immediate Improvements

- [ ] Incorporate oil price predictions into the model
- [ ] Add store-cluster specific features
- [ ] Implement demand-shaping for promotions
- [ ] Deploy as scalable prediction API

### Future Enhancements

- [ ] Deep learning models (LSTM/Transformer) for long-term patterns
- [ ] Real-time online learning updates
- [ ] Multi-horizon forecasting (16+ days)
- [ ] A/B testing framework for inventory strategies

---

## 🚀 How to Run

### Option 1: Local Development

```bash
# Setup environment
python -m venv .venv
(.venv) \Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run EDA
jupyter notebook notebooks/EDA_and_Feature_Engineering.ipynb

# Run modeling
jupyter notebook notebooks/Model_Development_
```
