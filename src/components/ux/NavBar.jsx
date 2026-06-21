import botImg from "../../assets/bot.webp";

export default function Navbar() {
  return (
    <aside
      className="
        w-full
        md:w-20
        bg-slate-900
        text-white
        p-4
        shadow-xl
      "
    >
      <nav
        className="
          flex
          flex-row
          md:flex-col
          justify-center
          items-center
          gap-4
        "
      >
        <button
          className="
            p-2
            rounded-xl
            hover:bg-slate-800
            transition
          "
        >
          <img
            src={botImg}
            alt="Bot"
            className="
              w-10
              h-10
              md:w-12
              md:h-12
              object-contain
            "
          />
        </button>
      </nav>
    </aside>
  );
}
