// src/components/Customers/CustomersTable.jsx

import React from 'react';

function CustomersTable() {
  const customers = [
    { id: '#001', name: 'Juan Pérez', doc: '12345678', contact: '3001234567', membership: 'Pro Mensual', status: 'Activo', img: 'https://via.placeholder.com/32x32' },
    // Aquí podrías agregar más clientes para poblar la tabla
  ];

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead>
          <tr className="bg-gray-50">
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Documento</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Contacto</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Membresía</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Estado</th>
            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {customers.map((customer) => (
            <tr key={customer.id}>
              <td className="px-6 py-4 whitespace-nowrap">{customer.id}</td>
              <td className="px-6 py-4 whitespace-nowrap">
                <div className="flex items-center">
                  <img src={customer.img} alt={customer.name} className="w-8 h-8 rounded-full mr-2" />
                  {customer.name}
                </div>
              </td>
              <td className="px-6 py-4 whitespace-nowrap">{customer.doc}</td>
              <td className="px-6 py-4 whitespace-nowrap">{customer.contact}</td>
              <td className="px-6 py-4 whitespace-nowrap">{customer.membership}</td>
              <td className="px-6 py-4 whitespace-nowrap">
                <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                  {customer.status}
                </span>
              </td>
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <button className="text-blue-600 hover:text-blue-900 mr-2">Editar</button>
                <button className="text-red-600 hover:text-red-900">Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default CustomersTable;