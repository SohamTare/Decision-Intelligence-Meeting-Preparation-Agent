import streamlit as st
from engine.extractor import extract_actions
from engine.decision_engine import prioritize
from engine.context_processor import enrich_context

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Meeting Preparation Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #F5F7FA;
    font-family: 'Segoe UI', sans-serif;
}

/* Remove Streamlit default padding */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 1px solid #E5E7EB;
}

/* Titles */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #6B7280;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #E5E7EB;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.04);
    margin-bottom: 18px;
}

/* Section Titles */
.section-title {
    font-size: 24px;
    font-weight: 600;
    color: #111827;
    margin-bottom: 15px;
}

/* Metric Cards */
.metric-card {
    background: #FFFFFF;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #E5E7EB;
    text-align: center;
    height: 120px;
}

/* Buttons */
.stButton>button {
    background-color: #16A34A;
    color: white;
    border-radius: 12px;
    height: 50px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    width: 100%;
}

.stButton>button:hover {
    background-color: #15803D;
    color: white;
}

/* Text Area */
textarea {
    border-radius: 12px !important;
    border: 1px solid #D1D5DB !important;
}

/* Footer */
.footer-box {
    background: #ECFDF5;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #BBF7D0;
    color: #065F46;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "assets/logo.png",
    width=180
)

st.sidebar.markdown("""
<div style="margin-top:-10px; margin-bottom:20px;">

<h2 style="
color:#111827;
font-size:28px;
margin-bottom:0px;
">
Springer Capital
</h2>

<p style="
color:#16A34A;
font-size:16px;
margin-top:0px;
font-weight:600;
">
Decision Intelligence Dashboard
</p>

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

client_type = st.sidebar.selectbox(
    "Client Type",
    ["Retail", "HNI"]
)

meeting_type = st.sidebar.selectbox(
    "Meeting Type",
    ["Portfolio Review", "Tax Planning", "General Advisory"]
)

st.sidebar.markdown("---")

st.sidebar.success("System Status: Active")
st.sidebar.info("Prototype Version: v1.0")

st.sidebar.markdown("---")
st.sidebar.caption("Internal Prototype Dashboard")

# ---------------- HEADER ---------------- #

st.markdown(
    '<div class="main-title">Decision Intelligence Meeting Preparation Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered advisor workflow prototype for meeting preparation and action prioritization</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT SECTION ---------------- #

st.markdown('<div class="card">', unsafe_allow_html=True)

notes = st.text_area(
    "Meeting Notes",
    height=180,
    placeholder="Enter advisor meeting notes, portfolio observations, or client discussion points..."
)

generate = st.button("Generate Executive Insights")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROCESSING ---------------- #

if generate:

    if notes.strip() == "":
        st.warning("Please enter meeting notes.")

    else:

        context = enrich_context(meeting_type)
        actions = extract_actions(notes)
        results = prioritize(actions, client_type)

        # ---------------- EXECUTIVE SUMMARY ---------------- #

        st.markdown(
            '<div class="section-title">Executive Summary</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"""
            <div class="metric-card">
            <h4>Advisory Focus</h4>
            <p>{context}</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="metric-card">
            <h4>Risk Signal</h4>
            <p>Moderate</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="metric-card">
            <h4>Meeting Complexity</h4>
            <p>Medium</p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown("""
            <div class="metric-card">
            <h4>Decision Readiness</h4>
            <p>82%</p>
            </div>
            """, unsafe_allow_html=True)

        # ---------------- ACTIONS ---------------- #

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            '<div class="section-title">Prioritized Actions</div>',
            unsafe_allow_html=True
        )

        for i, r in enumerate(results, 1):

            if r["priority"] == "HIGH":
                priority_color = "#DC2626"
                bg_color = "#FEF2F2"

            elif r["priority"] == "MEDIUM":
                priority_color = "#D97706"
                bg_color = "#FFFBEB"

            else:
                priority_color = "#059669"
                bg_color = "#ECFDF5"

            with st.container():

                st.markdown(f"""
                <div style="
                    background-color:white;
                    padding:22px;
                    border-radius:18px;
                    border:1px solid #E5E7EB;
                    margin-bottom:18px;
                ">
                """, unsafe_allow_html=True)

                col1, col2 = st.columns([5,1])

                with col1:
                    st.markdown(
                        f"### {i}. {r['action']}"
                    )

                with col2:
                    st.markdown(f"""
                    <div style="
                        background:{bg_color};
                        color:{priority_color};
                        padding:8px;
                        border-radius:10px;
                        text-align:center;
                        font-weight:700;
                        margin-top:10px;
                    ">
                    {r['priority']}
                    </div>
                    """, unsafe_allow_html=True)

                col3, col4 = st.columns(2)

                with col3:
                    st.markdown(
                        f"**Decision Score:** {r['score']}"
                    )

                with col4:
                    st.markdown(
                        "**Risk Classification:** Moderate"
                    )

                st.markdown("---")

                st.markdown(
                    f"**Insight Generated:** {r['reason']}"
                )

                st.markdown(
                    "**Recommended Next Step:** Advisor review and workflow confirmation recommended."
                )

                st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- FOOTER ---------------- #

        st.markdown(f"""
        <div class="footer-box">
        <b>System Insight:</b> This prototype demonstrates a decision intelligence workflow 
        for advisor meeting preparation using contextual analysis and action prioritization logic.
        </div>
        """, unsafe_allow_html=True)