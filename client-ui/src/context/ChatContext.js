import React, { useReducer, createContext } from "react";
import { ChatReducer } from "../reducer/ChatReducer";
const axios = require("axios");

export const ChatContext = createContext();

const ChatProvider = ({ children }) => {
  const initState = {
    question: "",
    answers: [],
  };

  const [chatState, dispatch] = useReducer(ChatReducer, initState);

  const addData = (data) => {
    dispatch({
      type: "ADD_DATA",
      payload: data,
    });
  };

  const writeQuestion = (data) => {
    dispatch({
      type: "WRITE_QUESTION",
      payload: data,
    });
  };

  const getAnswer = async (query) => {
    try {
      console.log("Get answer called")
      const response = await axios.get("http://127.0.0.1:5000/api", {
        params: { query: query },
      });
      addData(response.data)
      // console.log(response);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <ChatContext.Provider
      value={{
        data: chatState,
        addData,
        writeQuestion,
        getAnswer,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export default ChatProvider;
