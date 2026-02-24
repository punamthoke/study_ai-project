import streamlit as st
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="wide")

st.title("📚 AI-Powered Study Buddy")
st.write("Your Smart Learning Assistant 🤖")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔐 API Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- MAIN OPTIONS ----------------
option = st.selectbox(
    "Choose what you want:",
    ["Explain a Topic", "Summarize Notes", "Generate Quiz", "Create Flashcards"]
)

user_input = st.text_area("Enter your topic or notes here:", height=200)

# ---------------- FUNCTIONS ----------------
def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# ---------------- BUTTON ----------------
if st.button("Generate"):

    if not api_key:
        st.error("Please enter your API key first.")
    
    elif not user_input.strip():
        st.warning("Please enter some content.")
    
    else:
        with st.spinner("Thinking... 🤔"):
            
            if option == "Explain a Topic":
                prompt = f"Explain this topic in very simple language with examples:\n{user_input}"
                result = get_response(prompt)

            elif option == "Summarize Notes":
                prompt = f"Summarize these notes in short bullet points:\n{user_input}"
                result = get_response(prompt)

            elif option == "Generate Quiz":
                prompt = f"Create 5 multiple choice questions with answers from this topic:\n{user_input}"
                result = get_response(prompt)

            elif option == "Create Flashcards":
                prompt = f"Create flashcards (Question and Answer format) from this content:\n{user_input}"
                result = get_response(prompt)

        st.success("Done ✅")
        st.write(result)