import streamlit as st
import pandas as pd
import genai
import agentic_ai
import capstone

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Portfolio", layout="wide")

# ---------- CUSTOM STYLING ----------
st.markdown("""
    <style>
        .main-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.7rem 1.5rem;
            background-color: #0e1117;
            border-bottom: 1px solid #333;
        }
        .left-menu {
            display: flex;
            gap: 2rem;
        }
        .menu-item {
            font-weight: 600;
            color: #f0f0f0;
            cursor: pointer;
            text-decoration: none;
            transition: 0.2s;
        }
        .menu-item:hover {
            color: #00b4d8;
        }
        .active {
            color: #00b4d8;
            text-decoration: underline;
        }
        .right-menu {
            font-weight: 600;
            color: #f0f0f0;
            cursor: pointer;
            transition: 0.2s;
        }
        .right-menu:hover {
            color: #00b4d8;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "selected" not in st.session_state:
    st.session_state.selected = "GenAI"

def select_page(page):
    st.session_state.selected = page
    st.rerun()

# ---------- HEADER ----------
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 6])
with col1:
    if st.button("GenAI"):
        select_page("GenAI")
with col2:
    if st.button("Agentic AI"):
        select_page("Agentic AI")
with col3:
    if st.button("Capstone"):
        select_page("Capstone")
with col5:
    right_col = st.columns([10, 1])[1]
    with right_col:
        if st.button("Profile"):
            select_page("Profile")

st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #0e1117;
        color: white;
        border: none;
        font-weight: 600;
        font-size: 15px;
        cursor: pointer;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        color: #00b4d8;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- PAGE CONTENT ----------
if st.session_state.selected == "GenAI":
    genai.show()

elif st.session_state.selected == "Agentic AI":
    agentic_ai.show()

elif st.session_state.selected == "Capstone":
    capstone.show()

elif st.session_state.selected == "Profile":
    st.header("👤 Anand Bapi Raju — Portfolio")
    st.markdown("### Role: Gen AI Developer | Experience: 2+ years")
    st.markdown("---")

    # Profile sections
    st.subheader("💡 About Me")
    st.write("""
    I'm an **AI/ML Engineer** passionate about designing and developing intelligent, scalable, and production-ready AI solutions.
    My expertise spans **machine learning, deep learning, generative AI, and agentic AI**, with hands-on experience building end-to-end AI systems and pipelines.
    """)

    st.subheader("🧠 Core Competencies & Technical Expertise")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Machine Learning & Deep Learning**
        - Algorithms: Linear/Logistic Regression, Decision Trees, Random Forest, XGBoost, SVM, K-Means, Neural Networks, CNNs, RNNs, Transformers  
        - Frameworks: scikit-learn, PyTorch  
        - Full ML lifecycle: data preprocessing → feature engineering → model deployment  
        """)

        st.markdown("""
        **Backend & API Development**
        - FastAPI for production-grade APIs  
        - Docker for containerization and reproducibility
        """)

        st.markdown("""
        **Frontend & Prototyping**
        - Streamlit & Reflex for interactive dashboards, chatbots  
        - Seaborn for data visualization
        """)

    with col2:
        st.markdown("""
        **Generative AI & LLMs**
        - LLMs: OpenAI GPT, Hugging Face Transformers  
        - RAG: FAISS, Pinecone  
        - Prompt Engineering, Fine-tuning, Evaluation  
        - Agentic AI: ReAct, Tool Use, Multi-step Reasoning, Planning
        """)

        st.markdown("""
        **Data & Databases**
        - MongoDB, PostgreSQL  
        - Vector Databases for RAG/AI retrieval
        """)

        st.markdown("""
        **Cloud & MLOps**
        - AWS (S3, EC2, Lambda)  
        - CI/CD pipelines, Model Monitoring, and Deployment Automation
        """)

    st.markdown("---")
    st.success("✅ Portfolio organized and ready to add your projects dynamically!")

