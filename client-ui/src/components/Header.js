import "../styles/Header.css";
import React from "react";

function Header() {
  return (
    <div>
      <h1 className="heading">Chatbot Demo - Explore MITS</h1>
      <p className="text">
        This demo takes its data from MITS website crawled on December 2021
      </p>
      <p className="text noteText">
        <i>Note. Do not use keywords, but full fledged question</i>
      </p>
    </div>
  );
}

export default Header;
