import {Routes, Route} from "react-router-dom"
import Contact from "./components/Contact"
import Home from "./components/Home"
import Jacksonville from "./components/Jacksonville";
import Miami from "./components/Miami";

function App() {
  return (
    <Routes>
      <Route path = "/" element= {<Home />}></Route>
      <Route path = "contact" element= {<Contact />}></Route>
      <Route path = "jax" element= {<Jacksonville />}></Route>
      <Route path = "miami" element= {<Miami />}></Route>
    </Routes>
  );
}

export default App;
