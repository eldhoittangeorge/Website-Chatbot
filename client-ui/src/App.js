import "./styles/App.css";
import { useContext, useEffect } from "react";
import Header from "./components/Header";
import { ChatContext } from "./context/ChatContext";
import UserInput from "./components/UserInput";
import Loading from "./components/Loading";
import Result from "./components/Result";

function App() {
  const { getConfigData, data } = useContext(ChatContext);
  const loading = data.loading;

  useEffect(() => {
    getConfigData();
  }, []);

  return (
    <div className="App">
      <Header />
      <UserInput />
      {loading ? <Loading /> : <Result />}
    </div>
  );
}

export default App;
