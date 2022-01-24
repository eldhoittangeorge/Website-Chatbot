import React from "react";
import Button from "./Button";
import "../styles/UserInput.css";
import TextField from "./TextField";

const UserInput = () => {
  return (
    <div className="container">
      <TextField />
      <Button label="Send" />
    </div>
  );
};

export default UserInput;
