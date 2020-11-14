import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTempNA, setCurrentTempNA] = useState(0);
  const [currentTempSA, setCurrentTempSA] = useState(0);

  const [NorthArr, setNorthArr] = useState([])
  const [SouthArr, setSouthArr] = useState([])
  
  useEffect(() => {
    setInterval(() => {
    fetch('/api/tempArray').then(res => res.json()).then(data => {
      setNorthArr(data.North);
      setSouthArr(data.South);
    });
  }, 60000)
  }, []);

  useEffect(() => {
    setInterval(() => {
    fetch('/api/temp').then(res => res.json()).then(data => {
      setCurrentTempNA(data.temp1);
      setCurrentTempSA(data.temp2);
    });
  }, 60000)
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <body className="App-body">
        <p>North air temperature: {currentTempNA}°F.</p>
        <p>South air temperature: {currentTempSA}°F.</p>
        
      </body>
    </div>
  );
}

export default App;