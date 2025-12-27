// src/App.jsx
import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [chatHistory, setChatHistory] = useState([
    { role: "bot", text: "Hello! I'm your AI agent. How can I help you today?" }
  ]);
  const [loading, setLoading] = useState(false);

  const askBackend = async () => {
    if (!query.trim()) return;

    // Add user message to UI immediately
    const userMsg = { role: "user", text: query };
    setChatHistory((prev) => [...prev, userMsg]);
    setQuery("");
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();
      setChatHistory((prev) => [...prev, { role: "bot", text: data.answer }]);
    } catch (err) {
      setChatHistory((prev) => [...prev, { role: "bot", text: "❌ Connection error." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Synaptix AI</h1>
      
      <div className="chat-box">
        {chatHistory.map((msg, index) => (
          <div key={index} className={`message ${msg.role}`}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="message bot">Thinking...</div>}
      </div>

      <div className="input-area">
        <input
          type="text"
          placeholder="Ask your data..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && askBackend()}
        />
        <button onClick={askBackend} disabled={loading}>
          {loading ? "..." : "Ask"}
        </button>
      </div>
    </div>
  );
}

export default App;