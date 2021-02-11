import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import './App.css';
import Dashboard from './dashboard';
import Temp from './Temp';

function App() {
  return (
    <Router>
      <div className="App">
        <ul className="navigation">
          <li><Link to={'/'} className="nav-link"> Home </Link></li>
          <li><Link to={'/dashboard'} className="nav-link"> Dashboard </Link></li>
          <li><Link to={'/'} className="nav-link"> Download </Link></li>
        </ul>
        <Switch>
          <Route exact path='/' component={Temp}/>
          <Route exact path='/dashboard' component={Dashboard}/>
        </Switch>
      </div>
    </Router>
    // <div className="App">
    //   <Temp />
    //   <Dashboard />
    // </div>
  );
}

export default App;