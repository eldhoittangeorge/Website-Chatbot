import React from "react";

const ResultItem = (props) => {
  const { result, context, link } = props.result;
  return (
    <div>
      <p>Answer:{result}</p>
      <p>Context: {context}</p>
      <p>Links: {link}</p>
    </div>
  );
};

export default ResultItem;
