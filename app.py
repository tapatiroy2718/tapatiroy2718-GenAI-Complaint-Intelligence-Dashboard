import streamlit as st
import pandas as pd
from textblob import TextBlob
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="GenAI Complaint Intelligence Dashboard", layout="wide")

@st.cache_data(show_spinner=False)
def load_data(path="complaints.csv"):
    return pd.read_csv(path)

@st.cache_resource(show_spinner=False)
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_data(show_spinner=False)
def compute_sentiment(series):
    def _sentiment(text):
        analysis = TextBlob(text)
        p = analysis.sentiment.polarity
        if p > 0.1:
            return "Positive"
        elif p < -0.1:
            return "Negative"
        else:
            return "Neutral"
    return series.apply(_sentiment)

@st.cache_data(show_spinner=False)
def compute_clusters(complaints, n_clusters=4):
    model = load_model()
    embeddings = model.encode(complaints.tolist(), show_progress_bar=False)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    return kmeans.fit_predict(embeddings)

# ------ data load and first look ------
df = load_data("complaints.csv")

if "sentiment" not in df.columns:
    df["sentiment"] = compute_sentiment(df["complaint"])

if "cluster" not in df.columns:
    df["cluster"] = compute_clusters(df["complaint"], n_clusters=6)

st.title("GenAI Complaint Intelligence Dashboard")

# sidebar filters
st.sidebar.header("Filters")
selected_products = st.sidebar.multiselect("Product", options=sorted(df["product"].unique()), default=df["product"].unique())
selected_cities = st.sidebar.multiselect("City", options=sorted(df["city"].unique()), default=df["city"].unique())
selected_sentiments = st.sidebar.multiselect("Sentiment", options=["Positive", "Neutral", "Negative"], default=["Positive", "Neutral", "Negative"])
selected_clusters = st.sidebar.multiselect("Cluster", options=sorted(df["cluster"].unique()), default=sorted(df["cluster"].unique()))
rows = st.sidebar.slider("Sample rows", min_value=5, max_value=100, value=10)

filtered = df[
    df["product"].isin(selected_products) &
    df["city"].isin(selected_cities) &
    df["sentiment"].isin(selected_sentiments) &
    df["cluster"].isin(selected_clusters)
]

# top metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total complaints", len(filtered), delta=len(filtered) - len(df))
col2.metric("Unique products", filtered["product"].nunique())
col3.metric("Cities covered", filtered["city"].nunique())
col4.metric("Negative ratio", f"{filtered[filtered["sentiment"]=="Negative"].shape[0] / max(1, filtered.shape[0]) * 100:.1f}%")

st.subheader("Complaint dip (top rows)")
st.dataframe(filtered.head(rows).reset_index(drop=True))

# layout charts
c1, c2 = st.columns(2)
with c1:
    st.subheader("Sentiment distribution")
    st.bar_chart(filtered["sentiment"].value_counts())

with c2:
    st.subheader("Complaints by product")
    st.bar_chart(filtered["product"].value_counts())

c3, c4 = st.columns(2)
with c3:
    st.subheader("Complaints by city")
    st.bar_chart(filtered["city"].value_counts())

with c4:
    st.subheader("Complaint clusters")
    st.bar_chart(filtered["cluster"].value_counts())

# root cause summary
st.subheader("Top root cause phrases")
common = (
    filtered["complaint"].str.lower().str.replace("[^a-z0-9 ]", "", regex=True)
    .str.split()
    .explode()
    .value_counts()
    .head(15)
)
st.write(common)

# AI auto reply
st.subheader("AI Auto Reply Generator")
complaint_input = st.text_input("Paste or type a customer complaint to create a reply")

if complaint_input:
    reply = f"""
Dear Customer,

Thank you for reporting the issue: "{complaint_input}".
Our team has logged this as a {filtered[filtered['complaint'] == complaint_input]['priority'].iloc[0] if 'priority' in filtered.columns else 'High'} priority case.

We will investigate and update you within 24 hours.

Best regards,
Customer Support Team
"""
    st.code(reply)

# live complaint stream (randomized)
st.subheader("Live complaint stream preview")
for _, row in filtered.sample(min(6, len(filtered))).iterrows():
    st.markdown(f"**{row['complaint_date'] if 'complaint_date' in row else ''}** - {row['product']} ({row['city']}) - {row['sentiment']}")
    st.write(row['complaint'])

# explanation section
with st.expander("Viva/Industry explanation notes"):
    st.markdown("""
- Data source: synthetic complaint logs with product, city, category, priority, and timestamps.
- Sentiment uses TextBlob polarity thresholds to label Positive, Neutral, Negative.
- Root cause clustering: SentenceTransformer embeddings + KMeans identifies themes (3-6 cluster groups).
- KPIs include complaint count, negative sentiment ratio, and feature distribution by product/city.
- Advanced stage: integrate real-world dataset and accuracy tracking (TP/FP for sentiment and cluster mapping).

`Use this section to explain what each dashboard widget means during viva.`
""")

