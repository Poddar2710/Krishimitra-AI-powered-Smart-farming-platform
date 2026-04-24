import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyBcfDVKb6gDm3MeLj-Of2b-gPd6zn4xnWg")

st.title("🤖 KrishiMitra AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# AI function
def get_ai_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🌟 AUTO RESPONSE FROM DISEASE PAGE
if "detected_disease" in st.session_state:
    disease = st.session_state["detected_disease"]

    st.info(f"🌿 Detected Disease: {disease}")

    prompt = f"""
    Explain {disease} in simple terms for farmers.
    Include:
    - Causes
    - Symptoms
    - Treatment
    - Prevention
    """

    reply = get_ai_response(prompt)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

    del st.session_state["detected_disease"]

# User input
user_input = st.chat_input("Ask your farming question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    reply = get_ai_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)