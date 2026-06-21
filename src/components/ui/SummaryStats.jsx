export default function SummaryStats({ stats }) {
  if (!stats) return null;
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
      <div className="bg-white rounded-xl shadow-md p-3 min-w-0 border-l-4 border-green-500 flex items-center justify-between">
        <p className="text-xs font-semibold uppercase tracking-wider truncate">
          Ativos
        </p>
        <p className="text-xl font-bold text-slate-800">
          {stats.total_robos_ativos}
        </p>
      </div>
      <div className="bg-white rounded-xl shadow-md p-3 min-w-0 border-l-4 border-blue-500 flex items-center justify-between">
        <p className="text-xs font-semibold uppercase tracking-wider truncate">
          Rodando
        </p>
        <p className="text-xl font-bold text-blue-600 animate-pulse">
          {stats.robos_em_execucao_agora}
        </p>
      </div>
      <div className="bg-white rounded-xl shadow-md p-3 min-w-0 border-l-4 border-gray-500 flex items-center justify-between">
        <p className="text-xs font-semibold uppercase tracking-wider truncate">
          Execuções (24h)
        </p>
        <p className="text-xl font-bold text-slate-800">
          {stats.execucoes_24h}
        </p>
      </div>
      <div className="bg-white rounded-xl shadow-md p-3 min-w-0 border-l-4 border-red-500 flex items-center justify-between">
        <p className="text-xs font-semibold uppercase tracking-wider truncate">
          Falhas (24h)
        </p>
        <p className="text-xl font-bold text-red-600">{stats.falhas_24h}</p>
      </div>
    </div>
  );
}
