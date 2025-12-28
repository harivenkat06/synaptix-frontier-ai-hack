# Synaptix AI - Real-Time Intelligence Agent 🚀

Synaptix is a high-performance, reactive **RAG (Retrieval-Augmented Generation)** system built for the **Synaptix Frontier AI Hackathon**. By combining **Pathway's streaming data engine** with **Google Gemini 1.5 Flash**, Synaptix provides an agent that stays updated with live data—no manual re-indexing required.

---

## 🌟 Problem
Traditional LLMs and RAG systems suffer from a **knowledge cutoff**. When files change or new data arrives, developers often have to rebuild vector indexes or restart services. This creates a lag in decision-making for high-stakes industries like Finance and Healthcare.

---

## 💡 Solution
Synaptix uses Pathway to create a live streaming pipeline that monitors local directories. As soon as a `.txt` or `.pdf` file is added or edited, the context is instantly updated and available for **Gemini 1.5 Flash** to reason over.

---

## ✨ Features

- **⚡ Real-Time Knowledge**: Uses Pathway to monitor a data folder; as soon as you drop a file, the AI learns it instantly.
- **🧠 Smart Fallback**: Answers from your documents first. If the info isn't there, it gracefully falls back to general knowledge.
- **📁 Multi-Modal Support**: 
    - **Text Documents** (`.txt`, `.md`, `.csv`)
    - **PDFs** (Automatic extraction)
    - **Images** (Visual analysis and description)
- **🎨 Elegant UI**: A modern, dark-themed React interface with:
    - Integrated **File Upload Cards**.
    - Markdown rendering for rich chat responses.
    - Smooth animations and user feedback.

---

## 📸 Demo & Screenshots

### 1. Modern Chat Interface
A clean, glassmorphism-inspired UI designed for focus.

<img width="1917" height="967" alt="image" src="https://github.com/user-attachments/assets/1a8fac10-7e6d-42c2-9bd3-39787be5f464" />


### 2. Seamless File Uploads
Upload multiple files (PDFs, Images, Text) using the **"+" button**. Files appear as interactive cards instantly.

<img width="1917" height="967" alt="image" src="https://github.com/user-attachments/assets/8c3632a0-917b-4b7f-8c42-49cafa6dff1e" />

 ### 3. Dynamic Data Update 
 Initial State:
 
<img width="313" height="84" alt="Screenshot from 2025-12-28 14-00-07" src="https://github.com/user-attachments/assets/fb2c4331-9487-4899-ba5a-34e8f80ecd51" />

Result
<img width="1920" height="971" alt="Screenshot from 2025-12-28 14-00-49" src="https://github.com/user-attachments/assets/cd071e75-e697-48ab-8c61-74a35a0100a8" />

Updated State:

<img width="304" height="84" alt="Screenshot from 2025-12-28 14-02-06" src="https://github.com/user-attachments/assets/bd54f2bc-a858-4525-a0bb-f6372ac24db9" />

Result
<img width="1920" height="962" alt="Screenshot from 2025-12-28 14-02-35" src="https://github.com/user-attachments/assets/13101126-314e-4f11-bd2f-017a338b4bfe" />




 

---

## 🛠️ Tech Stack

- **AI Model:** Google Gemini 1.5 Flash
- **Data Engine:** Pathway (Live Streaming RAG)
- **Backend:** FastAPI & Python
- **Frontend:** React, Vite & CSS Modules
- **Security:** Environment variable management

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/harivenkat06/synaptix-frontier-ai-hack.git
cd synaptix-frontier-ai-hack
```

### 2️⃣ Setup Backend
The backend handles the AI logic and file processing.

```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create a .env file
# Add your GEMINI_API_KEY inside this file
cp .env.example .env

# Run the backend server
python app.py
```
*Server will run on `http://localhost:8001`*

### 3️⃣ Setup Frontend
The frontend provides the interactive chat experience.

```bash
cd ../frontend

# Install Node.js dependencies
npm install

# Start the frontend
npm run dev
```
*Open `http://localhost:5173` in your browser.*

---

## 💡 How to Use

1.  **Ask Questions**: Type any query in the chat bar.
    *   *Example:* "What is the capital of France?" (General Knowledge)
    *   *Example:* "Summarize the weather report?" (Context from file)
2.  **Upload Data**: 
    *   Click the **(+)** button on the bottom left.
    *   Select one or more files (PDF, Text, Images).
    *   See them appear as cards above the input.
    *   Ask a question related to them immediately!

---

## 📂 Project Structure
```bash
synaptix-frontier-ai-hack/
├── backend/
│   ├── app.py             # FastAPI entry point
│   ├── agent.py           # Gemini interaction logic
│   ├── gemini_index.py    # Pathway RAG pipeline
│   └── data/              # Live monitored data folder
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # Main UI Logic
│   │   └── index.css      # Styling (Glassmorphism & Layout)
└── screenshots/           # Demo images
```


