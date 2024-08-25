import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';
import Home from '../pages/Home';
import Launch from '../pages/Launch';
import Settings from '../pages/Settings';
import About from '../pages/About';

const App = () => {
  const [theme, setTheme] = useState('light');
  const [language, setLanguage] = useState('en');

  useEffect(() => {
    const storedTheme = localStorage.getItem('theme');
    const storedLanguage = localStorage.getItem('language');
    if (storedTheme) {
      setTheme(storedTheme);
    }
    if (storedLanguage) {
      setLanguage(storedLanguage);
    }
  }, []);

  const handleThemeChange = (newTheme) => {
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
  };

  const handleLanguageChange = (newLanguage) => {
    setLanguage(newLanguage);
    localStorage.setItem('language', newLanguage);
  };

  return (
    <BrowserRouter>
      <Header theme={theme} onThemeChange={handleThemeChange} />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/launch" component={Launch} />
        <Route path="/settings" component={Settings} />
        <Route path="/about" component={About} />
      </Switch>
      <Footer theme={theme} />
    </BrowserRouter>
  );
};

export default App;
