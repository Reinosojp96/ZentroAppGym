// src/components/ui/FloatingMenu.jsx
import React, { useState } from "react";

export default function FloatingMenu() {
  const [open, setOpen] = useState(false);

  return (
    <div className="fixed right-6 bottom-6 z-50">
      <div className="flex flex-col items-end space-y-2">
        {open && (
          <div className="bg-white shadow-lg rounded-lg overflow-hidden w-52">
            <button className="w-full p-3 text-left hover:bg-gray-100">Contacto rápido</button>
            <button className="w-full p-3 text-left hover:bg-gray-100">Enviar reporte</button>
            <button className="w-full p-3 text-left hover:bg-gray-100">Ayuda</button>
          </div>
        )}

        <button
          onClick={() => setOpen((s) => !s)}
          className="bg-blue-600 text-white w-14 h-14 rounded-full shadow-lg flex items-center justify-center hover:bg-blue-700 transition"
          aria-label="Abrir menú"
        >
          <i className={`fas ${open ? "fa-times" : "fa-ellipsis-v"}`}></i>
        </button>
      </div>
    </div>
  );
}
