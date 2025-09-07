// src/components/Layout/Sidebar.jsx

import React from 'react';

function Sidebar({ isCollapsed, activeSection, onNavigate }) {
  const navItems = [
    { name: 'Dashboard', icon: 'fas fa-home', section: 'dashboard' },
    { name: 'Clientes', icon: 'fas fa-users', section: 'clientes' },
    { name: 'Recepción', icon: 'fas fa-id-card', section: 'recepcion' },
    { name: 'Membresías', icon: 'fas fa-credit-card', section: 'membresias' },
    { name: 'Clases', icon: 'fas fa-calendar-alt', section: 'clases' },
    { name: 'Entrenadores', icon: 'fas fa-user-tie', section: 'entrenadores' },
    { name: 'Rutinas', icon: 'fas fa-clipboard-list', section: 'rutinas' },
    { name: 'Nutrición', icon: 'fas fa-apple-alt', section: 'nutricion' },
    { name: 'Tienda', icon: 'fas fa-store', section: 'tienda' },
    { name: 'Incidentes', icon: 'fas fa-exclamation-triangle', section: 'incidentes' },
    { name: 'Administración', icon: 'fas fa-cog', section: 'admin' },
    { name: 'Configuración', icon: 'fas fa-sliders-h', section: 'configuracion' },
    { name: 'Ayuda', icon: 'fas fa-question-circle', section: 'ayuda' },
  ];

  return (
    <div
      id="sidebar"
      className={`fixed left-0 top-0 h-screen overflow-y-auto bg-gray-900 text-white sidebar-transition z-30 ${isCollapsed ? 'w-16' : 'w-64'}`}
    >
      <div className="p-6">
        <div className="flex items-center space-x-3 mb-8">
          <div className="w-10 h-10 gradient-bg rounded-lg flex items-center justify-center">
            <i className="fas fa-dumbbell text-white"></i>
          </div>
          <h1 className={`text-xl font-bold ${isCollapsed ? 'hidden' : ''}`}>Zentro</h1>
        </div>
        <nav className="space-y-2">
          {navItems.map((item) => (
            <a
              key={item.section}
              href="#"
              onClick={() => onNavigate(item.section, item.name)}
              className={`nav-item flex items-center space-x-3 px-4 py-3 rounded-lg hover:bg-gray-800 ${activeSection === item.section ? 'bg-gray-800' : ''}`}
            >
              <i className={item.icon}></i>
              <span className={isCollapsed ? 'hidden' : ''}>{item.name}</span>
            </a>
          ))}
        </nav>
      </div>
    </div>
  );
}

export default Sidebar;