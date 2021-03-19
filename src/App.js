import React, {useState} from 'react';
import { ReactComponent as CloseMenu } from "./x.svg";
import { ReactComponent as MenuIcon } from "./menu.svg";
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import './App.css';
import Dashboard from './Dashboard';
import Temp from './Temp';
import Download from './Download'
import About from './About'
import NoMatchPage from './NoMatchPage'

const App = () => {
  const [click, setClick] = useState(false);
  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);
    return (
      <Router>
        <div className="App">
          <ul className={click ? "nav-options active" : "nav-options"} id="navigation">
            <li className="option" onClick={closeMobileMenu}>
              <Link to={'/'} className="nav-link"> Home </Link></li>
            <li className="option" onClick={closeMobileMenu}>
              <Link to={'/about'} className="nav-link"> About </Link></li>
            <li className="option" onClick={closeMobileMenu}>
              <Link to={'/dashboard'} className="nav-link"> Dashboards </Link></li>
            <li className="option" onClick={closeMobileMenu}>
              <Link to={'/download'} className="nav-link"> Download </Link></li>
          </ul>
          <Switch>
            <Route exact path='/' component={Temp}/>
            <Route path='/about' component={About}/>
            <Route path='/dashboard' component={Dashboard}/>
            <Route path='/download' component={Download}/>
            <Route component={NoMatchPage} />
          </Switch>
        </div>
        <div className="mobile-menu" onClick={handleClick}>
          {click ? (
            <CloseMenu className="menu-icon" />
          ) : (
            <MenuIcon className="menu-icon" />
          )}
        </div>
      </Router>
    );
}

export default App;