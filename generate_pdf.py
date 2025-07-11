import re
from fpdf import FPDF

resume_text = """
Md. Ariful Islam
Email: arifulislamcsecuet@gmail.com | GitHub: arifulisalm | LinkedIn: Ariful Islam

Research Interests
Machine Learning, Deep Learning, High-Performance Computing (HPC), Heterogeneous Systems, Natural Language Processing, Computer Vision, Image Processing.

Education
Bachelor of Computer Science and Engineering
Chittagong University of Engineering and Technology, Bangladesh.
Jan 2018 - Aug 2023
- GPA: 3.21/4.0
- Coursework: Computer Architecture, Artificial Intelligence, Data Structure, Algorithms, etc.

Publications
- Islam, M., Ahasan, S., Hoque, M.M: TranSenA: A Transformer-based Framework for Sentiment Analysis of Restaurant Reviews. Accepted in International Conference on Signal Processing, Information, Communication and Systems.

Research Activities
CUET NLP LAB – Research Fellow (July 2024 - Present)
- Developing a multimodal restaurant review dataset for sentiment analysis.
- Creating a generalized Bengali dataset including movie, airplane service reviews.

CUET NLP LAB – Undergraduate Researcher (Jan 2023 - June 2024)
- Built BEmoLex and BRRD datasets.
- Achieved 0.90 F1 score with deep learning models on BRRD.

Experience
Software Engineer, FSM (Frontier Semiconductor Metrology), CA (June 2023 – Present)
- Reduced wafer roughness calculation time from 8 mins to 9 sec using CUDA.
- Built MFC C++ apps and OCR tools for wafer ID tracking.

Software Engineer Intern, SELISE Digital Platforms (Oct 2022 – Nov 2022)
- Built an e-commerce site using Angular, Node.js, and MongoDB.

Test Scores
GRE: 309 (Q: 161, V: 148, AWA: 3.0) – Sept 2024
IELTS: 7 (L:7.5, R:7.5, S:6.5, W:6.0) – Nov 2024

Selected Projects
- HPC Vision System: Real-time CUDA image processing.
- Rock Paper Scissor Game: OpenCV + MediaPipe real-time hand gesture recognition.
- OCR Wafer ID: KNN-based character recognition.
- VocalShield Bangla: Whisper + custom abuse detection.
- Data Analyzer: MFC-based chart generator from CSV with PDF export.

Honors and Awards
- Merit Scholarship, CUET (2019–2024)
- HSC Talentpool Scholarship (2017), SSC (2015)
- ICPC Regional: 161st (2021), Honorable Mention (2020)
- NCPC, CodeJam (Top 40%), KickStart (Top 30%), Facebook Hacker Cup 2nd Round

Skills
- ML/DL: PyTorch, TensorFlow, Keras
- Languages: C, C++, Python, JavaScript, SQL
- Tools: CUDA, Pandas, MFC, Git, MongoDB

CP Achievements
- Solved 1200+ problems
- Codeforces: 950+, LeetCode: 350+, CodeChef: 80+

Leadership & Activities
CUET NLP Lab – Mentor: Train juniors in DL/NLP, meet bi-weekly
CUET Computer Club – Coordinator: Teach DSA, organize contests
Cumilla Student Welfare – Member: Represent students, fundraise

Workshops
- CLBLP Workshop on Bangla NLP
- AI with Python (SKBIT, CUET)
- Seminar on NLP in 4IR (SKBIT, CUET)
"""

# Step 1: Keep only A-Z, a-z, 0-9, newlines, and spaces
cleaned_text = re.sub(r"[^a-zA-Z0-9 \n]", "", resume_text)

# Step 2: Generate PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=10)

for line in cleaned_text.split('\n'):
    pdf.multi_cell(0, 10, line)

pdf.output("sample.pdf")
print("✅ PDF with only alphanumeric characters created successfully.")
