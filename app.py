import streamlit as st
import os
import google.generativeai as genai
from elevenlabs import ElevenLabs, Voice, play

# === CONFIGURE GOOGLE GEMINI ===
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-pro")

# === CONFIGURE ELEVENLABS ===
eleven_api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("ELEVENLABS_VOICE_ID")
eleven = ElevenLabs(api_key=eleven_api_key)

# === STREAMLIT UI ===
st.set_page_config(page_title="Jarvis AI Assistant", layout="centered")
st.markdown("## 🤖 Jarvis - Your Personal Assistant (Gemini Powered)")

user_input = st.text_input("What would you like to ask Jarvis?", "")

if st.button("Ask Jarvis") and user_input:
    with st.spinner("Jarvis is thinking..."):
        try:
            # === GEMINI GENERATES RESPONSE ===
            response = model.generate_content(
                f"You are Jarvis from Iron Man. Speak with a formal British tone. Respond to: {user_input}"
            )
            reply = response.text
            st.markdown(f"**Jarvis:** {reply}")

            # === ELEVENLABS VOICE OUTPUT ===
            audio = eleven.generate(
                text=reply,
                voice=Voice(voice_id=voice_id),
                model="eleven_multilingual_v2"
            )
            st.audio(audio, format="audio/mp3")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
