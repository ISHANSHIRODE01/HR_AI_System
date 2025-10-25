@echo off
echo Starting Streamlit Dashboard...
echo Expected: Local URL: http://localhost:8501 (or 8503 if busy)
echo Expected: Some Plotly warnings (normal)
echo.
cd ..
streamlit run src\dashboard.py