import { useEffect, useState } from "react";
import secretsJson from './frontend-secrets.json';

function App() {
  const [msg, setMsg] = useState("");
  const [payload, setPayload] = useState([]);

  useEffect(() => {
    // TODO replace w terraform!
    let backend_url = secretsJson.backend_url

    if(backend_url === "accelerando"){
      backend_url = "http://localhost:8000"
    }

    fetch(backend_url+"/tracker/get_winrate_data_by_id/1")
      .then((res) => res.json())
      .then(({ message, payloadType, payload }) => {
        setMsg(message);
        // Convert the payload into an array of objects if it's in dict format:
        const dataArray = Object.keys(payload.map).map((key) => ({
          map: payload.map[key],
          wins: payload.wins[key],
          losses: payload.losses[key],
        }));
        setPayload(dataArray);
      });
  }, []);

  return (
    <>
      <h1>{msg}</h1>
      <table>
        <thead>
          <tr>
            <th>Map</th>
            <th>Wins</th>
            <th>Losses</th>
          </tr>
        </thead>
        <tbody>
          {payload.map((item, index) => (
            <tr key={index}>
              <td>{item.map}</td>
              <td>{item.wins}</td>
              <td>{item.losses}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}

export default App;
