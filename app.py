# ==================================================
# CUSTOM CSS
# ==================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f7f4ff 0%, #eef7ff 45%, #ffffff 100%);
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #4B2E83;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #555;
    margin-bottom: 25px;
}

.hero-card {
    background: white;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 8px 24px rgba(75, 46, 131, 0.12);
    border-left: 8px solid #6C4AB6;
}

.info-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.08);
    height: 100%;
}

.metric-title {
    color: #6C4AB6;
    font-size: 18px;
    font-weight: 700;
}

.answer-box {
    background: #ffffff;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e5ddff;
    box-shadow: 0 5px 18px rgba(0,0,0,0.06);
}

.source-box {
    background: #f4f0ff;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 8px;
    color: #4B2E83;
    font-weight: 600;
}

.footer {
    text-align: center;
    color: #777;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# BEAUTIFUL SIDEBAR
# ==================================================
with st.sidebar:
    st.markdown("## 📘 Project Info")
    st.markdown(f"### **{GROUP_NO}**")

    st.divider()

    st.markdown("### 👥 Group Members")
    for member in GROUP_MEMBERS:
        st.markdown(f"**{member['student_id']}**  \n{member['name']}")

    st.divider()

    st.markdown("### 💡 Example Questions")
    st.markdown("""
    - ทุนประเภท 1 กับ 2 ต่างกันอย่างไร  
    - ได้เงินสนับสนุนเมื่อไหร่  
    - ถ้าไม่ผ่านระดับดีต้องทำอย่างไร  
    - ลิขสิทธิ์กี่ปี  
    - ผู้เขียนได้ค่าลิขสิทธิ์กี่เปอร์เซ็นต์  
    """)


# ==================================================
# MAIN UI
# ==================================================
st.markdown('<div class="main-title">📚 MFU Grant Assistant using RAG</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI Chatbot สำหรับตอบคำถามเกี่ยวกับทุนตำรา หนังสือ eBook และขั้นตอนการขอรับทุน</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero-card">
<h3>🎯 Project Overview</h3>
<p>
ระบบนี้ใช้แนวคิด <b>Retrieval-Augmented Generation (RAG)</b> 
เพื่อค้นคืนข้อมูลจากเอกสาร Dataset ของทุนตำรา MFU แล้วนำข้อมูลที่เกี่ยวข้องมาตอบคำถามผู้ใช้
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="metric-title">📄 Dataset</div>
        <p>PDF, DOCX และ Infographic เกี่ยวกับทุนตำรา MFU</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="metric-title">🧠 AI Concept</div>
        <p>Document Loading, Text Splitting, Embedding และ FAISS Retrieval</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="metric-title">🚀 Deployment</div>
        <p>พัฒนา Web Application ด้วย Streamlit Cloud</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

vectorstore = create_vectorstore()

if vectorstore is None:
    st.error("ไม่พบ dataset กรุณาตรวจสอบโฟลเดอร์ dataset")
    st.stop()

st.markdown("## 🔍 Ask from Dataset")

example_questions = [
    "ทุนประเภทที่ 1 กับประเภทที่ 2 ต่างกันอย่างไร",
    "ถ้าไม่ผ่านระดับดีต้องทำอย่างไร",
    "ลิขสิทธิ์กี่ปี",
    "ผู้เขียนได้รับค่าลิขสิทธิ์กี่เปอร์เซ็นต์"
]

selected_example = st.selectbox(
    "เลือกคำถามตัวอย่าง หรือพิมพ์คำถามเองด้านล่าง",
    [""] + example_questions
)

question = st.text_input(
    "กรอกคำถามของคุณ:",
    value=selected_example,
    placeholder="เช่น ทุนประเภทที่ 1 กับประเภทที่ 2 ต่างกันอย่างไร?"
)

if question:
    with st.spinner("กำลังวิเคราะห์ข้อมูลจาก Dataset..."):
        answer, sources = get_answer(question, vectorstore)

    st.markdown("## ✅ Answer")
    st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)

    st.markdown("## 📌 Sources Used")
    unique_sources = list(set(sources))

    for src in unique_sources:
        st.markdown(f'<div class="source-box">📎 {src}</div>', unsafe_allow_html=True)

st.divider()
st.markdown(
    '<div class="footer">Developed using Vibecode + RAG + Streamlit | Business Data Analytics Project</div>',
    unsafe_allow_html=True
)
