// src/components/Customers/NewCustomerForm.jsx

import React from 'react';

function NewCustomerForm({ onClose }) {
  return (
    <div className="bg-white p-6 rounded-lg card-shadow">
      <h3 className="text-lg font-semibold mb-4">Añadir Nuevo Cliente</h3>
      <form>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="mb-4">
            <label htmlFor="name" className="block text-sm font-medium text-gray-700">Nombre Completo</label>
            <input type="text" id="name" name="name" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm" />
          </div>
          <div className="mb-4">
            <label htmlFor="document" className="block text-sm font-medium text-gray-700">Documento</label>
            <input type="text" id="document" name="document" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm" />
          </div>
          <div className="mb-4">
            <label htmlFor="contact" className="block text-sm font-medium text-gray-700">Teléfono/WhatsApp</label>
            <input type="text" id="contact" name="contact" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm" />
          </div>
          <div className="mb-4">
            <label htmlFor="membership" className="block text-sm font-medium text-gray-700">Tipo de Membresía</label>
            <select id="membership" name="membership" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm">
              <option>Pro Mensual</option>
              <option>Básico Semanal</option>
              <option>Anual Premium</option>
            </select>
          </div>
        </div>
        <div className="flex justify-end space-x-2 mt-4">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300"
          >
            Cancelar
          </button>
          <button
            type="submit"
            className="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700"
          >
            Guardar Cliente
          </button>
        </div>
      </form>
    </div>
  );
}

export default NewCustomerForm;