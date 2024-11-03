import { ReactComponent as ProfileIcon } from './icons/person-fill.svg';
import { ReactComponent as ProductIcon } from './icons/basket.svg';
import Logo from './icons/logo.jpg';
import { ReactComponent as WeIcon } from './icons/person-arms-up.svg';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './features/Auth/login.js'
import Profile from './features/Auth/profile.js'
import Products from './features/Products/products.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import './index.css'

export default function App() {
  return <>
   <Navbar></Navbar>  
   <Router>
    <Routes>
      <Route path="users/login" element={<Login />} />
    </Routes>
  </Router>
  <Router>
    <Routes>
      <Route path="users/" element={<Profile />} />
    </Routes>
  </Router>
  <Router>
    <Routes>
      <Route path="products/" element={<Products />} />
    </Routes>
  </Router>
  </>;
}

function Navbar() {
  return <>
    <div className="menu">
      <a href="#"><img src={Logo} id="logo" /></a>
      <nav className="navbar">
        <ul className="navbar-nav"><a href="/users" ><ProfileIcon /> Profile</a></ul>
        <ul className="navbar-nav"><a href="#"><ProductIcon /> Products</a></ul>
        <ul className="navbar-nav"><a href="#"><WeIcon /> We</a></ul>
      </nav>
    </div>
  </>
}

