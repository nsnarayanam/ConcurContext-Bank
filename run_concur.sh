
#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Launching ConcurContext Bank..."
streamlit run streamlit_app.py
