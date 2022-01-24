import "../styles/Button.css";
import React, { useContext } from "react";
import { ChatContext } from "../context/ChatContext";

function Button(props) {
  const { data, addData, getAnswer } = useContext(ChatContext);

  const handleClick = () => {
    console.log("Clicked")
    getAnswer(data.question)
    addData("");
  };

  const { label } = props;
  return (
    <input
      onClick={handleClick}
      type="button"
      value={label}
      className="button"
    />
  );
}

export default Button;
