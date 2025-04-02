import React from "react";
import { Box, Typography } from "@mui/material";
import Layout from "./Layout.tsx";

const HomePage: React.FC = () => {
    return (
        <Layout>
            <Box
                sx={{
                    textAlign: "center",
                    pt: 2,  // Adds padding at the top
                    minHeight: "100vh", // Ensures it takes full page height
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                }}
            >
                <Typography variant="h3">You are at the Home Page</Typography>
            </Box>
        </Layout>
    );
};

export default HomePage;
