import React, { useContext } from "react";
import { ChatContext } from "../context/ChatContext";
import TextField from "@mui/material/TextField";
import "../styles/QueryInput.css";

const QueryInput = () => {
  const { data, writeQuestion } = useContext(ChatContext);

  const customStyle = { color: "red" };

  return (
    <input
      type="text"
      placeholder="Please ask the question"
      value={data.question}
      onChange={(event) => {
        writeQuestion(event.target.value);
      }}
    />
  );
};

export default QueryInput;
