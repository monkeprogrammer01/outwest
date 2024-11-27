import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import SuccessMessage from '../SuccessMessage'
import { h4 } from 'framer-motion/client';

function LoginForm() {
  const [user, setUser] = useState({
    email: '',
    password: '',
  });
  const [accessToken, setAccessToken] = useState()
  const [refreshToken, setRefreshToken] = useState()
  const [showSuccess, setShowSuccess] = useState(false)
  const [showError, setShowError] = useState(false)
  const [error, setError] = useState()
  const navigate = useNavigate();
  const handleChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Формирование запроса к API с данными пользователя
      const response = await axios.post(
        'http://localhost:8000/user/login/',
        { user },  // передаем данные пользователя как объект `user`
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      const { access, refresh } = response.data;
      setAccessToken(access);
      setRefreshToken(refresh);
      localStorage.setItem('access_token', access);
      setShowSuccess(true);  // Show success message
      setTimeout(() => {
      setShowSuccess(false); // Hide success message after a delay
        navigate('/user');      // Redirect to user profile
      }, 1500);  // Adjust delay as desired
      console.log(response.data, access);  // Ответ от сервера
    } catch (error) {
      setTimeout(() => {
        setShowError(true)
        setError(error.message)
      }, 1500)
      setShowError(false);
    }
  };

  return (
    <div className="container d-flex justify-content-center min-vh-100">
      <div className="card shadow" style={{ maxWidth: '400px', width: '100%' }}>
        <div className="card-body">
          <h3 className="card-title text-center mb-4">Log in</h3>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                <label htmlFor="email" className="form-label">Email</label>
                <input
                    type="email"
                    name="email"
                    className="form-control"
                    id="email"
                    placeholder="Enter your email"
                    value={user.email}
                    onChange={handleChange}
                  />
                </div>
                        <div className="mb-3">
                        <label htmlFor="password" className="form-label">Password</label>
                        <input
                            type="password"
                            name="password"
                            className="form-control"
                            id="password"
                            placeholder="Enter your password"
                            value={user.password}
                            onChange={handleChange}
                        />
                        {showError && <h6 style={{color: "red", textAlign: "center"}} >{error}</h6>}
                        </div>
                        <button type="submit" className="btn btn-success w-100">Login</button>
                    </form>
                    {showSuccess && <SuccessMessage onClose={() => setShowSuccess(false)} message={"Logged in successfully!"} />}
                    </div>
                </div>
        </div>
  );
}

export default LoginForm;

