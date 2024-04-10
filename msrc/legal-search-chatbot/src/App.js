import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/search', { query });
      setResults(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>LegalSearch Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your search query"
        />
        <button type="submit">Search</button>
      </form>
      <div className="results">
        {results.map((item, index) => (
          <div key={index} className="result">
            <h3>Case: {item.case_name}</h3>
            <p>Author: {item.author}</p>
            <p>Date Filed: {item.date_filed}</p>
            <p>
              URL: <a href={item.absolute_url} target="_blank" rel="noopener noreferrer">{item.absolute_url}</a>
            </p>
            <h4>Summary:</h4>
            <p>{item.summary}</p>
            <h4>Relevance:</h4>
            <p>{item.relevance}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;