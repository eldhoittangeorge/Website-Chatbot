import React, { useContext } from "react";
import Button from "./Button";
import "../styles/UserInput.css";
import QueryInput from "./QueryInput";
import { ChatContext } from "../context/ChatContext";

const UserInput = () => {
  const { clearAllData, data, getAnswer } = useContext(ChatContext);

  const handleRunClick = () => {
    if (data.question !== "") {
      getAnswer(data.question);
    }
  };

  const clearQuestionAndResult = () => {
    clearAllData();
  };

  return (
    <div className="userInputContainer">
      <QueryInput />
      <div className="buttonContainer">
        <Button label="Run" handleClick={handleRunClick} />
        <Button label="Clear Question" handleClick={clearQuestionAndResult} />
      </div>
    </div>
  );
};

export default UserInput;
