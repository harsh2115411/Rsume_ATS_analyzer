# Smart ATS - AI-Powered Resume Matcher

## 🚀 Overview
Smart ATS is an **AI-driven Applicant Tracking System (ATS)** built with **Streamlit & Google Gemini AI**. It evaluates resumes against job descriptions, providing:
- ✅ **ATS Score** (TF-IDF + Cosine Similarity)
- ✅ **Missing Keywords** (Identifies missing skills from JD)
- ✅ **AI-Generated Profile Summary** (Summarizes candidate experience)

## 📌 Features
- **Resume & Job Description Matching** using **TF-IDF & Cosine Similarity**
- **Skill Gap Analysis** to identify missing keywords
- **Profile Summary Generation** using Google Gemini AI
- **Simple UI** built with **Streamlit**

## 🛠 Requirements & Prerequisites
### Prerequisites
- **Python 3.8+** installed on your system
- **Google Gemini API Key** (Required for AI-based features)
- **pip** (Python package manager)
- **Stable internet connection** for API requests

### Required Python Libraries
Ensure you have the following dependencies installed:
```bash
pip install streamlit google-generativeai PyPDF2 python-dotenv scikit-learn
```

## 🛠 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/smart-ats.git
   cd smart-ats
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables (Google Gemini API key required)
4. Run the application:
   ```bash
   streamlit run ATS.py
   ```

## 📜 Usage
- Upload your resume (PDF format)
- Paste the job description
- Click **Submit** to get **ATS Score, Missing Skills, and AI-Generated Summary**

## 🔮 Future Scope
- **More Intelligent Context Understanding**: Implement advanced **NLP models like BERT or SBERT** for better semantic matching.
- **Experience & Role-Based Matching**: Consider candidate **experience level and job role alignment** rather than just keyword similarity.
- **Resume Optimization Suggestions**: AI-powered suggestions to improve resume structure, formatting, and keyword density for better ATS compatibility.


