import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
    return (
        <div className="bg-black text-white">
            <header className="text-center py-10">
                <h1 className="text-4xl font-bold">Esports Elevated</h1>
                <p className="mt-4">Join the competitions!</p>
            </header>
            <section className="px-4 py-8">
                <h2 className="text-2xl font-bold">Tournaments</h2>
                <p className="mt-2">Upcoming tournaments:</p>
                <ul className="list-disc list-inside mt-2">
                    <li>Tournament 1</li>
                    <li>Tournament 2</li>
                    <li>Tournament 3</li>
                </ul>
            </section>
            <section className="px-4 py-8">
                <h2 className="text-2xl font-bold">Join The Fun</h2>
                <p className="mt-2">Sign up or log in to your account:</p>
                <div className="flex justify-center">
                    <Link to="/signup" className="px-4 py-2 mr-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                        Sign Up
                    </Link>
                    <Link to="/login" className="px-4 py-2 ml-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                        Login
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
