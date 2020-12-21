import React from 'react';
import logo from './logo.svg';
import './App.css';
import Temp from './Temp';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div>
        <img src={logo} className="App-logo" alt="logo" />
        </div>
      </header>
      <Temp />
    </div>
  );
}

export default App;