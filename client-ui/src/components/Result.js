import React, { useContext } from "react";
import ResultItem from "./ResultItem";
import { ChatContext } from "../context/ChatContext";

const Result = () => {
  const { data } = useContext(ChatContext);

  const resultList = data.answers.map((result) => (
    <ResultItem result={result} />
  ));
  return resultList;
};

export default Result;
