// src/services/userService.js
import api from "./api.js";

/**
 * Devuelve response.data o el response si no tiene data.
 * @param {object} res Axios response
 */
const unwrap = (res) => (res && res.data !== undefined ? res.data : res);

/**
 * Normaliza y relanza errores (especialmente de axios)
 * @param {any} err
 */
function handleError(err) {
  if (err?.response) {
    const message =
      err.response.data?.detail ||
      err.response.data?.message ||
      err.response.statusText ||
      "Error en el servidor";
    const e = new Error(message);
    e.response = err.response;
    throw e;
  }
  throw err;
}

// Obtener todos los usuarios
export const getUsers = async () => {
  try {
    const res = await api.get("/users/");
    return unwrap(res);
  } catch (err) {
    handleError(err);
  }
};

// Crear un nuevo usuario
export const createUser = async (userData) => {
  try {
    const res = await api.post("/users/", userData);
    return unwrap(res);
  } catch (err) {
    handleError(err);
  }
};

// ✨ Login
export const login = async (email, password) => {
  try {
    const res = await api.post("/auth/login", { email, password });
    const data = unwrap(res);
    if (data?.access_token) {
      localStorage.setItem("token", data.access_token);
      // Si `api` es una instancia de axios, setear el header por defecto
      if (api?.defaults) {
        api.defaults.headers.common.Authorization = `Bearer ${data.access_token}`;
      }
    }
    return data;
  } catch (err) {
    handleError(err);
  }
};

// Logout
export const logout = () => {
  localStorage.removeItem("token");
  if (api?.defaults && api.defaults.headers?.common) {
    delete api.defaults.headers.common.Authorization;
  }
};

// Obtener token actual
export const getToken = () => localStorage.getItem("token");

// Verificar si usuario está logueado
export const isLoggedIn = () => !!getToken();
