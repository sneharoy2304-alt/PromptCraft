import streamlit as st
from utils.prompt_loader import load_prompt, fill_prompt

st.set_page_config(page_title="PromptCraft", page_icon="✨")
st.image("assets/banner.png", use_column_width=True)

st.title("🎨 PromptCraft")
st.subheader("🧠 A Beautiful Prompt Engineering Toolkit")

prompt_type = st.selectbox("Choose Prompt Type", ["summarization.txt", "translation.txt", "email_generator.txt"])
user_input = st.text_area("Enter your text below:", height=200)

if st.button("Generate Prompt"):
    template = load_prompt(prompt_type)
    result = fill_prompt(template, user_input)
    st.code(result, language="markdown")
