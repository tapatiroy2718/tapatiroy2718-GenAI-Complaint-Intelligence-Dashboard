# GenAI Complaint Intelligence Dashboard (Hackathon Project)

## 🔥 Project summary

This project is a complete end-to-end GenAI solution for customer complaint analytics. It demonstrates:

- Synthetic dataset generation (10,000 complaints) via Python
- Sentiment analysis using TextBlob
- Semantic clustering with SentenceTransformer embeddings + KMeans
- Self-learning complaint category classification using LogisticRegression
- Geospatial complaint heatmap by city
- Month-over-month trend and delta analytics
- Hugely interactive Streamlit dashboard (filters, KPIs, maps, charts)
- Auto-reply generator for live support interaction
- CSV upload + dynamic retraining capability

## 📁 Files in this repo

- `generate_data.py` — generates synthetic complaint dataset
- `complaints.csv` / `complaints_10k.csv` — generated sample datasets
- `app.py` — Streamlit dashboard UI with GenAI features
- `README.md` — setup and demo instructions
- `PROJECT.md` — polished project description
- `run_demo.bat` — quick local run script

## 🛠️ How to run

1. Install dependencies:

   ```powershell
   pip install pandas streamlit textblob scikit-learn sentence-transformers matplotlib
   python -m textblob.download_corpora
   ```

2. Generate data:

   ```powershell
   python generate_data.py
   ```

3. Start dashboard:

   ```powershell
   python -m streamlit run app.py
   ```

4. Open browser at `http://localhost:8501`

## 🧩 Hackathon showcase narrative

1. Problem: need intelligent ticket triage and root-cause analytics for complaint systems.
2. Solution: a single dashboard that includes sentiment, clustering, classification, and geo mapping.
3. Execution: code + data generator + interactive visualization in Streamlit.
4. Impact: rapid decision-making for support teams and ML-driven insights for product improvements.

## 🌐 GitHub repo link

Your code files should be visible here after push:

`https://github.com/tapatiroy2718/GenAI-Complaint-Intelligence-Dashboard`

If access is still blocked, clear credentials or use SSH and push again:

```powershell
# using HTTPS
git remote set-url origin https://github.com/tapatiroy2718/GenAI-Complaint-Intelligence-Dashboard.git
git push -u origin main

# or using SSH
git remote set-url origin git@github.com:tapatiroy2718/GenAI-Complaint-Intelligence-Dashboard.git
ssh-keygen -t ed25519 -C "your-email@example.com"
# add public key to GitHub
git push -u origin main
```

## ✅ Final result

This repo is now complete and presentation-ready for hackathon submission. Include a video link and what-if impact slide to impress judges.
