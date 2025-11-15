import os

if "OPENAI_API_KEY" not in os.environ:
    # Try to load from Streamlit secrets if running on Streamlit Cloud or locally with .streamlit/secrets.toml
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

def summarize(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Summarize in simple English: {text}"}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred during summarization: {e}"


import streamlit as st
st.set_page_config(page_title="Text Summarizer", page_icon="📝")

st.title("📝Text Summarizer")
st.markdown("Enter any text below, and I'll provide a concise summary in simple English!")

# Text input area
user_input = st.text_area(
    "Enter text to summarize:",
    height=200,
    placeholder="Paste your long paragraph here..."
)

# Summarize button
if st.button("Summarize Text"):
    if user_input:
        with st.spinner("Summarizing..."):
            summary = summarize(user_input)
            st.subheader("Summary:")
            st.success(summary)
    else:
        st.warning("Please enter some text to summarize.")

st.markdown("---")
st.info("Powered by OpenAI's gpt-4o-mini model developed by Satyam.")
