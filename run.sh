#!/bin/bash
echo "Starting HR-AI Core System..."
echo "API will be available at: http://localhost:8000"
echo "API Docs will be available at: http://localhost:8000/docs"
echo "To start dashboard, run: streamlit run dashboard/app.py"
uvicorn app.main:app --reload