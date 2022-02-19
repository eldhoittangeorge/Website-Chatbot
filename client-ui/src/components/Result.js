import React, { useContext } from "react";
import ResultItem from "./ResultItem";
import { ChatContext } from "../context/ChatContext";

const Result = () => {
  const { data } = useContext(ChatContext);

  console.log("The data inside reesult", data.answers);

  const resultList = data.answers.map((result, index) => (
    <ResultItem result={result} key={index} />
  ));

  return (
    <>
      {data.answers.length !== 0 ? <h2>Result</h2> : null}
      {resultList}
    </>
  );
};

export default Result;
