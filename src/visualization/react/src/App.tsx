import React, {useState, useEffect} from 'react';
import './App.css';
import AppLayout from './layout/AppLayout';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => {
    fetch("/time").then(res => res.json().then(data => {
      setCurrentTime(data.time);
    }));
  }, []);
  return (
    <div className="App">
      <AppLayout/>
    </div>
  );
}

export default App;
