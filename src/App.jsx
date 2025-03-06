import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false);
    }, 3000); // Длительность анимации

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="app">
      {loading ? <div className="star"></div> : <div className="menu show-menu">Выбор скина</div>}
    </div>
  );
}

export default App;