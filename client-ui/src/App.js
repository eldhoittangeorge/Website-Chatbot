import "./styles/App.css";
import { useContext, useEffect } from "react";
import Header from "./components/Header";
import { ChatContext } from "./context/ChatContext";
import UserInput from "./components/UserInput";
import Result from "./components/Result";

function App() {
  const { getConfigData } = useContext(ChatContext);

  useEffect(() => {
    getConfigData();
  }, []);

  return (
    <div className="App">
      <Header />
      <UserInput />
      <Result />
    </div>
  );
}

export default App;
