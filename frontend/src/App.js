import WinratePage from "./pages/WinratePage.tsx";

export default function App() {

  const backend_url = process.env.REACT_APP_BACKEND_URL;

  return (
  <WinratePage backend_url = {backend_url}/>
  );
}