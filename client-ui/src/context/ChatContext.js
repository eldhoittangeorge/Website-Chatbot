import React, { useReducer, createContext } from "react";
import { ChatReducer } from "../reducer/ChatReducer";
const axios = require("axios");

export const ChatContext = createContext();

const ChatProvider = ({ children }) => {
  const initState = {
    question: "",
    answers: [
      {
        result: "One",
        context:
          "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
        link: "http://www.google.com",
      },
    ],
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
      console.log("Get answer called");
      const response = await axios.get("http://127.0.0.1:5000/api", {
        params: { query: query },
      });
      addData(response.data);
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
