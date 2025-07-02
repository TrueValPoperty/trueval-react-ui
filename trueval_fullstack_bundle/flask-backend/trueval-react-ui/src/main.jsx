
import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import App from './pages/App'
import Admin from './pages/Admin'
import Logs from './pages/Logs'
import Login from './pages/Login'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/admin" element={<Admin />} />
      <Route path="/logs" element={<Logs />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  </BrowserRouter>
)
