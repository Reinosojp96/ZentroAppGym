// src/components/dashboard/RevenueChart.jsx
import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

// registra lo que uses
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function RevenueChart() {
  const data = {
    labels: ['Ene','Feb','Mar','Abr','May','Jun'],
    datasets: [
      {
        label: 'Ingresos',
        data: [12000,19000,15000,25000,22000,30000],
        borderColor: 'rgb(99,102,241)',
        backgroundColor: 'rgba(99,102,241,0.1)',
        tension: 0.4,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { callback: (v) => '$' + v.toLocaleString() },
      },
    },
  };

  return (
    <div className="relative h-64">
      <Line data={data} options={options} />
    </div>
  );
}
