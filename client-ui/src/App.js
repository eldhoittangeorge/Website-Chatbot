import "./styles/App.css";
import { useContext } from "react";
import TextField from "./components/TextField";
import Header from "./components/Header";
import Button from "./components/Button";
import { ChatContext } from "./context/ChatContext";

function App() {
  const { data, getAnswer } = useContext(ChatContext);

  console.log(getAnswer());

  return (
    <div className="App">
      <Header />
      <TextField />
      {/* <h1>{data.te}</h1> */}
      <div className="buttonContainer">
        <Button label="Submit" />
        <Button label="Clear" />
      </div>
    </div>
  );
}

export default App;
