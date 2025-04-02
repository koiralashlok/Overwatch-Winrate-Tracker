import * as React from "react";
import { styled, useTheme } from "@mui/material/styles";
import { useNavigate } from "react-router-dom";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import CssBaseline from "@mui/material/CssBaseline";
import MuiAppBar, { AppBarProps as MuiAppBarProps } from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import HomeIcon from '@mui/icons-material/Home';
import PersonIcon from '@mui/icons-material/Person';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import { Button } from "@mui/material";

const drawerWidth = 240;
const collapsedDrawerWidth = 60;

// Styled AppBar that stays fixed at the top
interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})<AppBarProps>(({ theme }) => ({
  zIndex: theme.zIndex.drawer + 1,
}));

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const navigate = useNavigate();

  const theme = useTheme();
  const [open, setOpen] = React.useState(true);

  const handleDrawerToggle = () => {
    setOpen(!open);
  };

  const menuItems = {
    Home: { path: "/home", icon: <HomeIcon /> },
    Winrate: { path: "/winrate", icon: <TrendingUpIcon /> },
    Account: { path: "/account", icon: <PersonIcon /> },
  }

  return (
    <Box sx={{ display: "flex", minHeight: "100vh", flexDirection: "column" }}>
      <CssBaseline />

      {/* Top Navbar */}
      <AppBar position="fixed">
        <Toolbar>
          <IconButton color="inherit" onClick={handleDrawerToggle} edge="start">
            <MenuIcon />
          </IconButton>
          <Button color="inherit" onClick={() => navigate("/")}>Overwatch Winrate Tracker</Button>
        </Toolbar>
      </AppBar>

      {/* Sidebar Drawer */}
      <Drawer
        variant="permanent"
        sx={{
          width: open ? drawerWidth : collapsedDrawerWidth,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: open ? drawerWidth : collapsedDrawerWidth,
            transition: theme.transitions.create("width", {
              easing: theme.transitions.easing.sharp,
              duration: theme.transitions.duration.enteringScreen,
            }),
            overflowX: "hidden",
            boxSizing: "border-box",
            mt: 8, // Space below AppBar
          },
        }}
        open={open}
      >
        <Divider />
        <List>
          {Object.keys(menuItems).map((listItemName) =>
            <ListItem key={listItemName} disablePadding sx={{ display: "flex" }}>
              <ListItemButton sx={{ justifyContent: open ? "initial" : "left" }} onClick={() => navigate((menuItems[listItemName]).path)}>
                <ListItemIcon sx={{ minWidth: 0, mr: open ? 2 : "auto" }}>
                  {(menuItems[listItemName]).icon}
                </ListItemIcon>
                {open && <ListItemText primary={listItemName} />}
              </ListItemButton>
            </ListItem>
          )}
        </List>
      </Drawer>

      {/* Main Content */}
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          minHeight: "calc(100vh - 64px)", // Adjusted for AppBar
          width: `calc(100% - ${open ? drawerWidth : collapsedDrawerWidth}px)`,
          ml: `${open ? drawerWidth : collapsedDrawerWidth}px`,
          mt: 8, // Space for AppBar
          px: 3,
          transition: theme.transitions.create(["margin", "width"], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
          }),
        }}
      >
        {children}
      </Box>

      {/* Footer */}
      <Box
        component="footer"
        sx={{
          bgcolor: "black",
          color: "white",
          textAlign: "center",
          p: 2,
          width: "100%",
          position: "relative",
        }}
      >
        {/* <Box sx={{ display: "flex", justifyContent: "center", mt: 1 }}> */}
        <Box sx={{
          display: "flex",
          justifyContent: "center",
          ml: `${open ? drawerWidth : collapsedDrawerWidth}px`,
          mt: 1,
          px: 3,
          transition: theme.transitions.create(["margin", "width"], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
          }),
        }}>
          <List sx={{ display: "flex", flexDirection: "row", p: 0 }}>
            <ListItemButton sx={{ textAlign: "center" }} onClick={() => navigate("/about")} >
              <ListItemText primary="About" />
            </ListItemButton>
            <ListItem sx={{ width: "auto", ml: 2 }}>
              <ListItemButton sx={{ textAlign: "center" }} onClick={() => navigate("/contact")} >
                <ListItemText primary="Contact Us" />
              </ListItemButton>
            </ListItem>
          </List>
        </Box>
      </Box>

    </Box>
  );
};

export default Layout;
