import React from 'react';

const SignupPage = () => {
  return (
    <div className="bg-gray-100">
      <header className="text-center py-10">
        <h1 className="text-4xl font-bold">Sign Up</h1>
      </header>
      <section className="px-4 py-8">
        <form>
          <div className="mb-4">
            <label className="block mb-2 font-bold" htmlFor="username">Username</label>
            <input className="w-full px-3 py-2 border border-gray-300 rounded" type="text" id="username" name="username" />
          </div>
          <div className="mb-4">
            <label className="block mb-2 font-bold" htmlFor="email">Email</label>
            <input className="w-full px-3 py-2 border border-gray-300 rounded" type="email" id="email" name="email" />
          </div>
          <div className="mb-4">
            <label className="block mb-2 font-bold" htmlFor="password">Password</label>
            <input className="w-full px-3 py-2 border border-gray-300 rounded" type="password" id="password" name="password" />
          </div>
          <div className="flex justify-center">
            <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" type="submit">Sign Up</button>
          </div>
        </form>
      </section>
    </div>
  );
};

export default SignupPage;
