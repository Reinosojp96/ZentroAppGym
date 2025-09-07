// src/components/Dashboard/QuickAccess.jsx

import React from 'react';

function QuickAccess() {
  const quickActions = [
    { name: 'Nuevo Cliente', icon: 'fas fa-user-plus', color: 'text-blue-600' },
    { name: 'Registrar Pago', icon: 'fas fa-credit-card', color: 'text-green-600' },
    { name: 'Reservar Clase', icon: 'fas fa-calendar-plus', color: 'text-purple-600' },
    { name: 'Exportar Reporte', icon: 'fas fa-file-export', color: 'text-orange-600' },
  ];

  return (
    <div className="bg-white p-6 rounded-lg card-shadow">
      <h3 className="text-lg font-semibold mb-4">Accesos Rápidos</h3>
      <div className="grid grid-cols-2 gap-4">
        {quickActions.map((action) => (
          <button key={action.name} className="p-4 border rounded-lg hover:bg-gray-50 text-center">
            <i className={`${action.icon} text-2xl ${action.color} mb-2`}></i>
            <p className="text-sm">{action.name}</p>
          </button>
        ))}
      </div>
    </div>
  );
}

export default QuickAccess;