/** @format */

import { useState } from "react";
import useAuth from "../hooks/useAuth";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { login, authLoading, authError } = useAuth();
  const navigate = useNavigate();
  const handleLogin = async (e) => {
    e.preventDefault();

    if (!username || !password) {
      setError("Please fill in all fields");
      return;
    }
    const success = await login(username, password);

    if (success) {
      navigate("/"); // ✅ Redirect only if login was successful
    }

    // Clear the error if everything is fine
    setError("");
  };

  return (
    <div className="max-w-lg p-6 mx-auto border rounded-lg shadow-lg mt-36 lg:mt-44 bg-[#FCFCFC]">
      <h2 className="text-2xl font-bold text-[#151517]">Login</h2>
      <p className="text-[#363a36] text-[15px] font-medium">
        Welcome back! Please log in to access your account.
      </p>
      {error && <p className="mb-2 text-sm text-red-500">{error}</p>}
      <form onSubmit={handleLogin} className="py-4">
        <div className="mb-4">
          <label
            htmlFor="username"
            className={`block mb-1 text-sm font-semibold text-gray-700 ${authError && 'text-red-700'}`}
          >
            Username
          </label>
          <input
            type="text"
            id="username"
            value={username}
            disabled={authLoading}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950"
            placeholder="Enter your Username"
            required
          />
        </div>
        <div className="mb-4">
          <label
            htmlFor="password"
            className={`block mb-1 text-sm font-semibold text-gray-700 ${authError && 'text-red-700'}`}
          >
            Password
          </label>
          <input
            type="password"
            id="password"
            value={password}
            disabled={authLoading}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950"
            placeholder="Enter your password"
            required
          />
        </div>
        <div className="flex items-center justify-center">
          <button
            type="submit"
            disabled={authLoading}
            className="w-40 py-2 text-center text-white transition duration-300 bg-blue-500 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 disabled:opacity-70 disabled:cursor-not-allowed flex items-center justify-center"
          >
            {authLoading ? (
              <>
                <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Logging in...
              </>
            ) : (
              'Login'
            )}
          </button>
        </div>
        {authError && <div className="text-red-500 place-self-center py-5">{authError.detail || authError}</div>}
      </form>
      <p className="mt-4 text-[17px] text-center text-[#15919B]">
        Don&apos;t have an account?{" "}
        <a href="/signup" className="text-[#151517] hover:underline">
          Sign Up
        </a>
      </p>
    </div>
  );
};

export default Login;
