import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  
  useEffect(() => {
    const intervalID = setInterval(() => {
    fetch('/temp').then(res => res.json()).then(data => {
      setCurrentTime(data.temp);
    });
  }, 60000)
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
        <p>The current temperature is {currentTime} °F.</p>
      </header>
    </div>
  );
}

export default App;