import React, { useReducer, createContext } from "react";
import { ChatReducer } from "../reducer/ChatReducer";
const axios = require("axios");

export const ChatContext = createContext();

const ChatProvider = ({ children }) => {
  const initState = {
    question: "",
    answers: [],
    config: { name: "" },
    loading: false,
  };

  const [chatState, dispatch] = useReducer(ChatReducer, initState);

  const changeLoading = (status) => {
    dispatch({
      type: "MODIFY_LOADING",
      payload: status,
    });
  };

  const addData = (data) => {
    dispatch({
      type: "ADD_DATA",
      payload: data,
    });
  };

  const addConfigData = (data) => {
    dispatch({
      type: "ADD_CONFIG_DATA",
      payload: data,
    });
  };

  const writeQuestion = (data) => {
    dispatch({
      type: "WRITE_QUESTION",
      payload: data,
    });
  };

  const clearAllData = () => {
    dispatch({
      type: "CLEAR_ALL_DATA",
    });
  };

  const getAnswer = async (query) => {
    try {
      changeLoading(true);
      const response = await axios.get("http://127.0.0.1:5000/api", {
        params: { query: query },
      });
      console.log("THe data inside context", response.data);
      clearAllData();
      addData(response.data);
    } catch (error) {
      console.log(error);
    }
    changeLoading(false);
  };

  const getConfigData = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/config");
      console.log("The config data is ", response.data);
      addConfigData(response.data);
    } catch (error) {
      console.log("The error in config is ", error.message);
    }
  };

  return (
    <ChatContext.Provider
      value={{
        data: chatState,
        addData,
        writeQuestion,
        clearAllData,
        getAnswer,
        getConfigData,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export default ChatProvider;
