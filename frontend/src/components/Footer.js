import React from 'react';

const Footer = ({ theme }) => {
  return (
    <footer className={`footer ${theme}`}>
      <p>&copy; 2023 PiMainNet Launcher (PMNL)</p>
    </footer>
  );
};

export default Footer;
