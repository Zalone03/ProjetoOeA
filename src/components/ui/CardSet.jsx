import CardBot from "./CardBot.jsx";

export default function CardSet({ bots }) {

  return (
    <div
      className="
        bg-white
        rounded-xl
        shadow-sm
        p-6
        h-[70vh]
        overflow-y-auto
      "
    >
      <div className="grid gap-4 grid-cols-1 md:grid-cols-2 2xl:grid-cols-3">

        {bots.map((bot) => (
          <CardBot
            key={bot.id}
            bot={bot}
          />
        ))}

      </div>
    </div>
  );
}