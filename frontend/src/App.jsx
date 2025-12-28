// src/App.jsx
import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function App() {
  const [query, setQuery] = useState("");
  const [chatHistory, setChatHistory] = useState([
    { role: "bot", text: "Hello! I'm your **Synaptix** AI agent.  \nI have access to real-time data. How can I help you today?" }
  ]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  // File Upload State
  const [uploadedFiles, setUploadedFiles] = useState([]);

  // Auto-scroll to bottom
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatHistory, loading]);

  const askBackend = async () => {
    if (!query.trim()) return;

    // Add user message to UI immediately
    const userMsg = { role: "user", text: query };
    setChatHistory((prev) => [...prev, userMsg]);
    setQuery("");
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8001/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();
      setChatHistory((prev) => [...prev, { role: "bot", text: data.answer }]);
    } catch (err) {
      console.error(err);
      setChatHistory((prev) => [...prev, { role: "bot", text: "❌ **Connection error.** Please check if the backend is running." }]);
    } finally {
      setLoading(false);
    }
  };

  // File Upload Logic
  const fileInputRef = useRef(null);

  const handleFileChange = async (e) => {
    const files = Array.from(e.target.files);
    if (files.length === 0) return;

    // Trigger upload immediately
    await uploadFiles(files);

    // Reset input
    if (fileInputRef.current) fileInputRef.current.value = "";
  };

  const uploadFiles = async (files) => {
    const formData = new FormData();
    files.forEach(file => {
      formData.append("files", file);
    });

    try {
      const response = await fetch("http://localhost:8001/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Upload failed");

      const data = await response.json();

      // Update state with new files for display
      const newFiles = files.map(f => ({
        name: f.name,
        type: f.name.split('.').pop().toUpperCase()
      }));
      setUploadedFiles(prev => [...prev, ...newFiles]);

    } catch (err) {
      console.error(err);
      // Optional: Handle error visual if needed, but Toast is removed as requested
    }
  };

  const removeFile = (indexToRemove) => {
    setUploadedFiles(prev => prev.filter((_, index) => index !== indexToRemove));
  };

  return (
    <div className="container">
      <h1>Synaptix AI</h1>

      <div className="chat-box">
        {chatHistory.map((msg, index) => (
          <div key={index} className={`message ${msg.role}`}>
            {msg.role === 'bot' ? (
              <ReactMarkdown remarkPlugins={[remarkGfm]}>{msg.text}</ReactMarkdown>
            ) : (
              msg.text
            )}
          </div>
        ))}

        {loading && (
          <div className="message bot">
            <div className="typing-indicator">
              <div className="dot"></div>
              <div className="dot"></div>
              <div className="dot"></div>
            </div>
          </div>
        )}
        <div ref={chatEndRef} />
      </div>

      <div className="input-area">
        {/* Uploaded File Cards */}
        {uploadedFiles.length > 0 && (
          <div className="file-preview-list">
            {uploadedFiles.map((file, idx) => (
              <div key={idx} className="file-card">
                <div className="file-icon-wrapper">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="file-icon">
                    <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
                    <polyline points="13 2 13 9 20 9"></polyline>
                  </svg>
                </div>
                <div className="file-info">
                  <span className="file-name">{file.name}</span>
                  <span className="file-type">{file.type}</span>
                </div>
                <button
                  className="remove-file-btn"
                  onClick={() => removeFile(idx)}
                  title="Remove file"
                >
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                  </svg>
                </button>
              </div>
            ))}
          </div>
        )}

        {/* Hidden File Input */}
        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileChange}
          multiple
          accept=".txt,.pdf,.jpg,.jpeg,.png,.md,.csv"
          style={{ display: "none" }}
        />

        <div className="input-controls">
          {/* Plus Button */}
          <button
            className="plus-btn"
            onClick={() => fileInputRef.current?.click()}
            title="Upload files"
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>

          <input
            type="text"
            placeholder="Ask about news, transactions, or earning calls..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && !loading && askBackend()}
            disabled={loading}
          />
          <button onClick={askBackend} disabled={loading || !query.trim()}>
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;