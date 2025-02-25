import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./components/LoginPage";
import SignupPage from "./components/SignupPage";
import MainMenu from "./components/MainMenu";
import TransactionHistory from "./components/TransactionHistory";
import AdminControls from "./components/AdminControls";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route path="/menu" element={<MainMenu />} />
        <Route path="/transactions/:accountId" element={<TransactionHistory />} />
        <Route path="/admin" element={<AdminControls />} />
      </Routes>
    </Router>
  );
}

export default App;
