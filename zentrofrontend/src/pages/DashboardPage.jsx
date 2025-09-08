// src/pages/DashboardPage.jsx  (o en el componente de dashboard que uses)
import React from "react";
import RevenueChart from "../components/dashboard/RevenueChart";
import QuickAccess from "../components/Dashboard/QuickAccess";
import StatsCard from "../components/Dashboard/StatsCard"; // si usas varias stat cards

export default function DashboardPage() {
  return (
    <div className="p-6">
      {/* estadísticas arriba */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
        <StatsCard title="Clientes Activos" value="1,247" detail="+12% este mes" icon="fas fa-user-friends" bgColor="bg-blue-50" iconColor="#2563EB"/>
        <StatsCard title="Ingresos del Día" value="$2,450" detail="+8% ayer" icon="fas fa-dollar-sign" bgColor="bg-green-50" iconColor="#16A34A"/>
        <StatsCard title="Clases Hoy" value="24" detail="85% ocupado" icon="fas fa-calendar-alt" bgColor="bg-purple-50" iconColor="#8B5CF6"/>
        <StatsCard title="Notificaciones" value="7" detail="3 urgentes" icon="fas fa-exclamation-triangle" bgColor="bg-red-50" iconColor="#EF4444"/>
      </div>

      {/* main grid: chart (2/3) + quick access (1/3) */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-start">
        <div className="lg:col-span-2">
          <RevenueChart />
        </div>

        <div className="lg:col-span-1">
          <QuickAccess />
        </div>
      </div>
    </div>
  );
}
