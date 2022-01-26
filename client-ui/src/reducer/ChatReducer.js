export const ChatReducer = (state, action) => {
  switch (action.type) {
    case "ADD_DATA":
      return { ...state, answers: action.payload.answers };
    case "WRITE_QUESTION":
      return { ...state, question: action.payload };
      case "CLEAR_ALL_DATA":
        return {...state, question:"", answers:[]};
    default:
      return state;
  }
};
