import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import { useEffect } from 'react';
import red_image from './red_image.png'
import { useNavigate } from 'react-router-dom';

function Error({ show, onClose }) {
    const navigate = useNavigate();

    const LoginClick = async (e) => {
        navigate('/user/login')
    }
    const RegisterClick = async (e) => {
        navigate('/user/registration')
    }

    return (
      <>
        {/* Conditionally render the toast based on the "show" prop */}
        {show && (
          <div className="toast show position-fixed bottom-0 end-0 p-3" style={{ zIndex: 9999 }}>
            <div className="toast-header">
              <img src={red_image} className="rounded me-2" alt="There should be red sign." style={{ width: '10%', height: '10%' }} />
              <strong className="me-auto">Outwest</strong>
              <small>just now</small>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="toast"
                aria-label="Close"
                onClick={onClose}  // Trigger the onClose function when clicked
              ></button>
            </div>
            <div className="toast-body">
                <h6>You are not logged in.</h6>
                <button className='btn btn-warning' style={{'marginrRight': '10%'}} onClick={LoginClick} >Log in</button>
                <button className="btn btn-warning" onClick={RegisterClick} >Sign up</button>
            </div>
          </div>
        )}
      </>
    );
  }
  
  export default Error;