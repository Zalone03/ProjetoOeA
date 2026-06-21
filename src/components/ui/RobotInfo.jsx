export default function RobotInfo({ bot }) {
  return (
    <div className="bg-white rounded-xl shadow-sm p-6 mb-6 border border-slate-200">
      <h1 className="text-3xl font-bold text-slate-900 mb-2">{bot.nome}</h1>

      <p className="text-slate-600 mb-4">{bot.descricao}</p>

      <p className="text-xs text-slate-400">
        Cadastrado em: {new Date(bot.criado_em).toLocaleDateString("pt-BR")}
      </p>
    </div>
  );
}
