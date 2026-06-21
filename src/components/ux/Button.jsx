export default function Button({ children, onClick }) {
  return (
    <button
      onClick={onClick}
      className="
        bg-blue-600
        hover:bg-white
        text-white
        hover:text-blue-600
        border
        border-blue-600
        font-medium
        px-4
        py-2
        rounded-lg
        shadow-sm
        transition-all
        duration-200
        cursor-pointer
      "
    >
      {children}
    </button>
  );
}
