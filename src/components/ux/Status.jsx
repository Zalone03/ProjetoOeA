export default function Status({ status }) {
  const s = status
    ? status.replace("_", " ").charAt(0).toUpperCase() +
      status.slice(1).toLowerCase().replace("_", " ")
    : status;

  if (s === "Sucesso") {
    return (
      <span className="bg-green-100 text-green-700 px-2.5 py-0.5 rounded-full text-xs md:text-sm font-medium border border-green-300 w-max h-10 flex items-center  gap-1 shrink-0">
        ● {s}
      </span>
    );
  } else if (s === "Info" || s === "Debug") {
    return (
      <span className="bg-blue-100 text-blue-700 px-2.5 py-0.5 rounded-full text-xs md:text-sm font-medium border border-blue-300 w-max h-10 flex items-center gap-1 shrink-0">
        ● {s}
      </span>
    );
  } else if (s === "Em andamento" || s === "Parcial") {
    return (
      <span className="bg-amber-100 text-amber-700 px-2.5 py-0.5 rounded-full text-xs md:text-sm font-medium border border-amber-300 w-max h-10 flex items-center gap-1 shrink-0 animate-pulse">
        ● {s}
      </span>
    );
  } else if (s === "Erro" || s === "Warning") {
    return (
      <span className="bg-red-100 text-red-700 px-2.5 py-0.5 rounded-full text-xs md:text-sm font-medium border border-red-300 w-max h-10 flex items-center gap-1 shrink-0">
        ● {s}
      </span>
    );
  } else {
    return (
      <span className="bg-red-100 text-red-700 px-2.5 py-0.5 rounded-full text-xs md:text-sm font-medium border border-red-300 w-max h-10 flex items-center gap-1 shrink-0">
        ● Falha
      </span>
    );
  }
}
