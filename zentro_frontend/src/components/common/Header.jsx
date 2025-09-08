// src/components/common/Header.jsx
import React, { useEffect, useRef, useState } from "react";

/**
 * Props opcionales:
 * - onToggleSidebar: () => void
 * - onSearch: (query) => void  // se llama con debounce 300ms
 * - notifications: [{ id, title, body, time, read }]
 * - user: { name, role, avatarUrl }
 * - onSignOut: () => void
 */
export default function Header({
  onToggleSidebar,
  onSearch,
  notifications = [
    { id: 1, title: "Pago recibido", body: "Pago de María por $45", time: "2h", read: false },
    { id: 2, title: "Nueva reserva", body: "Carlos reservó Zumba", time: "5h", read: false },
    { id: 3, title: "Membresía próxima", body: "Vence: 15/09 - Juan", time: "1d", read: true },
  ],
  user = { name: "Admin User", role: "Administrador", avatarUrl: "https://via.placeholder.com/40" },
  onSignOut,
}) {
  const [query, setQuery] = useState("");
  const [debounced, setDebounced] = useState("");
  const [openNotif, setOpenNotif] = useState(false);
  const [openProfile, setOpenProfile] = useState(false);
  const notifRef = useRef(null);
  const profileRef = useRef(null);
  const searchRef = useRef(null);

  // Debounce search and call onSearch
  useEffect(() => {
    const t = setTimeout(() => setDebounced(query), 300);
    return () => clearTimeout(t);
  }, [query]);

  useEffect(() => {
    if (typeof onSearch === "function") onSearch(debounced);
  }, [debounced, onSearch]);

  // Close dropdowns on outside click or ESC
  useEffect(() => {
    function handleClick(e) {
      if (notifRef.current && !notifRef.current.contains(e.target)) setOpenNotif(false);
      if (profileRef.current && !profileRef.current.contains(e.target)) setOpenProfile(false);
    }
    function handleKey(e) {
      if (e.key === "Escape") {
        setOpenNotif(false);
        setOpenProfile(false);
      }
    }
    window.addEventListener("click", handleClick);
    window.addEventListener("keydown", handleKey);
    return () => {
      window.removeEventListener("click", handleClick);
      window.removeEventListener("keydown", handleKey);
    };
  }, []);

  const unreadCount = notifications.filter((n) => !n.read).length;

  return (
    <header className="bg-white border-b shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Left: toggle + search */}
          <div className="flex items-center gap-4">
            <button
              onClick={() => onToggleSidebar && onToggleSidebar()}
              className="p-2 rounded-md hover:bg-gray-100 text-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              aria-label="Toggle sidebar"
            >
              <i className="fas fa-bars text-lg" />
            </button>

            <div className="relative w-[520px] max-w-full">
              <label htmlFor="search" className="sr-only">Buscar</label>
              <div className="flex items-center bg-white border rounded-lg shadow-sm overflow-hidden">
                <span className="pl-3 pr-2 text-gray-400"><i className="fas fa-search" /></span>
                <input
                  ref={searchRef}
                  id="search"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Buscar..."
                  className="w-full py-2 pr-3 text-sm placeholder-gray-400 focus:outline-none focus:ring-0"
                />
                {query && (
                  <button
                    onClick={() => setQuery("")}
                    className="px-3 text-gray-400 hover:text-gray-600"
                    aria-label="Limpiar búsqueda"
                  >
                    <i className="fas fa-times" />
                  </button>
                )}
              </div>
              {/* sugerencia / hint */}
            </div>
          </div>

          {/* Right: actions */}
          <div className="flex items-center gap-4">
            {/* Quick action button (opcional) */}
            <div className="hidden md:block">
              <button className="inline-flex items-center gap-2 px-3 py-2 rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 shadow-sm">
                <i className="fas fa-plus" />
                <span className="text-sm font-medium">Nuevo</span>
              </button>
            </div>

            {/* Notifications */}
            <div className="relative" ref={notifRef}>
              <button
                onClick={(e) => { e.stopPropagation(); setOpenNotif((s) => !s); }}
                className="relative p-2 rounded-full hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                aria-haspopup="true"
                aria-expanded={openNotif}
                aria-label="Notificaciones"
              >
                <i className="fas fa-bell text-gray-600 text-lg" />
                {unreadCount > 0 && (
                  <span className="absolute -top-1 -right-1 inline-flex items-center justify-center px-1.5 py-0.5 rounded-full text-xs font-semibold bg-red-500 text-white">
                    {unreadCount}
                  </span>
                )}
              </button>

              {openNotif && (
                <div
                  className="absolute right-0 mt-2 w-80 bg-white border rounded-lg shadow-lg z-50 overflow-hidden"
                  role="menu"
                  aria-label="Lista de notificaciones"
                  onClick={(e) => e.stopPropagation()}
                >
                  <div className="p-3 border-b flex items-center justify-between">
                    <strong>Notificaciones</strong>
                    <button className="text-sm text-indigo-600 hover:underline">Marcar todas</button>
                  </div>
                  <ul className="max-h-64 overflow-auto">
                    {notifications.map((n) => (
                      <li key={n.id} className={`p-3 hover:bg-gray-50 ${n.read ? "" : "bg-gray-50"}`}>
                        <div className="flex items-start justify-between">
                          <div>
                            <div className="text-sm font-medium">{n.title}</div>
                            <div className="text-xs text-gray-500">{n.body}</div>
                          </div>
                          <div className="text-xs text-gray-400 ml-3">{n.time}</div>
                        </div>
                      </li>
                    ))}
                    {notifications.length === 0 && <li className="p-3 text-sm text-gray-500">Sin notificaciones</li>}
                  </ul>
                  <div className="p-2 border-t text-center">
                    <button className="text-sm text-indigo-600 hover:underline">Ver todas</button>
                  </div>
                </div>
              )}
            </div>

            {/* Profile */}
            <div className="relative" ref={profileRef}>
              <button
                onClick={(e) => { e.stopPropagation(); setOpenProfile((s) => !s); }}
                className="flex items-center gap-2 rounded-md px-2 py-1 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                aria-haspopup="true"
                aria-expanded={openProfile}
              >
                <img src={user.avatarUrl} alt="Avatar" className="w-8 h-8 rounded-full object-cover" />
                <div className="hidden sm:flex flex-col items-start">
                  <span className="text-sm font-medium text-gray-700">{user.name}</span>
                  <span className="text-xs text-gray-400">{user.role}</span>
                </div>
                <i className="fas fa-caret-down text-gray-500 ml-1" />
              </button>

              {openProfile && (
                <div
                  className="absolute right-0 mt-2 w-48 bg-white border rounded-lg shadow-lg z-50 overflow-hidden"
                  role="menu"
                >
                  <button className="w-full px-4 py-2 text-left hover:bg-gray-50">Perfil</button>
                  <button className="w-full px-4 py-2 text-left hover:bg-gray-50">Ajustes</button>
                  <div className="border-t" />
                  <button
                    onClick={() => onSignOut ? onSignOut() : (window.location.href = "/logout")}
                    className="w-full px-4 py-2 text-left text-red-600 hover:bg-gray-50"
                  >
                    Cerrar sesión
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
