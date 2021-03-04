import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import './App.css';
import Dashboard from './Dashboard';
import Temp from './Temp';
import Download from './Download'
import About from './About'

function App() {
  return (
    <Router>
      <div className="App">
        <ul className="navigation">
          <li><Link to={'/'} className="nav-link"> Home </Link></li>
          <li><Link to={'/about'} className="nav-link"> About </Link></li>
          <li><Link to={'/dashboard'} className="nav-link"> Dashboards </Link></li>
          <li><Link to={'/download'} className="nav-link"> Download </Link></li>
        </ul>
        <Switch>
          <Route exact path='/' component={Temp}/>
          <Route path='/about' component={About}/>
          <Route path='/dashboard' component={Dashboard}/>
          <Route path='/download' component={Download}/>
        </Switch>
      </div>
    </Router>
  );
}

export default App;