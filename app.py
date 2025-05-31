import streamlit as st
import os
from openai import OpenAI
from elevenlabs import ElevenLabs, Voice, play

# Load secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
eleven_api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("ELEVENLABS_VOICE_ID")

eleven = ElevenLabs(api_key=eleven_api_key)

st.set_page_config(page_title="Jarvis AI Assistant", layout="centered")
st.markdown("## 🤖 Jarvis - Your Personal Assistant")

user_input = st.text_input("What can I help you with?", "")

if st.button("Ask Jarvis") and user_input:
    with st.spinner("Jarvis is thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis from Iron Man. Speak with a formal British tone."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        st.markdown(f"**Jarvis:** {reply}")

        audio = eleven.generate(text=reply, voice=Voice(voice_id=voice_id), model="eleven_multilingual_v2")
        st.audio(audio, format="audio/mp3")
