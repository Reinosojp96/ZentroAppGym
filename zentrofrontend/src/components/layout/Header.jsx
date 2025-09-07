// src/components/Layout/Header.jsx

import React from 'react';

function Header({ sectionTitle, onToggleSidebar }) {
  return (
    <header className="bg-white shadow-sm border-b">
      <div className="flex items-center justify-between px-6 py-4">
        <div className="flex items-center space-x-4">
          <button onClick={onToggleSidebar} className="text-gray-600 p-2">
            <i className="fas fa-bars"></i>
          </button>
          <button
            id="sidebar-toggle"
            onClick={onToggleSidebar}
            className="text-gray-500 hover:text-gray-700"
          >
            <i className="fas fa-bars text-xl"></i>
          </button>
          <h2 id="section-title" className="text-2xl font-bold text-gray-800">
            {sectionTitle}
          </h2>
        </div>
        <div className="flex items-center space-x-4">
          <div className="relative">
            <button className="relative text-gray-500 hover:text-gray-700">
              <i className="fas fa-bell text-xl"></i>
              <span className="absolute -top-1 -right-1 w-3 h-3 bg-red-500 rounded-full notification-badge"></span>
            </button>
          </div>
          <div className="flex items-center space-x-3">
            <img src="https://via.placeholder.com/40x40" alt="Profile" className="w-10 h-10 rounded-full" />
            <div>
              <p className="text-sm font-medium">Admin User</p>
              <p className="text-xs text-gray-500">Administrador</p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;