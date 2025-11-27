
# SPARK — Career Mentor Platform

SPARK is a comprehensive career mentorship platform built using **Flask (Python)**.
It provides resume analysis, AI-powered quizzes, domain roadmaps, and personalized career insights.
The platform also includes **Sparky**, an AI chatbot powered by **Groq API** for real-time guidance.

---

## Overview

SPARK includes the following major modules:

* **Resume Analysis** using Groq LLaMA 3.1B-Instant + Gemini API
* **AI-Based Domain Quiz** (24 domains, 3 difficulty levels)
* **26 Complete Career Roadmaps**
* **Sparky Chatbot (Groq API)**
* **User Login System**
* **Modern HTML/CSS/JS Frontend**

---

## ✨ Features

### 🧾 Resume Analysis

**ATS Score (Groq API)**

* Model: **LLaMA 3.1B-Instant**
* Evaluates keyword match, resume structure, job-role alignment, and skills

**AI-Powered Suggestions (Gemini API)**

* Advice is provided to user for itsbetterment

**Course Suggestions (Gemini API)**

* Based on analysing the resume 

**Project Recommendations**

* Recommeneded on the basis of user job description and resume analysis

**Job Openings**

* Currently active job openings on various platforms

---

## 🧠 AI Domain Quiz (24 Domains)

### Powered by Gemini API

Automatically generates domain-specific quizzes.

### Difficulty Levels

* **Easy** → MCQ + MSQ
* **Medium** → MCQ + MSQ + Numeric
* **Hard** → MSQ + Coding Questions

### Question Types

* MCQ
* MSQ
* Numerics
* Coding Problems (Hard level)

### Domain Output

* Quiz Result
* Every Question description is provided

---

## 🛣️ 26 Career Roadmaps

Each roadmap includes:

* Step-by-step learning path
* Tools & technologies to master
* Recommended courses & resources
* Portfolio project ideas
* Certifications

---

## 🤖 Sparky — AI Chatbot (Groq API)

Sparky helps users with:

* Career questions
* Roadmap guidance
* Technology updates

Powered by **Groq API** for fast and accurate responses.

---

## 📦 Project Structure

```plaintext
Carrier_Catalyst/
│
├── backend/
│   ├── webpage.py            # Main Flask application
│   ├── ats.py                # Groq ATS using LLaMA 3.1B-Instant
│   ├── quiz.py               # Gemini-powered domain quiz
│   ├── roadmap.py            # 26-domain roadmap generator
│   ├── auth.py               # Login/auth system
│   ├── feedback.py           # Gemini-powered resume advice
│
├── templates/
│   ├── webpage.html
│   ├── login.html
│   ├── quiz.html
│   ├── jobs.html
│   ├── feedback.html
│   ├── roadmaps/
       ├──Data_scientist.html
       ├── many more ....

├── static/
│   └── images/
|
├──Roadmps/
   ├── Data_scientist.py
   ├── many more...

```

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone git clone https://github.com/Sujal-Core/SPARK.git
cd SPARK
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Option A — Flask CLI

Windows:

```bash
set FLASK_APP=backend.webpage
flask run
```

macOS/Linux:

```bash
export FLASK_APP=backend.webpage
flask run
```

### Option B — Direct run

```bash
python backend/webpage.py
```

### Option C — Using run.py

```bash
python run.py
```

---

## 🔧 Dependencies

* Flask
* python-dotenv
* requests
* Groq API (LLaMA 3.1B-Instant)
* Gemini API
* pdfminer / python-docx

---

## 📄 License

Licensed under **GNU AGPLv3**, requiring:

* Attribution
* Open-source continuation
* No closed-source redistribution

---

## 👤 Author

**Sujal**
Developer | AI & ML Enthusiast


