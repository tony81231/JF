import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Gemini Model Check", layout="centered")
st.title("🔍 Gemini API Test")

# Load your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.markdown("### 📡 Checking available Gemini models...")

try:
    models = genai.list_models()
    found_gemini = False

    for model in models:
        st.write(f"• `{model.name}`")
        if "gemini-pro" in model.name:
            found_gemini = True

    if found_gemini:
        st.success("✅ Gemini Pro is available. You're good to go!")
    else:
        st.warning("⚠️ Gemini Pro is NOT listed. You may have limited access.")

except Exception as e:
    st.error(f"❌ Failed to list models: {e}")
