import React from 'react';
import ReactDOM from 'react-dom';
import App from '../App';
import { render, fireEvent, waitFor } from '@testing-library/react';

describe('App', () => {
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<App />, div);
  });

  it('displays the login form', () => {
    const { getByText } = render(<App />);
    expect(getByText('Login')).toBeInTheDocument();
  });

  it('calls the login function when the form is submitted', () => {
    const loginSpy = jest.fn();
    const { getByText } = render(<App login={loginSpy} />);
    const form = getByText('Login').closest('form');
    fireEvent.submit(form);
    expect(loginSpy).toHaveBeenCalledTimes(1);
  });

  it('displays an error message when the login fails', async () => {
    const loginSpy = jest.fn(() => Promise.reject(new Error('Invalid credentials')));
    const { getByText } = render(<App login={loginSpy} />);
    const form = getByText('Login').closest('form');
    fireEvent.submit(form);
    await waitFor(() => getByText('Invalid credentials'));
    expect(getByText('Invalid credentials')).toBeInTheDocument();
  });
});
