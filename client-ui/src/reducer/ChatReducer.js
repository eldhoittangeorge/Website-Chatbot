export const ChatReducer = (state, action) => {
  switch (action.type) {
    case "ADD_DATA":
      console.log("the value ", action.payload);
      return { ...state, answers: action.payload.answers };
    case "WRITE_QUESTION":
      return { ...state, question: action.payload };
    case "CLEAR_ALL_DATA":
      return { ...state, question: "", answers: [] };
    case "ADD_CONFIG_DATA":
      return { ...state, config: action.payload };
    case "MODIFY_LOADING":
      return { ...state, loading: action.payload };
    default:
      return state;
  }
};
