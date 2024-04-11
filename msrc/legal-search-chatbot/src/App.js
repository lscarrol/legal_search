import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [userInput, setUserInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (userInput.trim() !== '') {
      setLoading(true);
      try {
        const response = await axios.post('http://localhost:5000/api/chat', {
          userInput,
          chatHistory,
        });
        const botResponse = response.data.botResponse;
        setChatHistory([...chatHistory, { userInput, botResponse }]);
        setUserInput('');
      } catch (error) {
        console.error('Error:', error);
      }
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>LegalSearch Chatbot</h1>
      <div className="chat-container">
        {chatHistory.map((chat, index) => (
          <div key={index}>
            <p className="user-input">User: {chat.userInput}</p>
            <p className="bot-response">Bot: {chat.botResponse}</p>
          </div>
        ))}
        {loading && <p className="loading">Loading...</p>}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Type your message"
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </form>
    </div>
  );
}

export default App;