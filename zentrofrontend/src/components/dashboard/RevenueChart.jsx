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

export default function RevenueChart({ title = "Ingresos (últimos meses)" }) {
  const data = {
    labels: ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    datasets: [
      {
        label: "Ingresos",
        data: [12000, 19000, 15000, 25000, 22000, 30000],
        borderColor: "rgb(99,102,241)",
        backgroundColor: "rgba(99,102,241,0.08)",
        pointBackgroundColor: "rgb(99,102,241)",
        pointRadius: 4,
        tension: 0.35,
        fill: true,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false, // importante: permitir que ocupe la altura del contenedor
    plugins: {
      legend: { display: false },
      tooltip: { mode: "index", intersect: false },
    },
    interaction: { mode: "nearest", axis: "x", intersect: false },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          // añade formato de moneda
          callback: function (value) {
            // value puede venir como número; toLocaleString mejora la lectura
            return "$" + Number(value).toLocaleString();
          },
        },
        grid: { color: "rgba(200,200,200,0.06)" },
      },
      x: {
        grid: { display: false },
      },
    },
  };

  return (
    <div className="bg-white p-6 rounded-lg card-shadow hover-scale">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
        {/* si quieres añadir un select de rango lo puedes poner aquí */}
      </div>

      {/* contenedor que controla la altura del canvas */}
      <div className="w-full" style={{ height: 320 }}>
        <Line data={data} options={options} />
      </div>
    </div>
  );
}

