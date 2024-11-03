import React from 'react';
import Logo from './ava.jpg'
import './css/profile.css'
import Hoodie from './hoodie.jpg'
import ProductCard from '/Users/arsensejtkaliev/PycharmProjects/pythonProject1/out_west_frontend/west/src/features/Products/ProductCard.js'


export default function Profile(){
    return <> 

    <div className="user-info">
        <div className="user-image"><a><img src={Logo}  id="profile" /></a></div>
        
        <div className="line" ></div>

        <div className="user-data">
            <h5>First Name</h5>
            <h5>18 products selected</h5>
        </div>

        <div className="line" ></div>
        
    </div>
    <div className="selected_products">
        <div className="product-image">
        <a><img id="product_image" src={Hoodie} /></a>

            
        </div>
        <div className="product-info">
            <p>Hoodie "Pepe the frog"</p>
        </div>
    </div>

    </>
}