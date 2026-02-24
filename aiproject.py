import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Fitness Planner", page_icon="🏋️", layout="wide")

st.title("🏋️ Personalized Workout & Diet Planner with AI")
st.write("Get customized fitness and meal plans based on your needs 💪")

# Sidebar API
st.sidebar.header("🔐 API Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)

        # ✅ FIXED MODEL (important)
        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        st.sidebar.success("API Connected ✅")
    except Exception as e:
        st.sidebar.error("Invalid API Key ❌")
        st.stop()
else:
    st.sidebar.warning("Please enter your API key to continue")
    st.stop()

# User inputs
st.header("👤 Enter Your Details")

age = st.number_input("Age", min_value=10, max_value=80)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Stay Fit"])
diet_type = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])
budget = st.selectbox("Budget Level", ["Low Budget", "Medium Budget", "High Budget"])
workout_place = st.selectbox("Workout Location", ["Home", "Gym"])
health_issues = st.text_area("Any Health Issues? (Optional)")

if st.button("Generate Plan 💪"):
    with st.spinner("Creating your personalized fitness plan..."):

        prompt = f"""
        Create a personalized weekly workout and diet plan.

        Age: {age}
        Gender: {gender}
        Goal: {goal}
        Diet Type: {diet_type}
        Budget: {budget}
        Workout Location: {workout_place}
        Health Issues: {health_issues}

        Requirements:
        - Student friendly
        - Indian foods
        - Budget friendly
        - Weekly workout schedule
        - 7 day meal plan
        - Simple explanation
        """

        try:
            response = model.generate_content(prompt)
            st.success("Your Personalized Plan is Ready ✅")
            st.write(response.text)

        except Exception as e:
            st.error("Error occurred ❌")
            st.code(str(e))