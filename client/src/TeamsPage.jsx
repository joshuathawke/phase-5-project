import React from 'react';

const TeamsPage = () => {
  const teams = [
    { id: 1, name: 'Team 1', members: ['Player 1', 'Player 2', 'Player 3'] },
    { id: 2, name: 'Team 2', members: ['Player 4', 'Player 5', 'Player 6'] },
    { id: 3, name: 'Team 3', members: ['Player 7', 'Player 8', 'Player 9'] },
  ];

  const handleJoinTeam = (teamId) => {
    // Logic to handle joining a team upon approval
    console.log(`Joining team with id ${teamId}`);
  };

  return (
    <div className="bg-gray-100">
      <header className="text-center py-10">
        <h1 className="text-4xl font-bold">Teams</h1>
      </header>
      <section className="px-4 py-8">
        <ul className="space-y-4">
          {teams.map((team) => (
            <li key={team.id} className="border-b border-gray-300">
              <h2 className="text-xl font-bold">{team.name}</h2>
              <p className="mt-2">Members: {team.members.join(', ')}</p>
              <button
                className="px-4 py-2 mt-4 bg-blue-500 text-white rounded hover:bg-blue-600"
                onClick={() => handleJoinTeam(team.id)}
              >
                Join Team
              </button>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};

export default TeamsPage;
