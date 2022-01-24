import "./styles/App.css";
import { useContext } from "react";
import Header from "./components/Header";
import { ChatContext } from "./context/ChatContext";
import UserInput from "./components/UserInput";
import Result from "./components/Result";

function App() {
  const { data, getAnswer } = useContext(ChatContext);

  // console.log(getAnswer());

  return (
    <div className="App">
      <Header />
      <UserInput />
      <Result />
    </div>
  );
}

export default App;
