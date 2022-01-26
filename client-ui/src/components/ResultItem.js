import React from "react";
import "../styles/ResultItem.css";

const ResultItem = (props) => {
  const { result, context, document_link } = props.result;
  return (
    <div className="resultItemContainer">
      <p className="resultItem">
        <b>Answer</b>:{result}
      </p>
      <p className="resultItem">
        <b>Context</b>:{context}
      </p>
      <p className="resultItem">
        <b>Source</b>: <a href={document_link}>{document_link}</a>
      </p>
      <hr className="solid" />
    </div>
  );
};

export default ResultItem;
