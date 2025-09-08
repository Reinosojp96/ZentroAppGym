// src/components/layout/MainLayout.jsx
import React, { useState } from "react";
import Sidebar from "../common/Sidebar";
import Header from "../common/Header";
import FloatingMenu from "../ui/FloatingMenu"; // opcional si lo usas

export default function MainLayout({ children }) {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div className="min-h-screen flex bg-gray-50">
      {/* Sidebar fija */}
      <Sidebar
        collapsed={collapsed}
        onToggle={(next) => setCollapsed((s) => (typeof next === "boolean" ? next : !s))}
      />

      {/* Contenido: margen a la izquierda igual al ancho de la sidebar */}
      <div
        className={`flex-1 transition-all duration-300 ${collapsed ? "ml-16" : "ml-64"}`}
        style={{ minHeight: "100vh" }}
      >
        {/* Header (no fixed) — si haces fixed ajusta el padding-top) */}
        <Header onToggleSidebar={() => setCollapsed((s) => !s)} />

        {/* main con padding si quieres */}
        <main className="p-6">
          {children}
        </main>
      </div>

      {/* Floating menu opcional (esquina inferior derecha) */}
      <FloatingMenu />
    </div>
  );
}
