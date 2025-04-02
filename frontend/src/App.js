import { Routes, Route } from "react-router-dom";
import WinratePage from "./pages/WinratePage.tsx";
import AccountPage from "./pages/AccountPage.tsx";
import AboutPage from "./pages/AboutPage.tsx";
import ContactPage from "./pages/ContactPage.tsx";
import HomePage from "./pages/HomePage.tsx";
import LoginPage from "./pages/LoginPage.tsx";
export default function App() {

  const backend_url = process.env.REACT_APP_BACKEND_URL;

  return (
    <>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/winrate" element={<WinratePage backend_url={backend_url} />} />
        <Route path="/account" element={<AccountPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/contact" element={<ContactPage />} />
      </Routes>
    </>
  );
}