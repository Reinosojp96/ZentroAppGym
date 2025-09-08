// src/components/layout/MainLayout.jsx
import React, { useState } from "react";
import { Outlet } from "react-router-dom";
import Sidebar from "../common/Sidebar";
import Header from "../common/Header";

export default function MainLayout() {
  // controla collapse y pásalo al Sidebar
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Sidebar - fijo */}
      <Sidebar
        collapsed={collapsed}
        onToggle={(next) => setCollapsed(next)}
        // opcional: onNavigate handler si quieres centralizar navegación
      />

      {/* Contenedor principal: header + contenido */}
      <div
        className={`flex-1 min-h-screen transition-all duration-300 ${
          collapsed ? "lg:ml-16" : "lg:ml-64"
        }`}
      >
        <Header />
        <main className="p-6">
          {/* Aquí renderizan las rutas hijas */}
          <Outlet />
        </main>
      </div>
    </div>
  );
}
