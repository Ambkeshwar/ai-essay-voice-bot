import streamlit as st
import requests

API_URL = "http://10.106.108.83:5000"

st.set_page_config(layout="wide", page_title="AI Voice Essay Brainstormer")

# ------------------ HEADER ------------------
st.title("🎙️ AI Voice Essay Brainstormer")
st.caption("Speak your thoughts. Get intelligent questions. Build your essay.")

# ------------------ SESSION INIT ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "last_text" not in st.session_state:
    st.session_state.last_text = None

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([2, 1])

# ------------------ LEFT PANEL ------------------
with col1:
    st.subheader("🎤 Voice + Text Input")

    uploaded_file = st.file_uploader(
        "Upload audio file",
        type=["wav", "mp3", "m4a", "webm"]
    )

    # -------- AUDIO BUTTON --------
    if st.button("Send Audio / Combine"):
        if not uploaded_file and not st.session_state.last_text:
            st.warning("Please provide audio or text input")
        else:
            files = {}
            data = {}

            # Attach file if available
            if uploaded_file:
                files["file"] = uploaded_file

            # Attach text if available
            if st.session_state.last_text:
                data["text"] = st.session_state.last_text

            response = requests.post(
                f"{API_URL}/voice-input",
                files=files if files else None,
                data=data if data else None
            )

            if response.status_code == 200:
                res = response.json()

                st.session_state.chat.append(("user", res["user_text"]))
                st.session_state.chat.append(("ai", res["ai_question"]))

                # Clear last text after sending
                st.session_state.last_text = None

            else:
                st.error("API Error")

    st.divider()

    # ------------------ CHAT ------------------
    st.subheader("💬 Conversation")

    for role, msg in st.session_state.chat:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

    # ------------------ TEXT INPUT ------------------
    user_input = st.chat_input("Type your response here...")

    if user_input:
        st.session_state.last_text = user_input
        st.session_state.chat.append(("user", user_input))

        response = requests.post(
            f"{API_URL}/voice-input",
            data={"text": user_input}
        )

        if response.status_code == 200:
            res = response.json()
            st.session_state.chat.append(("ai", res["ai_question"]))
        else:
            st.error("API Error")

        st.rerun()


# ------------------ RIGHT PANEL ------------------
with col2:
    st.subheader("📝 Essay Structure")

    if st.button("Generate Essay"):
        response = requests.get(f"{API_URL}/generate-essay")

        if response.status_code == 200:
            essay = response.json()["essay_structure"]
            st.session_state["essay"] = essay
        else:
            st.error("Failed to generate essay")

    if "essay" in st.session_state:
        st.markdown(st.session_state["essay"])