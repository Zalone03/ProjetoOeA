export default function Filter({ search, setSearch }) {
  return (
    <div className="w-full lg:w-1/4 bg-white rounded-xl shadow-sm p-6">
      <h2 className="font-semibold text-slate-700 mb-3">Filtros</h2>

      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Buscar robô..."
        className="
          w-full
          border
          rounded-lg
          p-2
          outline-none
        "
      />
    </div>
  );
}
