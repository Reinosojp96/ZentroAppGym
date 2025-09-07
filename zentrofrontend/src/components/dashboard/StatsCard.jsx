// src/components/Dashboard/StatsCard.jsx

import React from 'react';

function StatsCard({ title, value, detail, icon, bgColor, iconColor }) {
  return (
    <div className="bg-white p-6 rounded-lg card-shadow hover-scale">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-gray-600">{title}</p>
          <p className="text-3xl font-bold text-gray-800">{value}</p>
          <p className="text-sm" style={{ color: iconColor }}>{detail}</p>
        </div>
        <div className={`w-12 h-12 rounded-lg flex items-center justify-center ${bgColor}`}>
          <i className={`${icon} text-xl`} style={{ color: iconColor }}></i>
        </div>
      </div>
    </div>
  );
}

export default StatsCard;