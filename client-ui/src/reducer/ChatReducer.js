export const ChatReducer = (state, action) => {
  switch (action.type) {
    case "ADD_DATA":
      return { ...state, te: action.payload };
    case "WRITE_QUESTION":
      return { ...state, question: action.payload };
    default:
      return state;
  }
};
