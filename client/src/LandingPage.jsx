import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="flex justify-between bg-gray-900 p-4">
      <div className="text-white">
        <Link to="/">Esports Elevated</Link>
      </div>
      <div className="flex">
        <Link to="/tournaments" className="text-white mx-4">
          Tournaments
        </Link>
        <Link to="/teams" className="text-white mx-4">
          Teams
        </Link>
        <Link to="/login" className="text-white mx-4">
          Login
        </Link>
      </div>
    </nav>
  );
};

const LandingPage = () => {
  return (
    <div className="bg-black text-white">
      <Navbar />
      <header className="text-center py-10">
        <h1 className="text-4xl font-bold">Esports Elevated</h1>
        <p className="mt-4">Elevate your Game!</p>
      </header>
      <section className="px-4 py-8 text-center">
       
      </section>
      <section className="px-4 py-8 text-center">
        <h2 className="text-2xl font-bold">Join The Games!</h2>
        <div className="flex justify-center">
          <Link
            to="/signup"
            className="px-4 py-2 mr-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Sign Up
          </Link>
        </div>
      </section>
      <footer className="text-center py-4 bg-gray-900 fixed bottom-0 left-0 w-full">
        <p>&copy; 2023 Esports Elevated. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default LandingPage;