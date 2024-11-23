import { ReactComponent as ProfileIcon } from './icons/person-fill.svg';
import { ReactComponent as ProductIcon } from './icons/basket.svg';
import Logo from './icons/logo.jpg';
import { ReactComponent as WeIcon } from './icons/person-arms-up.svg';
import { HashRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Login from './features/Auth/Login/login.js'
import Profile from './features/Auth/Profile/profile.js'
import Products from './features/Products/products.js'
import Registration from './features/Auth/Registration/registration.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import './index.css'

export default function App() {
  return <>   
   
   <Router>
    <Navbar /> 
      <Routes>
        <Route path="/user/login" element={<Login />} />
        <Route path="/user" element={<Profile />} />
        <Route path="/products" element={<Products />} />
        <Route path="/user/registration" element={<Registration />} />
      </Routes>
    </Router>

  </>;
}

function Navbar() {
  return <>
    <div className="menu">
      <a href="#"><img src={Logo} id="logo" /></a>
      <nav className="navbar">
           <ul className="navbar-nav">
          <li>
            <Link to="/user">
              <ProfileIcon /> Profile
            </Link>
          </li>
        </ul>
        <ul className="navbar-nav">
          <li>
            <Link to="/products">
              <ProductIcon /> Products
            </Link>
          </li>
        </ul>
        <ul className="navbar-nav">
          <li>
            <Link to="#">
              <WeIcon /> We
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  </>
}

