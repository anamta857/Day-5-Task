import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE ----------------
st.set_page_config(page_title="Student Dashboard", layout="wide")

# ---------------- CSS FIX ----------------
st.markdown("""
<style>

.stApp {
    background-color: #F5F7FA;
}

/* Title */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: #1E3A8A;
    margin-bottom: 10px;
}

/* Metrics fix */
[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

/* Fix hidden text issue */
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: #111827 !important;
}

/* Section headings */
h3 {
    color: #111827 !important;
    font-weight: 600;
}

/* Table visibility fix */
.stDataFrame {
    background-color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">📊 Student Performance Dashboard</div>', unsafe_allow_html=True)

# ---------------- DATA ----------------
df = pd.read_csv("dataset.csv")

# ---------------- METRICS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Total Students", len(df))

with c2:
    st.metric("Average Marks", round(df["Marks"].mean(), 2))

with c3:
    st.metric("Average Attendance", str(round(df["Attendance"].mean(), 2)) + "%")

st.markdown("---")

# ---------------- TABLE (NOW TOP FIXED) ----------------
st.subheader("📋 Dataset Preview")
st.dataframe(df, use_container_width=True)

st.markdown("---")

# ---------------- CHARTS ----------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("Attendance Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["Attendance"], kde=True, ax=ax)
    st.pyplot(fig)

with c2:
    st.subheader("Marks Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["Marks"], kde=True, ax=ax)
    st.pyplot(fig)

# ---------------- HEATMAP ----------------
st.subheader("Feature Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# ---------------- PERFORMANCE ----------------
def get_grade(m):
    if m >= 80:
        return "Excellent"
    elif m >= 60:
        return "Good"
    elif m >= 40:
        return "Average"
    return "Poor"

df["Performance"] = df["Marks"].apply(get_grade)

st.subheader("Performance Categories")

fig, ax = plt.subplots()
df["Performance"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)