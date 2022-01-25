import React, { useContext } from "react";
import ResultItem from "./ResultItem";
import { ChatContext } from "../context/ChatContext";

const Result = () => {
  const { data } = useContext(ChatContext);

  if (data.answers == null) {
    return "";
  } else {
    const resultList = data.answers.map((result) => (
      <ResultItem result={result} />
    ));
    return (
      <>
        <h2>Result</h2>
        {resultList}
      </>
    );
  }
};

export default Result;
