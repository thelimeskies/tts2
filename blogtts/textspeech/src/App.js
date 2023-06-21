import logo from './logo.svg';
import './App.css';
import { Route, Routes } from 'react-router';
import Home from './views/Home';
import Blog from './views/Blog';
import LandingPage from './views/LandingPage';

function App() {
  return (
    <div className="App overflow-hidden">
      <Routes>
        <Route path="/" element={<LandingPage />}/>
        <Route path="/home" element={<Home />}/>
        <Route path="/blog">
          <Route path=":blogId"  element={<Blog />}/>
        </Route>
      </Routes>
    </div>
  );
}

export default App;
