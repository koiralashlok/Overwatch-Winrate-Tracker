import React from "react";
import { useEffect, useState } from "react";
import WinrateTable from "../components/WinrateTable.tsx";
import { Typography } from "@mui/material";

type WinrateData = {
  map: string;
  wins: number;
  losses: number;
};

function WinratePage(props: { backend_url: string }) {
  const [msg, setMsg] = useState<string>("");
  const [payload, setPayload] = useState<WinrateData[]>([]);
  const playerId = "1";

  useEffect(() => {
    let backend_url = props.backend_url;

    fetch(backend_url + "/get_winrate_data_by_id/" + playerId)
      .then((res) => res.json())
      .then(({ message, payloadType, payload }) => {
        setMsg(message);

        if (payload && payload.map) {
          const dataArray: WinrateData[] = Object.keys(payload.map).map(
            (key) => ({
              map: payload.map[key] as string,
              wins: payload.wins[key] as number,
              losses: payload.losses[key] as number,
            })
          );
          setPayload(dataArray);
        }
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [props.backend_url]);

  return (
    <>
      <Typography variant="h3" align="center" sx={{ mt: 4 }}>
        Winrate Data for Player {playerId}
      </Typography>
      {payload.length != 0 && <WinrateTable data={payload} />}
      {!payload.length && (
        <Typography variant="h6" align="center" sx={{ mt: 4 }}>
          Could not fetch winrate data!
        </Typography>
      )}
    </>
  );
}

export default WinratePage;
