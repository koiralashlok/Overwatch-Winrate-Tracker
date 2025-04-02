import React, { useState } from "react";
// import { login } from "../services/authService";
import { Box, Typography } from "@mui/material";

const LoginPage = ({ setUser }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = async (e) => {
        // e.preventDefault();
        // try {
        //     const userData = await login(username, password);
        //     setUser(userData.user);
        // } catch (err) {
        //     setError(err);
        // }
    };

    return (
        <Box sx={{ mx: 'auto', width: 200 }}>
            <Typography variant="h3">Login</Typography>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <form onSubmit={handleLogin}>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Login</button>
            </form>
        </Box>
    );
};

export default LoginPage;
