# Real-Time AI Intelligence Agent 🚀

It is a high-performance, reactive RAG (Retrieval-Augmented Generation) system built for the **Synaptix Frontier AI Hackathon**. By combining Pathway's streaming data engine with Google Gemini 1.5 Flash, Synaptix provides an agent that stays updated with live data—no manual re-indexing required.

---

## 🌟 Problem
Traditional LLMs and RAG systems suffer from a **knowledge cutoff**. When files change or new data arrives, developers often have to rebuild vector indexes or restart services. This creates a lag in decision-making for high-stakes industries like Finance and Healthcare.

---

## 💡 Solution
It uses Pathway to create a live streaming pipeline that monitors local directories. As soon as a `.txt` file is added or edited, the context is instantly updated and available for **Gemini 1.5 Flash** to reason over.

---

## 🛠️ Tech Stack
- **AI Model:** Google Gemini 1.5 Flash  
- **Data Engine:** Pathway  
- **Backend:** FastAPI & Uvicorn  
- **Frontend:** React & Vite  
- **Security:** `python-dotenv` for environment variable management  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/harivenkat06/synaptix-frontier-ai-hack.git
cd synaptix-frontier-ai-hack
```
### 2️⃣ Setup Backend
```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create a .env file (copy from example and add your API key)
cp .env.example .env

# Run the backend server
uvicorn app:app --reload
```
### 3️⃣ Setup Frontend
```bash
cd ../frontend

# Install Node.js dependencies
npm install

# Start the frontend
npm run dev
```
### 4️⃣ Folder Structure
```bash
synaptix-frontier-ai-hack/
├── backend/
│   ├── app.py
│   ├── agent.py
│   ├── gemini_index.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
└── README.md
```


