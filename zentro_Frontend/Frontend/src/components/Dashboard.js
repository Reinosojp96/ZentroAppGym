import React, { useEffect, useState } from 'react';
import apiClient from '../services/apiClient';

export default function Dashboard() {
  const [ping, setPing] = useState('');

  useEffect(() => {
    apiClient.get('/auth/ping')
      .then(res => setPing(res.data.message))
      .catch(() => setPing('Error'));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Dashboard Zentro</h2>
      <p>Backend says: {ping}</p>
    </div>
  );
}
