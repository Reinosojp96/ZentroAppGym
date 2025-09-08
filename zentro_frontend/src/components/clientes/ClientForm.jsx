// src/components/clientes/ClientForm.jsx
import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../../services/api";

export default function ClientForm() {
  const { id } = useParams();
  const editing = !!id;
  const [form, setForm] = useState({ name: "", email: "", phone: "" });
  const nav = useNavigate();

  useEffect(() => {
    if (!editing) return;
    let mounted = true;
    api.get(`/clients/${id}`)
      .then((res) => mounted && setForm(res.data))
      .catch(() => {})
      .finally(() => (mounted = false));
  }, [editing, id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editing) await api.put(`/clients/${id}`, form);
      else await api.post("/clients", form);
      nav("/clientes");
    } catch (err) {
      console.error(err);
      alert("Error al guardar");
    }
  };

  return (
    <div className="p-6">
      <div className="bg-white p-6 rounded-lg card-shadow">
        <h2 className="text-lg font-semibold mb-4">{editing ? "Editar Cliente" : "Nuevo Cliente"}</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm text-gray-600">Nombre</label>
            <input className="input" value={form.name} onChange={(e) => setForm({...form, name: e.target.value})} />
          </div>
          <div>
            <label className="block text-sm text-gray-600">Email</label>
            <input className="input" value={form.email} onChange={(e) => setForm({...form, email: e.target.value})} />
          </div>
          <div>
            <label className="block text-sm text-gray-600">Teléfono</label>
            <input className="input" value={form.phone} onChange={(e) => setForm({...form, phone: e.target.value})} />
          </div>

          <div className="flex gap-2">
            <button type="submit" className="btn-primary">{editing ? "Guardar" : "Crear"}</button>
            <button type="button" onClick={() => nav(-1)} className="btn-secondary">Cancelar</button>
          </div>
        </form>
      </div>
    </div>
  );
}
