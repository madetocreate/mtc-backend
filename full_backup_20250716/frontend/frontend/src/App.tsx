import React from "react";

export default function App() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white p-4">
      <h1 className="mb-4 text-3xl font-bold">Aion Chat Interface</h1>
      <textarea
        rows={5}
        maxLength={1000}
        placeholder="Schreibe deine Nachricht an Aion..."
        className="w-full max-w-xl p-3 mb-4 text-black rounded"
      />
      <button className="px-6 py-2 mb-4 font-semibold text-white bg-blue-600 rounded hover:bg-blue-700">
        Absenden
      </button>
      <div className="w-full max-w-xl p-4 bg-gray-800 rounded min-h-[150px] whitespace-pre-wrap">
        Antwort erscheint hier...
      </div>
    </div>
  );
}
