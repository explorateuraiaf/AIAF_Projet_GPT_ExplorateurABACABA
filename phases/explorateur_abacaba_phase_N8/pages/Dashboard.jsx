import React from "react";
import ChatBox from "../components/ChatBox";
import HistoryPanel from "../components/HistoryPanel";

const Dashboard = () => (
  <div className="dashboard">
    <h1>GPT Explorateur ABACABA</h1>
    <ChatBox />
    <HistoryPanel />
  </div>
);

export default Dashboard;
