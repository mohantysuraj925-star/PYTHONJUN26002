import "./App.css";

function App() {
  return (
    <div className="login-container">
      <nav className="navbar">
        <div className="logo">SURAJ KUMAR</div>
        <div className="menu">
          <a href="#">Home</a>
          <a href="#">Services</a>
          <a href="#">Contact</a>
        </div>
      </nav>
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
    </div>
  );
}
export default App;
