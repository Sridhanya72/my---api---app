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
    border-radius: 12px;
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

.block-container {
    padding-top: 2rem;
}

footer {
    visibility: hidden;
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
    st.write("📘 Explain Concepts")
    st.write("💼 Real-Life Examples")
    st.write("📝 Generate Quiz")
    st.write("💬 Ask Anything")

    st.markdown("---")

    st.info(
        "💜 Dhanya helps you learn HR, Analytics, Business Concepts, Interview Preparation, Resume Tips, and Career Guidance."
    )

    st.markdown("---")

    st.write("### ℹ️ Version")
    st.write("Version 1.0")

    st.caption("Made with ❤️ using Streamlit & Gemini AI")

# -------------------------
# MAIN PAGE
# -------------------------
st.title("🤖 Dhanya – Your Friendly AI HR & Analytics Companion")

st.success("👋 Welcome! I'm Dhanya, your AI learning companion.")

st.info("""
### 💡 Try asking:
- HR Analytics
- Recruitment Process
- SQL Joins
- Power BI Dashboard
- Employee Attrition
- Resume Tips
- Interview Preparation
""")

st.markdown("---")

# -------------------------
# INPUT SECTION
# -------------------------
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input(
        "📘 Enter a Topic",
        placeholder="Example: HR Analytics, SQL, Power BI, Recruitment..."
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

st.markdown("")

# -------------------------
# GENERATE BUTTON
# -------------------------
if st.button("🚀 Generate Answer"):

    if topic.strip() == "":
        st.warning("⚠ Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"""
You are Dhanya – AI HR & Analytics Tutor.

Explain '{topic}' in simple language suitable for a beginner.

Use:
- Simple explanation
- One real-life analogy
- Short and clear points
"""

        elif option == "Real-Life Example":
            prompt = f"""
Give one real-life HR or business example of '{topic}'.

Explain it step by step using simple English.
"""

        elif option == "Generate Quiz":
            prompt = f"""
Create 5 multiple-choice questions on '{topic}'.

Include:
- Four options
- Correct answer
- Short explanation
"""

        else:
           prompt = f"""
        try:

            with st.spinner("🤖 Dhanya is preparing your answer..."):

                response = model.generate_content(prompt)

            st.markdown("---")
            st.subheader("💡 Dhanya's Response")

            st.success(response.text)

        except Exception:
            st.error("❌ Something went wrong. Please check your API key or try again.")

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")

st.caption("💜 Developed by Dhanya")
st.caption("🤖 Powered by Google Gemini AI")
st.caption("© 2026 | AI HR & Analytics Companion")
       
