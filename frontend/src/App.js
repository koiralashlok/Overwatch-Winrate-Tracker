import { useEffect, useState } from "react";

function App() {
    const [msg, setMsg] = useState("");
    const [myTs, setTs] = useState("")

    useEffect(() => {
      fetch("http://127.0.0.1:8000/tracker/ping_frontend/1")
          .then((res) => res.json())
          .then(({ message, ts }) => {
              setMsg(message);
              setTs(ts);
          });
  }, []);
  
    return <>
      <h1>The response at {myTs} was:</h1>
      <h1>{msg}</h1>
    </>;
}

export default App;
