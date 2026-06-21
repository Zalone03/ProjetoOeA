export default function Loading() {
  return (
    <div className="min-h-screen flex items-center justify-center gap-2">
      <div className="w-4 h-4 bg-blue-500 rounded-full animate-bounce"></div>

      <div
        className="w-4 h-4 bg-blue-500 rounded-full animate-bounce"
        style={{ animationDelay: "0.15s" }}
      ></div>

      <div
        className="w-4 h-4 bg-blue-500 rounded-full animate-bounce"
        style={{ animationDelay: "0.30s" }}
      ></div>
    </div>
  );
}
