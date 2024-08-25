import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { Header, Footer, LoginForm } from '../components';

describe('Header', () => {
  it('renders the logo', () => {
    const { getByAltText } = render(<Header />);
    expect(getByAltText('Logo')).toBeInTheDocument();
  });

  it('renders the navigation menu', () => {
    const { getByText } = render(<Header />);
    expect(getByText('Home')).toBeInTheDocument();
    expect(getByText('About')).toBeInTheDocument();
  });
});

describe('Footer', () => {
  it('renders the copyright information', () => {
    const { getByText } = render(<Footer />);
    expect(getByText('Copyright 2023')).toBeInTheDocument();
  });
});

describe('LoginForm', () => {
  it('renders the username and password fields', () => {
    const { getByPlaceholderText } = render(<LoginForm />);
    expect(getByPlaceholderText('Username')).toBeInTheDocument();
    expect(getByPlaceholderText('Password')).toBeInTheDocument();
  });

  it('calls the login function when the form is submitted', () => {
    const loginSpy = jest.fn();
    const { getByText } = render(<LoginForm login={loginSpy} />);
    const form = getByText('Login').closest('form');
    fireEvent.submit(form);
    expect(loginSpy).toHaveBeenCalledTimes(1);
  });
});
