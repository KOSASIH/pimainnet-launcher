import React from 'react';
import { Link } from 'react-router-dom';

const Header = ({ theme, onThemeChange }) => {
  return (
    <header className={`header ${theme}`}>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/launch">Launch</Link>
          </li>
          <li>
            <Link to="/settings">Settings</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>
      <div className="theme-switcher">
        <button onClick={() => onThemeChange('light')}>Light</button>
        <button onClick={() => onThemeChange('dark')}>Dark</button>
      </div>
    </header>
  );
};

export default Header;
