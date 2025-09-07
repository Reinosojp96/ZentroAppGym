// src/components/layout/MainLayout.jsx

import React from 'react';
import Sidebar from '../common/Sidebar';
import Header from '../common/Header';

function MainLayout({ children, activeSection, onNavigate }) {
  const getSectionTitle = (section) => {
    switch(section) {
      case 'dashboard':
        return 'Dashboard';
      case 'clientes':
        return 'Gestión de Clientes';
      case 'pagos':
        return 'Pagos';
      case 'clases':
        return 'Clases';
      case 'reportes':
        return 'Reportes';
      case 'recepcion':
        return 'Recepción';
      case 'ajustes':
        return 'Ajustes';
      default:
        return 'Dashboard';
    }
  };

  const sectionTitle = getSectionTitle(activeSection);

  return (
    <div className="flex bg-gray-100 min-h-screen">
      <Sidebar activeSection={activeSection} onNavigate={onNavigate} />
      <div className="flex-1 flex flex-col">
        <Header sectionTitle={sectionTitle} />
        <main className="flex-1 p-6 overflow-y-auto">
          {children}
        </main>
      </div>
    </div>
  );
}

export default MainLayout;