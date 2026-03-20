@echo off
cd /d "%~dp0"
python -m textblob.download_corpora
python generate_data.py
python -m streamlit run app.py
pause