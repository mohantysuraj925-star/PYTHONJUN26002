import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import "./App.css";

function Page({ title }) {
  return <div className="wrap"><h1 style={{color: 'white', marginTop: '50px'}}>{title} Page</h1></div>;
}

function App() {
  return (
    <Router>
      <div className="login-container">
        <nav className="navbar">
          <div className="logo">SURAJ KUMAR</div>
          <div className="menu">
            <Link to="/">Home</Link>
            <Link to="/services">Services</Link>
            <Link to="/contact">Contact</Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={
            <div className="wrap">
              <div className="card">
                <h2 className="title">Login</h2>
                <form>
                  <div className="group"><input type="email" placeholder="Email" required /></div>
                  <div className="group"><input type="password" placeholder="Password" required /></div>
                  <button className="login-btn" type="button">Login</button>
                </form>
              </div>
            </div>
          } />
          <Route path="/services" element={<Page title="Services" />} />
          <Route path="/contact" element={<Page title="Contact" />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;
