import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signUp } from './api'; // API function to handle signup

function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await signUp(email, password);
    if (success) {
      navigate.push('/login');
    } else {
      // Here we need to Handle signup failure
    }
  };

  return (
    <div>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
        <button type="submit">Signup</button>
      </form>
    </div>
  );
}

export default Signup;
