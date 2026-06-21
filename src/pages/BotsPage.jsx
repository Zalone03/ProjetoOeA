import { useEffect, useState } from "react";
import { getBots, getStatus } from "../data/service.js";

import CardSet from "../components/ui/CardSet.jsx";
import SummaryStats from "../components/ui/SummaryStats.jsx";

import Loading from "../components/ui/Loading.jsx";
import NavBar from "../components/ux/NavBar.jsx";

import Header from "../components/ux/Header.jsx";
import Filter from "../components/ux/Filter.jsx";

import { filterBots } from "../utils/filterBots";

export default function BotsPage() {
  const [bots, setBots] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");
  const filteredBots = filterBots(bots, search);

  useEffect(() => {
    Promise.all([getBots(), getStatus()])
      .then(([botsData, statsData]) => {
        console.log(botsData);
        setBots(botsData);
        setStats(statsData);
      })
      .catch((error) => {
        console.error(error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <Loading />;
  }

  return (
    <div className="min-h-screen flex flex-col md:flex-row bg-slate-100">
      <NavBar />

      <main className="flex-1 p-6">
        <div className="flex flex-col lg:flex-row gap-4 mb-6">
          <div className="w-full lg:w-3/4">
            <Header />
          </div>
          <Filter search={search} setSearch={setSearch} />
        </div>

        <SummaryStats stats={stats} />

        <CardSet bots={filteredBots} />
      </main>
    </div>
  );
}
