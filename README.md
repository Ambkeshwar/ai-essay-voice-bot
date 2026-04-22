```markdown
# 🎙️ AI Voice Essay Brainstormer

An AI-powered FastAPI application that converts voice input into text, asks intelligent follow-up questions, and generates a structured essay based on the conversation.

---

## 🚀 Features

- 🎤 Voice-to-Text using OpenAI transcription
- 🤖 AI-generated follow-up questions
- 🧠 Conversation memory tracking
- 📝 Essay structure generation
- ⚡ FastAPI-based backend
- 🔄 Audio format auto-conversion to `.wav` using FFmpeg

---

## 🏗️ Project Structure

```text
ai-essay-voice-bot/
│
├── app/
│   ├── services/
│   │   ├── stt_service.py        # Speech-to-text logic
│   │   ├── llm_service.py        # Question generation
│   │   ├── essay_service.py      # Essay structure generation
│   │
│   ├── utils/
│   │   └── memory.py             # Conversation memory
│   │
│   ├── core/
│   │   └── config.py             # Environment settings
│
├── app.py                        # FastAPI entry point
├── requirements.txt
├── .env                          # (Not committed)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```

git clone [https://github.com/Ambkeshwar/ai-essay-voice-bot.git](https://github.com/Ambkeshwar/ai-essay-voice-bot.git)
cd ai-essay-voice-bot

```

---

### 2️⃣ Create Virtual Environment

```

python -m venv .venv
.venv\Scripts\activate   # Windows

```

---

### 3️⃣ Install Dependencies

```

pip install -r requirements.txt

```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```

OPENAI_API_KEY=your_openai_api_key

```

⚠️ Never commit this file.

---

### 5️⃣ Install FFmpeg (Required)

Download and install FFmpeg, then add it to PATH.

Verify installation:

```

ffmpeg -version

```

---

### 6️⃣ Run the Application

```

python app.py

```

Server will start at:

```

[http://localhost:5000](http://localhost:5000)

```

---

## 📡 API Endpoints

### 🔹 1. Upload Voice Input

**POST** `/voice-input/`

- Upload audio file (form-data)

**Response:**
```

{
"user_text": "Transcribed text",
"ai_question": "Follow-up question"
}

```

---

### 🔹 2. Generate Essay

**GET** `/generate-essay/`

**Response:**
```

{
"essay_structure": "Generated essay outline"
}

```

---

## 🧪 Testing (Postman)

### Voice Input
- Method: POST  
- Body: form-data  
- Key: `file` (type: File)

---

## 🎨 Streamlit UI (Frontend)

This project includes a Streamlit-based UI for interacting with the FastAPI backend.

---

## ▶️ Running the Application

This application has two parts:
1. FastAPI Backend
2. Streamlit Frontend

---

### 1️⃣ Start FastAPI Server

```bash
python app.py
```

Backend will run at:
```
http://localhost:5000
```

---

### 2️⃣ Start Streamlit UI (in a new terminal)

```bash
streamlit run streamlit_app.py
```

Frontend will run at:
```
http://localhost:8501
```

---

## ⚠️ Important Notes

- Make sure FastAPI is running before starting Streamlit  
- Ensure the API URL in `streamlit_app.py` is:

```python
API_URL = "http://127.0.0.1:5000"
```

- Use correct endpoints:
  - `/voice-input`
  - `/generate-essay`

---

## 🚀 Optional: Run Both Together

You can create a helper script `run_all.py`:

```python
import subprocess

subprocess.Popen(["python", "app.py"])
subprocess.Popen(["streamlit", "run", "streamlit_app.py"])

input("Press ENTER to stop...")
```

Run it using:

```bash
python run_all.py
```

---

## 🧪 How It Works

1. Upload audio via Streamlit UI  
2. Audio is sent to FastAPI `/voice-input/`  
3. AI generates transcription + follow-up question  
4. Conversation is maintained in memory  
5. Click **Generate Essay** to call `/generate-essay/`  
6. Structured essay is displayed on the UI  



## ⚠️ Common Issues

### ❌ 307 Redirect
Use correct endpoint with trailing slash:
```

/voice-input/

```

### ❌ FFmpeg Not Found
Ensure FFmpeg is installed and added to PATH.

### ❌ Audio Not Supported
The app auto-converts audio to `.wav`. Ensure valid audio input.

---

## 🔐 Security

- Do NOT commit `.env`
- Rotate API keys if exposed
- Use environment variables for secrets

---

## 🛠️ Tech Stack

- FastAPI
- OpenAI API
- FFmpeg
- Python 3.10+

---

## 📌 Future Improvements

- 🎙️ Real-time streaming transcription
- 🧠 Context-aware essay generation
- 🌐 Frontend UI integration
- ☁️ Docker deployment

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is for educational and experimental purposes.

---

## 👨‍💻 Author

**Ambkeshwar Shukla**
```
