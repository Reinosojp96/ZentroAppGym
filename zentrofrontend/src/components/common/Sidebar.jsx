// src/components/common/Sidebar.jsx

import React from 'react';

function Sidebar({ activeSection, onNavigate }) {
  const navItems = [
    { id: 'dashboard', name: 'Dashboard', icon: 'fas fa-tachometer-alt' },
    { id: 'clientes', name: 'Clientes', icon: 'fas fa-users' },
    { id: 'pagos', name: 'Pagos', icon: 'fas fa-credit-card' },
    { id: 'clases', name: 'Clases', icon: 'fas fa-dumbbell' },
    { id: 'reportes', name: 'Reportes', icon: 'fas fa-chart-line' },
    { id: 'recepcion', name: 'Recepción', icon: 'fas fa-door-open' },
    { id: 'ajustes', name: 'Ajustes', icon: 'fas fa-cog' },
  ];

  return (
    <aside className="w-64 bg-gray-800 text-white min-h-screen p-4 flex flex-col justify-between">
      <div>
        <h2 className="text-2xl font-bold mb-8 text-center text-blue-400">Gym Manager</h2>
        <nav>
          <ul>
            {navItems.map((item) => (
              <li key={item.id} className="mb-2">
                <button
                  onClick={() => onNavigate(item.id)}
                  className={`w-full flex items-center p-3 rounded-lg hover:bg-gray-700 transition-colors duration-200 ${activeSection === item.id ? 'bg-blue-600' : ''}`}
                >
                  <i className={`${item.icon} mr-3`}></i>
                  <span>{item.name}</span>
                </button>
              </li>
            ))}
          </ul>
        </nav>
      </div>
      <div className="mt-8 border-t border-gray-700 pt-4">
        <button className="w-full flex items-center p-3 text-red-400 rounded-lg hover:bg-gray-700">
          <i className="fas fa-sign-out-alt mr-3"></i>
          <span>Cerrar Sesión</span>
        </button>
      </div>
    </aside>
  );
}

export default Sidebar;