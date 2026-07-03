import streamlit as st
import google.generativeai as genai

# -------------------------
# CONFIGURE GEMINI API
# -------------------------
genai.configure(api_key=st.secrets[""])

model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------
# PAGE SETTINGS
# -------------------------
st.set_page_config(
    page_title="Dhanya – AI HR & Analytics Companion",
    page_icon="🎓"
)

st.title("Dhanya – Your Friendly AI HR & Analytics Companion")

# -------------------------
# USER INPUT
# -------------------------
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    ["Explain Concept", "Real-Life Example", "Generate Quiz", "Ask Anything"]
)

# -------------------------
# GENERATE BUTTON
# -------------------------
if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"""
You are Dhanya – AI HR & Analytics Tutor.
Explain '{topic}' in simple language for a beginner.
Use one real-life analogy.
Keep it short and clear.
"""

        elif option == "Real-Life Example":
            prompt = f"""
Give one real-life HR or business example of '{topic}'.
Explain step by step in simple words.
"""

        elif option == "Generate Quiz":
            prompt = f"""
Create 5 MCQs on '{topic}' with answers and explanations.
"""

        else:
            prompt = topic

        try:
            response = model.generate_content(prompt)
            st.write(response.text)

        except Exception as e:
            st.error("Something went wrong. Please check API key or try again.")
