import React, { useState, useEffect } from 'react';

function App() {
  const [logs, setLogs] = useState([]);

  const fetchLogs = async () => {
    try {
      // 🚀 The Magic Link: Now pointing to your Cloud Server!
      const response = await fetch('https://drowsiness-alert.vercel.app/logs');
      const data = await response.json();
      setLogs(data);
    } catch (error) {
      console.error("Database not connected yet!", error);
    }
  };

  useEffect(() => {
    fetchLogs();
    const interval = setInterval(fetchLogs, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ backgroundColor: '#282c34', minHeight: '100vh', color: 'white', padding: '50px', fontFamily: 'Arial' }}>
      <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center' }}>
        <h1 style={{ fontSize: '3rem', borderBottom: '2px solid white', paddingBottom: '20px' }}>
          🚗 Drowsiness AI Dashboard
        </h1>
        
        <h2 style={{ marginTop: '40px', color: '#61dafb' }}>Live Alerts</h2>
        
        <div style={{ backgroundColor: '#1e2126', padding: '20px', borderRadius: '10px', marginTop: '20px' }}>
          {logs.length === 0 ? (
            <p style={{ fontSize: '1.5rem', color: '#4caf50' }}>✅ Driver is awake and focused. No alerts yet!</p>
          ) : (
            <ul style={{ listStyle: 'none', padding: 0 }}>
              {logs.map((log, index) => (
                <li key={index} style={{ backgroundColor: '#ff4c4c', margin: '10px 0', padding: '15px', borderRadius: '5px', fontSize: '1.2rem', fontWeight: 'bold' }}>
                  🚨 {log.status} detected at {log.timestamp}
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;