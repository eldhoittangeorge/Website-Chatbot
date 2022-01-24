import React, { useContext } from "react";
import ResultItem from "./ResultItem";
import { ChatContext } from "../context/ChatContext";

const Result = () => {
  const { data } = useContext(ChatContext);

  // console.log("The data was "+JSON.stringify(data))

  if(data.answers == null){
    return ""
  }else{
    const resultList = data.answers.map((result) => (
    <ResultItem result={result} />
  ));
 return resultList;
 
  }
};

export default Result;
