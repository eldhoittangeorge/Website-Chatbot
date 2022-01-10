import React, { useContext } from "react";
import { ChatContext } from "../context/ChatContext";

const TextField = () => {
  const { data, writeQuestion } = useContext(ChatContext);

  return (
    <div>
      <input
        type="text"
        value={data.question}
        onChange={(event) => {
          writeQuestion(event.target.value);
        }}
      />
    </div>
  );
};

export default TextField;
