import streamlit as st
from agents.writer_agent import run_writer_agent
from agents.editor_agent import run_editor_agent
from agents.designer_agent import run_designer_agent
from agents.narrator_agent import run_narrator_agent

st.set_page_config(page_title="AutoContentForge", layout="centered")
st.title("🧠 AutoContentForge: AI Content Factory")

with st.form("content_form"):
    topic = st.text_input("Enter blog topic:")
    submitted = st.form_submit_button("Generate Content")

if submitted and topic:
    with st.spinner("✍️ Writing article..."):
        draft = run_writer_agent(topic)
    st.subheader("📝 Draft")
    st.write(draft)

    with st.spinner("🧹 Editing article..."):
        final = run_editor_agent(draft)
    st.subheader("✅ Final Edited Version")
    st.write(final)

    with st.spinner("🎨 Creating image..."):
        image_url = run_designer_agent(topic)
    st.subheader("🖼️ Generated Image")
    st.image(image_url, caption=topic)

    with st.spinner("🔊 Narrating article..."):
        audio_path = run_narrator_agent(final)
    st.subheader("🎧 Audio Version")
    st.audio(audio_path)
