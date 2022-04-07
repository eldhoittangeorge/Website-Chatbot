import "../styles/Header.css";
import React, { useContext, useEffect } from "react";
import { ChatContext } from "../context/ChatContext";

function Header() {
  const { data } = useContext(ChatContext);
  const { name, website } = data.config;

  return (
    <div>
      <h1 className="heading">Chatbot Demo - Explore {name}</h1>
      <p className="text">
        This demo takes its data from MITS website({website}) crawled on
        December 2021
      </p>
      <p className="text noteText">
        <i>Note. Do not use keywords, but full fledged question</i>
      </p>
    </div>
  );
}

export default Header;
