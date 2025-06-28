import React, { useState } from 'react';
import apiClient from '../services/apiClient';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      // Example authentication endpoint
      const response = await apiClient.post('/auth/login', { email, password });
      const token = response.data.access_token;
      localStorage.setItem('token', token);
      apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      navigate('/dashboard');
    } catch (error) {
      setMessage('Login failed');
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: 'auto', padding: '2rem' }}>
      <h2>Login Zentro</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>Email:</label><br/>
          <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
        </div>
        <div>
          <label>Password:</label><br/>
          <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
        </div>
        <button type="submit">Ingresar</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
