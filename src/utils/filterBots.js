export function filterBots(bots, search) {
  if (!search) return bots;

  const q = search.toLowerCase();

  return bots.filter((bot) => {
    const nome = bot.nome?.toLowerCase() || "";
    const status = bot.ultimo_status?.toLowerCase() || "falha";

    return nome.includes(q) || status.includes(q);
  });
}
