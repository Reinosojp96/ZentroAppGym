// src/components/common/Header.jsx

import React from 'react';

function Header() {
  return (
    <header className="bg-white p-4 flex items-center justify-between shadow-sm sticky top-0 z-50">
      {/* Barra de Búsqueda */}
      <div className="relative w-1/3">
        <input 
          type="text" 
          placeholder="Buscar..." 
          className="w-full pl-10 pr-4 py-2 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <i className="fas fa-search text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2"></i>
      </div>

      {/* Íconos de Notificaciones y Usuario */}
      <div className="flex items-center space-x-4">
        <button className="text-gray-600 hover:text-blue-600 relative">
          <i className="fas fa-bell text-xl"></i>
          <span className="absolute top-0 right-0 inline-flex items-center justify-center px-2 py-1 text-xs font-bold leading-none text-red-100 bg-red-600 rounded-full">3</span>
        </button>
        <div className="relative">
          <button className="flex items-center space-x-2 text-sm font-medium text-gray-700 hover:text-blue-600">
            <img src="https://via.placeholder.com/40x40" alt="Avatar" className="w-10 h-10 rounded-full" />
            <span>Carlos R.</span>
            <i className="fas fa-chevron-down text-xs"></i>
          </button>
        </div>
      </div>
    </header>
  );
}

export default Header;