import secretsJson from './frontend-secrets.json';
import WinratePage from "./pages/WinratePage.tsx";

function App() {

  // TODO replace w terraform!
  let backend_url = secretsJson.backend_url;

  if(backend_url === "accelerando"){
    backend_url = "http://localhost:8000";
  }

  backend_url += "/tracker";

  return (
    <WinratePage backend_url = {backend_url}></WinratePage>
  );
}

export default App;
