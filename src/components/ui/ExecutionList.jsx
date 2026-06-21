import ExecutionItem from "./ExecutionItem";

export default function ExecutionList({
  executions,
  activeExecutionId,
  logs,
  loadingLogs,
  onExecutionClick,
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm p-6 border border-slate-200">
      <h2 className="text-xl font-bold mb-4">Execuções do Robô</h2>

      <div className="flex flex-col gap-3">
        {executions.map((exec) => (
          <ExecutionItem
            key={exec.id}
            exec={exec}
            isOpened={activeExecutionId === exec.id}
            logs={logs}
            loadingLogs={loadingLogs}
            onClick={() => onExecutionClick(exec.id)}
          />
        ))}
      </div>
    </div>
  );
}
