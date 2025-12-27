# Synaptix: Real-Time AI Intelligence Agent 🚀

**Synaptix** is a high-performance, reactive RAG (Retrieval-Augmented Generation) system built for the **Synaptix Frontier AI Hackathon**. By combining **Pathway's** streaming data engine with **Google Gemini 1.5 Flash**, Synaptix provides an agent that stays updated with live data—no manual re-indexing required.

---

## 🌟 The Problem
Traditional LLMs and RAG systems suffer from a "knowledge cutoff." When files change or new data arrives, developers often have to rebuild vector indexes or restart services. This creates a lag in decision-making for high-stakes industries like Finance and Healthcare.

## 💡 The Solution
Synaptix uses **Pathway** to create a live streaming pipeline that monitors local directories. As soon as a `.txt` file is added or edited, the context is instantly updated and available for **Gemini 1.5 Flash** to reason over.

---

## 🛠️ Tech Stack
- **AI Model:** [Google Gemini 1.5 Flash](https://aistudio.google.com/) (Chosen for its massive context window and speed)
- **Data Engine:** [Pathway](https://pathway.com/) (Used for real-time streaming data ingestion)
- **Backend:** FastAPI & Uvicorn
- **Security:** `python-dotenv` for environment variable management

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10 or higher
- A Google Gemini API Key

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/synaptix-frontier-ai.git](https://github.com/YOUR_USERNAME/synaptix-frontier-ai.git)
cd synaptix-frontier-ai/backend

# Install dependencies
pip install -r requirements.txt
