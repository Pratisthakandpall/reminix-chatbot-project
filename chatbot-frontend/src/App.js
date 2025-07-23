import React, { useState } from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [chat, setChat] = useState([]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const response = await fetch('http://localhost:5000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    });

    const data = await response.json();
    setChat([...chat, { user: input, bot: data.response }]);
    setInput('');
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
      <h2> Intelligent Chatbot</h2>
      <div style={{ border: '1px solid #ccc', borderRadius: '10px', padding: '10px', height: '300px', overflowY: 'auto', marginBottom: '10px' }}>
        {chat.map((c, i) => (
          <div key={i}>
            <p><strong>You:</strong> {c.user}</p>
            <p><strong>Bot:</strong> {c.bot}</p>
            <hr />
          </div>
        ))}
      </div>
      <input
        style={{ width: '70%', padding: '10px', borderRadius: '5px', border: '1px solid #ccc' }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
      />
      <button onClick={handleSend} style={{ marginLeft: '10px', padding: '10px 20px', borderRadius: '5px' }}>
        Send
      </button>
    </div>
  );
}

export default App;