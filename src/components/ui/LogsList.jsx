import Status from "../ux/Status";

export default function LogsList({ logs }) {
  if (logs.length === 0) {
    return <p className="text-slate-400 text-xs">Nenhum log registrado.</p>;
  }

  return (
    <div className="flex flex-col gap-2">
      {logs.map((log) => (
        <div
          key={log.id}
          className="
            flex
            gap-3
            py-2
            border-b
            border-slate-100
          "
        >
          <span className="text-xs text-slate-400 font-mono">
            {new Date(log.criado_em).toLocaleTimeString("pt-BR")}
          </span>

          <Status status={log.nivel} />

          <span className="text-slate-700">{log.mensagem}</span>
        </div>
      ))}
    </div>
  );
}
