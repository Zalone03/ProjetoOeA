import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import Loading from "../components/ui/Loading.jsx";
import RobotInfo from "../components/ui/RobotInfo.jsx";
import ExecutionList from "../components/ui/ExecutionList.jsx";

import Button from "../components/ux/Button.jsx";

import { getBot, getExecutions, getLogs } from "../data/service.js";

export default function DetailsPage() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [bot, setBot] = useState(null);
  const [executions, setExecutions] = useState([]);

  const [activeExecutionId, setActiveExecutionId] = useState(null);
  const [logs, setLogs] = useState([]);
  const [loadingLogs, setLoadingLogs] = useState(false);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([getBot(id), getExecutions(id)])
      .then(([botData, executionsData]) => {
        setBot(botData);
        setExecutions(executionsData);
      })
      .catch((error) => {
        console.error(error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [id]);

  async function handleFetchLogs(executionId) {
    if (activeExecutionId === executionId) {
      setActiveExecutionId(null);
      setLogs([]);

      return;
    }

    setActiveExecutionId(executionId);
    setLoadingLogs(true);
    setLogs([]);

    try {
      const logsData = await getLogs(executionId);

      setLogs(logsData);
    } catch (error) {
      console.error("Erro ao buscar logs:", error);
    } finally {
      setLoadingLogs(false);
    }
  }

  if (loading) {
    return <Loading />;
  }

  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <div className="pb-5">
        <Button onClick={() => navigate("/")}> ← Voltar </Button>
      </div>
      <RobotInfo bot={bot} />

      <ExecutionList
        executions={executions}
        activeExecutionId={activeExecutionId}
        logs={logs}
        loadingLogs={loadingLogs}
        onExecutionClick={handleFetchLogs}
      />
    </div>
  );
}
