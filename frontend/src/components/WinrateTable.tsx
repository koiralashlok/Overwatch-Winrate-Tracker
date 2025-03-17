import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Box } from "@mui/material";

/**
 *
 * @param props
 *  data -> rows (map, win, losses)
 * @returns
 */
export default function WinrateTable(props) {

  if (props.data.length === 0){
    return false;
  }

  const header = ["Maps", "Wins", "Losses"].map((item) => (
    <TableCell key={item + " column header"}>
      <b>{item}</b>
    </TableCell>
  ));
  const headerRow = <TableRow>{header}</TableRow>;

  const rows = props.data.map((item, index) => (
    <TableRow key={index + " " + item + " row"}>
      <TableCell>{item.map}</TableCell>
      <TableCell>{item.wins}</TableCell>
      <TableCell>{item.losses}</TableCell>
    </TableRow>
  ));

  return (
    <Box display="flex" justifyContent="center" mt={4}>
      <TableContainer component={Paper} sx={{ maxWidth: 600 }}>
        <Table aria-label="winrate_table">
          <TableHead>{headerRow}</TableHead>
          <TableBody>{rows}</TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}
