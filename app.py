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
st.info("Powered by OpenAI's gpt-4o-mini model.")
