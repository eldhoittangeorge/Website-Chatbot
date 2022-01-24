export const ChatReducer = (state, action) => {
  switch (action.type) {
    case "ADD_DATA":
      // console.log("Blah here"+JSON.stringify(action.payload))
      return { ...state, answers: action.payload.answers };
    case "WRITE_QUESTION":
      console.log("The question is "+action.payload)
      return { ...state, question: action.payload };
    default:
      return state;
  }
};
