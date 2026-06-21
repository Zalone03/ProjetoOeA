import Status from "../ux/Status.jsx";
import Button from "../ux/Button.jsx";
import { useNavigate } from "react-router-dom";

export default function CardBot({ bot }) {

  const navigate = useNavigate();

  return (
    <div className="bg-white rounded-xl shadow-md p-4 flex flex-col gap-3 min-w-0">

      <h2 className="text-lg font-bold truncate">
        {bot.nome}
      </h2>

      <Status
        status={bot.ultimo_status}
      />

      <p className="text-sm text-gray-500">
        Última execução: {
          bot.ultima_execucao
            ? new Date(bot.ultima_execucao).toLocaleString("pt-BR")
            : "Nunca executado"
        }
      </p>

      <Button
        onClick={() => navigate(`/robos/${bot.id}`)}
      >
        Ver detalhes
      </Button>

    </div>
  );
}