import React from 'react';
import './css/ProductCard.css'; // Import the CSS file for styling
import {useState} from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom';
import Error from './NotAuthorizedError';
import SuccessMessage from '../Auth/SuccessMessage.js'

const ProductCard = ({ product }) => {
    //const [showSuccess, setShowSuccess] = useState(false);
    const [showToast, setShowToast] = useState(false);

    const handleShowToast = () => setShowToast(true);
    const handleCloseToast = () => setShowToast(false);
    const handleSubmit = async (e) => {
        e.preventDefault()
        const token = localStorage.getItem("access_token")
        if (!token){
            setShowToast(true);
            setTimeout( () => {
                setShowToast(false)
            }, 3000 )
        
            return;
        }
        const data = {
            product: product.id,
        }
        try {
            await axios.post("http://127.0.0.1:8000/products/add/", data, 
                {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                }}
            )
        } catch (error) {
            console.log("error")
        }
    }

    console.log(product.product_image);
    return <>
        <div className="products">
            <div className="product-card">
                <img src={`http://127.0.0.1:8000${product.product_image}`} className="product-image" />
                <h2 className="product-title">{product.product_name}</h2>
                <p className="product-description">{product.product_description}</p>
                <span className="product-price">{product.product_price} Теңге</span>
                <div><button className="product-button" type="button" onClick={handleSubmit}>Add to Cart</button></div>

            </div>
        </div>
        <Error show={showToast} onClose={handleCloseToast}/>

    </>;
};

export default ProductCard;