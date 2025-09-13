// src/pages/ClientesPage.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';

// 1. Importa los componentes de presentación (los "especialistas")
import ClientList from '../components/clientes/ClientList';
import ClientForm from '../components/clientes/ClientForm';

function ClientesPage() {
  // --- ESTADOS ---
  // Estado para la lista de clientes que viene de la API
  const [clientes, setClientes] = useState([]);
  // Estado para controlar la vista actual: 'lista' o 'formulario'
  const [vista, setVista] = useState('lista'); 
  // Estado para manejar el estado de carga de los datos
  const [cargando, setCargando] = useState(true);
  // Estado para almacenar cualquier error de la API
  const [error, setError] = useState(null);

  // --- EFECTO PARA OBTENER DATOS ---
  // Se ejecuta solo una vez cuando el componente se monta
  useEffect(() => {
    fetchClientes();
  }, []);

  // --- FUNCIONES (LÓGICA) ---

  // Función para obtener los clientes del backend
  const fetchClientes = async () => {
    setCargando(true); // Inicia la carga
    try {
      // Reemplaza esta URL con la de tu API real
      const response = await axios.get('http://localhost:3001/api/clientes');
      setClientes(response.data);
      setError(null); // Limpia errores previos
    } catch (err) {
      setError('Error al cargar los clientes. Inténtalo de nuevo más tarde.');
      console.error(err);
    } finally {
      setCargando(false); // Finaliza la carga
    }
  };

  // Función para guardar un nuevo cliente (se la pasaremos al ClientForm)
  const handleSaveClient = async (nuevoCliente) => {
    try {
      // Aquí harías la petición POST para crear el nuevo cliente
      // await axios.post('http://localhost:3001/api/clientes', nuevoCliente);
      console.log('Guardando cliente:', nuevoCliente); // Simulación por ahora

      // Después de guardar, vuelve a la lista y actualiza los datos
      setVista('lista');
      fetchClientes(); // Vuelve a cargar la lista para incluir el nuevo cliente
    } catch (err) {
      setError('No se pudo guardar el cliente.');
      console.error(err);
    }
  };

  // --- RENDERIZADO ---

  // Muestra un mensaje de carga mientras se obtienen los datos
  if (cargando) {
    return <div className="text-center p-10">🔄 Cargando...</div>;
  }

  // Muestra un mensaje de error si la petición a la API falló
  if (error) {
    return <div className="text-center p-10 text-red-600">⚠️ {error}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      {/* El título y el botón cambian según la vista actual */}
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">
          {vista === 'lista' ? 'Lista de Clientes' : 'Agregar Nuevo Cliente'}
        </h1>
        {vista === 'lista' && (
          <button
            onClick={() => setVista('formulario')}
            className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg shadow"
          >
            + Agregar Cliente
          </button>
        )}
      </div>

      {/* Renderizado condicional: muestra la lista o el formulario */}
      {vista === 'lista' ? (
        <ClientList clientes={clientes} />
      ) : (
        <ClientForm
          onSave={handleSaveClient}
          onCancel={() => setVista('lista')}
        />
      )}
    </div>
  );
}

export default ClientesPage;