import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';

export default function Main(){

    const [products, setProducts] = useState();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/products/', {
                });
                setProducts(response.data); // Set the products data
            } catch (err) {
                setError(err);
                console.error('Error fetching products:', err);
            } finally {
                setLoading(false); // Stop loading once data is fetched
            }
         }
        fetchProducts();
    }, []);

    if (loading) {
        return <p>Loading products...</p>;
    }

    if (error) {
        return <p>Error loading products: {error.message}</p>;
    }
    return <>        
        {products.map((product) => (
            <ProductCard key={product.id} product={product} /> 
            
        ))}
    
    </>
}