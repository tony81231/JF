import streamlit as st
import os
import google.generativeai as genai
from elevenlabs import ElevenLabs, Voice

# === CONFIGURE GEMINI ===
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-pro")

# === CONFIGURE ELEVENLABS ===
eleven = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
voice_id = os.getenv("ELEVENLABS_VOICE_ID")

# === STREAMLIT UI ===
st.set_page_config(page_title="Jarvis AI Assistant", layout="centered")
st.markdown("## 🤖 Jarvis - Your Personal Assistant (Gemini + ElevenLabs)")

user_input = st.text_input("🗨️ What would you like to ask Jarvis?")

if st.button("Ask Jarvis") and user_input:
    with st.spinner("🧠 Jarvis is thinking..."):
        try:
            # === GENERATE TEXT WITH GEMINI ===
            response = model.generate_content(
                f"You are Jarvis from Iron Man. Respond with formal British tone. User asked: {user_input}"
            )
            reply = response.text
            st.markdown(f"**Jarvis:** {reply}")

            # === GENERATE VOICE WITH ELEVENLABS ===
            audio = eleven.generate(
                text=reply,
                voice=Voice(voice_id=voice_id),
                model="eleven_multilingual_v2"
            )
            st.audio(audio, format="audio/mp3")

        except Exception as e:
            st.error(f"❌ Error: {e}")
