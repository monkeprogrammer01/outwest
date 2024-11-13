import React, { useState } from  'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios'
import SuccessMessage from '../SuccessMessage.js'
import { useNavigate } from 'react-router-dom';
import ErrorMessage from '../ErrorMessage.js';

export default function Form(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState(null)     
    const [showSuccess, setShowSuccess] = useState(false)
    const [showError, setShowError] = useState(false)
    const navigate = useNavigate();
    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (password !== confirmPassword){
            setError("Password does not match")
            setTimeout(() => {
                setError("");
              }, 3000);
            return;
        }

        const userData = {
            "user": {
                email: email,
                password: password,
            }
        }

        try{
            await axios.post("http://localhost:8000/user/registration/", userData , {
                headers: {
                    'Content-Type': 'application/json',
                    
                }
            })
            setShowSuccess(true);  // Show success message
            setTimeout(() => {
            setShowSuccess(false); // Hide success message after a delay
              navigate('/user/login');      // Redirect to user profile
            }, 1500);
        }catch(error){       
            setShowError(true);  // Show error message
            setTimeout(() => {
            setShowError(false); // Hide error message after a delay

            }, 1500);}
    } 
    return <>    

            <div className="container d-flex justify-content-center min-vh-100">
            
                <div className="card shadow" style={{ maxWidth: '400px', width: '100%' }}>
                    <div className="card-body">
                    <h3 className="card-title text-center mb-4">Register</h3>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                        <label htmlFor="email" className="form-label">Email</label>
                        <input
                            type="email"
                            className="form-control"
                            id="email"
                            placeholder="Enter your email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                        </div>
                        <div className="mb-3">
                        <label htmlFor="password" className="form-label">Password</label>
                        <input
                            type="password"
                            className="form-control"
                            id="password"
                            placeholder="Enter your password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                        </div>
                        <div className="mb-3">
                        <label htmlFor="password" className="form-label">Confirm Password</label>
                        <input
                            type="password"
                            className="form-control"
                            placeholder="Enter your password"
                            onChange={ (e) => setConfirmPassword(e.target.value) }
                            value={confirmPassword}
                            required
                        />
                        {error && <h5 style={{textAlign: "center", color: "red"}} >Password does not match</h5> }
                        {showError && <ErrorMessage onClose={() => setShowError(false)} message="Something went wrong. Try again!" />}
                        {showSuccess && <SuccessMessage onClose={() => setShowSuccess(false)} message={"Registered successfully!"} />}
                        </div>
                        <button type="submit" className="btn btn-success w-100">Register</button>
                    </form>         
      
                    </div>
                </div>
        </div>
    </>

}
