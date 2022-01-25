import React from "react";
import Button from "./Button";
import "../styles/UserInput.css";
import QueryInput from "./QueryInput";

const UserInput = () => {
  return (
    <div className="userInputContainer">
      <QueryInput />
      <div className="buttonContainer">
        <Button label="Run" />
        <Button label="Clear Question" />
      </div>
    </div>
  );
};

export default UserInput;
