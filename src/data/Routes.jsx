import { BrowserRouter, Routes, Route } from "react-router-dom";

import BotsPage from "../pages/BotsPage.jsx";
import BotDetailsPage from "../pages/DetailsPage.jsx";

export default function AppRoutes() {

  return (
    <BrowserRouter>
      <Routes>

        <Route
          path="/"
          element={<BotsPage/>}
        />

        <Route
          path="/robos/:id"
          element={<BotDetailsPage />}
        />

      </Routes>
    </BrowserRouter>
  );
}