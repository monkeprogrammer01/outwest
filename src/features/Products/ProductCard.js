import React from 'react';
import './css/ProductCard.css'; // Import the CSS file for styling



const ProductCard = ({ product }) => {
    console.log(product.product_image);
    return <>
        <div className="products">
            <div className="product-card">
                <img src={`http://127.0.0.1:8000${product.product_image}`} className="product-image" />
                <h2 className="product-title">{product.product_name}</h2>
                <p className="product-description">{product.product_description}</p>
                <span className="product-price">{product.product_price} Tg</span>
                <div><button className="product-button" >Add to Cart</button></div>

            </div>
        </div>
    </>;
};

export default ProductCard;