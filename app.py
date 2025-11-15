import os
from openai import OpenAI
import streamlit as st

# --- OpenAI API Key Setup ---
# Check for API key in environment variables or Streamlit secrets
if "OPENAI_API_KEY" not in os.environ:
    if hasattr(st, 'secrets') and 'OPENAI_API_KEY' in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    else:
        st.error("OPENAI_API_KEY environment variable or Streamlit secret not found. Please set it.")
        st.stop()

try:
    client = OpenAI()
except Exception as e:
    st.error(f"Failed to initialize OpenAI client: {e}. Please check your API key.")
    st.stop()

# --- Summarize Function ---
def summarize(text, style="simple"):
    try:
        if style == "simple":
            prompt_content = f"Summarize in simple English: {text}"
        elif style == "short":
            prompt_content = f"Summarize the following text in 3-5 lines: {text}"
        else:
            prompt_content = f"Summarize in simple English: {text}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt_content}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred during summarization: {e}"

# --- Streamlit Frontend ---
st.set_page_config(page_title="Text Summarizer", page_icon="📝")

st.title("📝Text Summarizer")
st.markdown("Enter any text below, and I'll provide a concise summary!")

# Text input area
user_input = st.text_area(
    "Enter text to summarize:",
    height=200,
    placeholder="Paste your long paragraph here..."
)

# Summarize buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Summarize Text (Simple)"):
        if user_input:
            with st.spinner("Summarizing in simple English..."):
                summary = summarize(user_input, style="simple")
                st.subheader("Summary (Simple English):")
                st.success(summary)
        else:
            st.warning("Please enter some text to summarize.")

with col2:
    if st.button("Summarize in 3-5 Lines"):
        if user_input:
            with st.spinner("Summarizing in 3-5 lines..."):
                summary = summarize(user_input, style="short")
                st.subheader("Summary (3-5 lines):")
                st.success(summary)
        else:
            st.warning("Please enter some text to summarize.")

st.markdown("---")
st.info("Powered by OpenAI's gpt-4o-mini model developed by Satyam.")
