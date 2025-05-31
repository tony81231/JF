import streamlit as st
import os
import google.generativeai as genai
from elevenlabs import ElevenLabs, Voice

# Gemini setup (pick an available model name)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# ElevenLabs setup
eleven = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
voice_id = os.getenv("ELEVENLABS_VOICE_ID")

st.set_page_config(page_title="Jarvis AI Assistant", layout="centered")
st.title("🤖 Jarvis – Powered by Gemini + ElevenLabs")

user_input = st.text_input("Ask Jarvis anything:")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(user_input)
            reply = response.text
            st.markdown(f"**Jarvis:** {reply}")

            audio = eleven.generate(
                text=reply,
                voice=Voice(voice_id=voice_id),
                model="eleven_multilingual_v2"
            )
            st.audio(audio, format="audio/mp3")

        except Exception as e:
            st.error(f"❌ Error: {e}")
