import streamlit as st
import google.generativeai as genai

# -------------------------
# PAGE SETTINGS
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
    width:100%;
    background-color:#6C63FF;
    color:white;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background-color:#5A54E8;
}

.block-container{
    padding-top:2rem;
}

footer{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# GEMINI API
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
        "💜 Dhanya helps you learn HR, Analytics, SQL, Power BI, Interview Preparation, Resume Tips and Career Guidance."
    )

    st.markdown("---")

    st.write("Version 1.0")

    st.caption("Made with ❤️ using Streamlit & Gemini AI")

# -------------------------
# MAIN PAGE
# -------------------------

st.title("🤖 Dhanya – Your Friendly AI HR & Analytics Companion")

st.success("👋 Welcome! I'm Dhanya, your AI learning companion.")

st.info("""
### 💡 Try asking

• HR Analytics

• Recruitment Process

• SQL Joins

• Power BI Dashboard

• Employee Attrition

• Resume Tips

• Interview Preparation
""")

st.markdown("---")

# -------------------------
# INPUTS
# -------------------------

col1, col2 = st.columns(2)

with col1:

    topic = st.text_input(
        "📘 Enter your topic or question",
        placeholder="Example: Explain HR Analytics or How do I prepare for interviews?"
    )

with col2:

    option = st.selectbox(
        "✨ Choose Activity",
        (
            "Explain Concept",
            "Real-Life Example",
            "Generate Quiz",
            "Ask Anything"
        )
    )

# -------------------------
# GENERATE
# -------------------------

if st.button("🚀 Generate Answer"):

    if topic.strip() == "":

        st.warning("⚠ Please enter a topic or question.")

    else:

        if option == "Explain Concept":

            prompt = f"""
You are Dhanya – AI HR & Analytics Tutor.

Explain '{topic}' in simple English.

Use:
- Beginner-friendly language
- Short explanation
- One real-life example
- Key points
"""

        elif option == "Real-Life Example":

            prompt = f"""
Give one real-life HR or business example for:

{topic}

Explain step-by-step in simple language.
"""

        elif option == "Generate Quiz":

            prompt = f"""
Create 5 MCQs on:

{topic}

For each question include:
- Four options
- Correct answer
- Short explanation
"""

        else:

            prompt = f"""
You are Dhanya, a friendly AI HR & Analytics Companion.

Answer the user's question naturally and conversationally.

You can help with:
- HR
- HR Analytics
- Business Analytics
- SQL
- Power BI
- Excel
- Python basics
- Resume writing
- Interview preparation
- Career guidance
- Business concepts

If the user asks a greeting, greet them politely.

If the user asks a career question, provide practical guidance.

If the user asks a technical question, explain it clearly.

User Question:

{topic}
"""

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
