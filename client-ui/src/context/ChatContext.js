import React, { useReducer, createContext } from "react";
import { ChatReducer } from "../reducer/ChatReducer";
const axios = require("axios");

export const ChatContext = createContext();

const ChatProvider = ({ children }) => {
  const initState = {
    question: "one",
    answers: [
      {
        answer: "Ernakulam",
        context:
          "ering (CSE) at the Muthoot Institute of Technology and Science (MITS), Ernakulam! As you glance through the faculty profile, I am sure that you will a",
      },
      {
        answer: "Puthencruz",
        context:
          "Department profile Muthoot Institute of Technology and Science (MITS) Puthencruz was established in May 2013 and started its academic program in Augus",
      },
      {
        answer: "Kochi",
        context:
          "pal Muthoot Institute of Technology & Science Varikoli P.O., Puthencruz, Kochi – 682308, Ernakulam District. Ph.0484 – 2732100, 2732111, 2733011 Fax:",
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

  const getAnswer = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/api", {
        params: { One: "two" },
      });
      console.log(response);
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
