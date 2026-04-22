import subprocess

# Start FastAPI
subprocess.Popen(["uv", "run", "app.py"])

# Start Streamlit
subprocess.Popen(["streamlit", "run", "streamlit_app.py"])

input("Press ENTER to stop...")