// src/pages/RegisterPage.jsx
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createUser } from "../services/userService";

export default function RegisterPage() {
  const navigate = useNavigate();
  const [id, setId] = useState(""); // documento de identidad
  const [documentType, setDocumentType] = useState("CC"); // valor por defecto
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      const data = await createUser({
        id, // documento como ID único
        document_type: documentType,
        first_name: firstName,
        last_name: lastName,
        email,
        password,
      });

      if (data.id) {
        setSuccess("Usuario registrado correctamente. Redirigiendo al login...");
        setTimeout(() => navigate("/login"), 2000);
      } else {
        setError("No se pudo registrar el usuario");
      }
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || "Error al registrar usuario");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 space-y-4 bg-white rounded shadow">
        <h2 className="text-2xl font-bold text-center">Registrar Usuario</h2>
        {error && <p className="text-red-500">{error}</p>}
        {success && <p className="text-green-500">{success}</p>}
        <form onSubmit={handleSubmit} className="space-y-4">

          {/* Tipo de documento */}
          <div>
            <label className="block mb-1 font-medium">Tipo de documento</label>
            <select
              value={documentType}
              onChange={(e) => setDocumentType(e.target.value)}
              className="w-full px-3 py-2 border rounded"
              required
            >
              <option value="CC">Cédula de Ciudadanía</option>
              <option value="TI">Tarjeta de Identidad</option>
              <option value="PASAPORTE">Pasaporte</option>
              <option value="OTRO">Otro</option>
            </select>
          </div>

          {/* Número de documento */}
          <div>
            <label className="block mb-1 font-medium">Número de documento</label>
            <input
              type="text"
              value={id}
              onChange={(e) => setId(e.target.value)}
              className="w-full px-3 py-2 border rounded"
              required
            />
          </div>

          {/* Nombre */}
          <div>
            <label className="block mb-1 font-medium">Nombre</label>
            <input
              type="text"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              className="w-full px-3 py-2 border rounded"
              required
            />
          </div>

          {/* Apellido */}
          <div>
            <label className="block mb-1 font-medium">Apellido</label>
            <input
              type="text"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              className="w-full px-3 py-2 border rounded"
              required
            />
          </div>

          {/* Email */}
          <div>
            <label className="block mb-1 font-medium">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3 py-2 border rounded"
              required
            />
          </div>

          {/* Contraseña */}
          <div>
            <label className="block mb-1 font-medium">Contraseña</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-2 border rounded"
              required
            />
          </div>

          {/* Botón */}
          <button
            type="submit"
            className="w-full px-4 py-2 font-bold text-white bg-blue-500 rounded hover:bg-blue-600"
          >
            Registrarse
          </button>

          <div className="mt-4 text-center">
            <p className="text-sm">
              ¿Ya tienes cuenta?{" "}
              <a
                href="/Login"
                className="text-blue-600 hover:underline font-medium"
              >
                Inicia sesión aquí
              </a>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
}
