import streamlit as st
import google.generativeai as genai

# -------------------------
# PAGE SETTINGS (Must be first Streamlit command)
# -------------------------
st.set_page_config(
    page_title="Dhanya – AI HR & Analytics Companion",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #F8F9FF;
}

.stButton>button {
    width: 100%;
    background-color: #6C63FF;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #5A54E8;
}

div[data-testid="stTextInput"] input {
    border-radius: 10px;
}

div[data-testid="stSelectbox"] {
    border-radius: 10px;
}

.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# CONFIGURE GEMINI API
# -------------------------
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:
    st.title("🤖 Dhanya")
    st.write("### AI HR & Analytics Companion")

    st.markdown("---")

    st.write("### 🌟 Features")
    st.write("✅ Explain Concepts")
    st.write("✅ Real-Life Examples")
    st.write("✅ Quiz Generation")
    st.write("✅ Ask Anything")

    st.markdown("---")

    st.info(
        "💜 Dhanya is your friendly AI companion for learning HR, Analytics, "
        "Interview Preparation, Resume Tips, and Career Guidance."
    )

# -------------------------
# MAIN PAGE
# -------------------------
st.title("🤖 Dhanya – Your Friendly AI HR & Analytics Companion")

st.success("👋 Welcome! Ask me anything about HR, Analytics, Business, Interviews, or Career Guidance.")

st.markdown("---")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input(
        "📘 Enter a Topic",
        placeholder="Example: Recruitment, HR Analytics, SQL..."
    )

with col2:
    option = st.selectbox(
        "✨ Choose Activity",
        [
            "Explain Concept",
            "Real-Life Example",
            "Generate Quiz",
            "Ask Anything"
        ]
    )

# Generate button
if st.button("✨ Generate Response"):

    if topic.strip() == "":
        st.warning("⚠ Please enter a topic.")

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
            with st.spinner("🤖 Dhanya is thinking..."):

                response = model.generate_content(prompt)

            st.markdown("## 📖 Response")
            st.write(response.text)

        except Exception:
            st.error("❌ Something went wrong. Please check your API key or try again.")

st.markdown("---")
st.caption("💜 Developed by Dhanya | AI HR & Analytics Companion")
      
       
