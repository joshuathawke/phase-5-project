import React from 'react';
import { Route, Routes } from 'react-router-dom';
import LandingPage from './LandingPage';
import TournamentsPage from './TournamentsPage';
import SignupPage from './SignupPage';
import TeamsPage from './TeamsPage';
import LoginPage from './LoginPage';

function App() {
  return (
    <Routes>
      <Route exact path="/" element={<LandingPage />} />
      <Route exact path="/tournaments" element={<TournamentsPage />} />
      <Route exact path="/signup" element={<SignupPage />} />
      <Route exact path="/teams" element={<TeamsPage />} />
      <Route exact path="/login" element={<LoginPage />} />
    </Routes>
  );
}

export default App;