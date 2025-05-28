import React, { useState } from "react";
import axios from "axios";

const ChatBox = () => {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState(null);

  const sendPrompt = async () => {
    const res = await axios.post("http://localhost:5000/prompt/score", { prompt });
    setResponse(res.data);
  };

  return (
    <div>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      <button onClick={sendPrompt}>Envoyer</button>
      {response && (
        <div>
          <p><strong>Réponse IA :</strong> {response.response}</p>
          <p><strong>Score :</strong> {response.score}</p>
        </div>
      )}
    </div>
  );
};

export default ChatBox;
