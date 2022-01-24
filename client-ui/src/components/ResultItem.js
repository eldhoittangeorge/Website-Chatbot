import React from "react";

const ResultItem = (props) => {
  const { answer, context, link } = props.result;
  return (
    <div>
      <p>Answer:{answer}</p>
      <p>Context: {context}</p>
      <p>Links: {link}</p>
    </div>
  );
};

export default ResultItem;
