import React, { useState, useEffect } from 'react';
import UserImage from '/Users/arsensejtkaliev/PycharmProjects/pythonProject1/out_west_frontend/west/src/icons/default-image.jpeg'
import './css/profile.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import ErrorMessage from '../ErrorMessage'

export default function Profile(){
    const [user, setUser] = useState({});
    const [error, setError] = useState();
    const token = localStorage.getItem('access_token');
    const [showMessage, setShowMessage] = useState(false)
    const navigate = useNavigate()
    useEffect(() => {
      if (!token) {
        setShowMessage(true)
        setTimeout(() => {
            setShowMessage(false); 
            navigate('/user/login');      // Redirect to login page
            }, 1500);
          console.log("No token found");
          
          return;
      }

      axios.get('http://localhost:8000/user/profile/', {
          headers: {
              'Authorization': `Bearer ${token}`
          }
      })
      .then(response => {
          console.log(response.data);
          
          setUser(response.data); // Save the data in state
          
      })
      .catch(error => {
          console.error(error);
      });
  }, [token]);
    return <> 
    <div className="user-info">
        <div className="user-image"><a><img src={UserImage}  id="profile" /></a></div>
        
        <div className="line" ></div>

        <div className="user-data">
            <h5>{user.email}</h5>
            <h5>18 products selected</h5>
        </div>

        <div className="line" ></div>
        <div>
            <button onClick={logout} className="btn btn-danger" >Log out</button>
        </div>
        </div>
        {showMessage && <ErrorMessage onClose={() => setShowMessage(false)} message="You are not logged in!" />}
    </>
}

const logout = () => {
    // Remove the token from localStorage or sessionStorage
    localStorage.removeItem('access_token'); // Or use sessionStorage.removeItem('token')
  
    // Redirect to the login page or any other route
    window.location.href = '/user/login'; // or use react-router navigate() method
  };