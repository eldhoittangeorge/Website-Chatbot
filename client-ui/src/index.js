import React from "react";
import ReactDOM from "react-dom";
import "./styles/index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import ChatContext from "./context/ChatContext";

ReactDOM.render(
  <React.StrictMode>
    <ChatContext>
      <App />
    </ChatContext>
  </React.StrictMode>,
  document.getElementById("root")
);

reportWebVitals();
