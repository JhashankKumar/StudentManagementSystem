import React from 'react';
import { BrowserRouter as  Route, Routes, Router } from 'react-router-dom';
import Login from './components/Login';
import SignUp from './components/SignUp';
import AdminDashboard from './components/AdminDashboard';
import TeacherDashboard from './components/TeacherDashboard';

function App() {
  return (
    
    <Router>
      <Routes>
        <Route path="/login" component={Login} />
        <Route path="/signup" component={SignUp} />
        <Route path="/admin" component={AdminDashboard} />
        <Route path="/teacher" component={TeacherDashboard} />
        <Route path="/" component={Login} />
      </Routes>
    </Router>
  );
}


export default App;

