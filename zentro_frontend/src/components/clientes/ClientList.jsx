// src/components/clientes/ClientList.jsx
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../services/api";

export default function ClientList() {
  const [clients, setClients] = useState([]);
  const [loading, setLoading] = useState(true);
  const nav = useNavigate();

  useEffect(() => {
    let mounted = true;
    api.get("/clients")
      .then((res) => mounted && setClients(res.data || []))
      .catch(() => mounted && setClients([]))
      .finally(() => mounted && setLoading(false));
    return () => (mounted = false);
  }, []);

  return (
    <div className="p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-semibold">Clientes</h2>
        <button onClick={() => nav("/clientes/nuevo")} className="btn-primary">Nuevo Cliente</button>
      </div>

      <div className="bg-white p-4 rounded-lg card-shadow">
        {loading ? (
          <p>Cargando...</p>
        ) : (
          <table className="w-full text-left">
            <thead className="text-sm text-gray-500">
              <tr>
                <th>Nombre</th>
                <th>Email</th>
                <th>Membresía</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {clients.map((c) => (
                <tr key={c.id} className="border-t">
                  <td className="py-3">{c.name}</td>
                  <td>{c.email}</td>
                  <td>{c.membership || "—"}</td>
                  <td>
                    <button onClick={() => nav(`/clientes/${c.id}`)} className="text-indigo-600">Editar</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
