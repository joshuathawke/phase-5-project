import React from 'react';
import { Link } from 'react-router-dom';

const TournamentsPage = () => {
  const tournaments = [
    { id: 1, name: 'Tournament 1', date: 'June 2, 2023' },
    { id: 2, name: 'Tournament 2', date: 'June 9, 2023' },
    { id: 3, name: 'Tournament 3', date: 'June 16, 2023' },
  ];

  return (
    <div className="bg-gray-100">
      <header className="text-center py-10">
        <h1 className="text-4xl font-bold">Upcoming Tournaments</h1>
      </header>
      <section className="px-4 py-8">
        <ul className="space-y-4">
          {tournaments.map(tournament => (
            <li key={tournament.id} className="border-b border-gray-300">
              <h2 className="text-xl font-bold">{tournament.name}</h2>
              <p className="text-gray-600">{tournament.date}</p>
              <a href={`/tournament/${tournament.id}`} className="text-blue-500 hover:underline">View Details</a>
            </li>
          ))}
        </ul>
      </section>
      <section className="px-4 py-8">
        <h2 className="text-2xl font-bold">Join The Fun</h2>
        <p className="mt-2">Sign up now to join our esports community.</p>
        <Link to="/sign-up" className="px-4 py-2 mt-4 bg-blue-500 text-white rounded hover:bg-blue-600">Sign Up</Link>
      </section>
    </div>
  );
};

export default TournamentsPage;
