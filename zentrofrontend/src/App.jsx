// src/App.jsx

import React, { useState } from 'react';
import MainLayout from './components/layout/MainLayout';
// Importa todos los componentes necesarios
import StatsCard from './components/dashboard/StatsCard';
import RevenueChart from './components/dashboard/RevenueChart';
import QuickAccess from './components/dashboard/QuickAccess';
import CustomersTable from './components/customers/CustomersTable';
import NewCustomerForm from './components/customers/NewCustomerForm';

function App() {
  const [activeSection, setActiveSection] = useState('dashboard');
  const [showNewCustomerForm, setShowNewCustomerForm] = useState(false);

  // La función handleNavigate ahora se define aquí para cambiar el estado
  const handleNavigate = (section) => {
    setActiveSection(section);
    // Asegúrate de resetear el estado del formulario cuando cambies de sección
    setShowNewCustomerForm(false);
  };

  const renderSection = () => {
    switch (activeSection) {
      case 'dashboard':
        return (
          <div id="dashboard-section" className="section-content">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
              <StatsCard
                title="Clientes Activos"
                value="1,247"
                detail="+12% este mes"
                icon="fas fa-users"
                bgColor="bg-blue-100"
                iconColor="#3b82f6" // blue-600
              />
              <StatsCard
                title="Ingresos del Día"
                value="$2,450"
                detail="+8% ayer"
                icon="fas fa-dollar-sign"
                bgColor="bg-green-100"
                iconColor="#22c55e" // green-600
              />
              <StatsCard
                title="Clases Hoy"
                value="24"
                detail="85% ocupado"
                icon="fas fa-calendar-alt"
                bgColor="bg-purple-100"
                iconColor="#a855f7" // purple-600
              />
              <StatsCard
                title="Notificaciones"
                value="7"
                detail="3 urgentes"
                icon="fas fa-exclamation-triangle"
                bgColor="bg-red-100"
                iconColor="#ef4444" // red-600
              />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <RevenueChart />
              <QuickAccess />
            </div>
          </div>
        );
      case 'clientes':
        return (
          <div id="clientes-section" className="section-content">
            <div className="bg-white rounded-lg card-shadow">
              <div className="p-6">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-lg font-semibold">Gestión de Clientes</h3>
                  <button 
                    onClick={() => setShowNewCustomerForm(true)}
                    className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
                  >
                    <i className="fas fa-plus mr-2"></i>Nuevo Cliente
                  </button>
                </div>
                {showNewCustomerForm ? (
                  <NewCustomerForm onClose={() => setShowNewCustomerForm(false)} />
                ) : (
                  <>
                    <div className="mb-4 flex space-x-4">
                      <input type="text" placeholder="Buscar cliente..." className="flex-1 px-4 py-2 border rounded-lg" />
                      <select className="px-4 py-2 border rounded-lg">
                        <option>Todos los estados</option>
                        <option>Activo</option>
                        <option>Inactivo</option>
                      </select>
                    </div>
                    <CustomersTable />
                  </>
                )}
              </div>
            </div>
          </div>
        );
      case 'pagos':
        return <div id="pagos-section" className="section-content">Gestión de Pagos...</div>;
      case 'clases':
        return <div id="clases-section" className="section-content">Horarios de Clases...</div>;
      case 'reportes':
        return <div id="reportes-section" className="section-content">Generación de Reportes...</div>;
      case 'recepcion':
        return <div id="recepcion-section" className="section-content">Control de Acceso...</div>;
      case 'ajustes':
        return <div id="ajustes-section" className="section-content">Configuración de la Aplicación...</div>;
      default:
        return null;
    }
  };

  return (
    <MainLayout activeSection={activeSection} onNavigate={handleNavigate}>
      {renderSection()}
    </MainLayout>
  );
}

export default App;