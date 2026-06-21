import Status from "../ux/Status";
import LogsList from "./LogsList";

export default function ExecutionItem({
  exec,
  isOpened,
  logs,
  loadingLogs,
  onClick,
}) {
  return (
    <div className="border border-slate-200 rounded-lg overflow-hidden">
      <div
        onClick={onClick}
        className="
          p-4
          flex
          justify-between
          items-center
          cursor-pointer
          hover:bg-slate-50
        "
      >
        <div className="flex gap-4">
          <Status status={exec.status} />

          <div>
            <p className="text-sm font-medium">
              {new Date(exec.iniciado_em).toLocaleString("pt-BR")}
            </p>

            <span className="text-xs text-blue-600">
              {isOpened ? "Ocultar logs" : "Ver logs"}
            </span>
          </div>
        </div>

        <div>{exec.duracao_segundos}s</div>
      </div>

      {isOpened && (
        <div className="bg-slate-50 border-t p-4">
          {" "}
          {loadingLogs ? <p>Carregando...</p> : <LogsList logs={logs} />}{" "}
        </div>
      )}
    </div>
  );
}
