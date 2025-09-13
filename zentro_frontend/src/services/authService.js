import api from "./api";

export const login = async (email, password) => {
  const formData = new URLSearchParams();
  formData.append("username", email); // OAuth2PasswordRequestForm espera "username"
  formData.append("password", password);

  const res = await api.post("/auth/login", formData, {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });

  if (res.data.access_token) {
    localStorage.setItem("token", res.data.access_token);
  }

  return res.data;
};

export const logout = () => {
  localStorage.removeItem("token");
};

export const register = async (userData) => {
  const res = await api.post("/auth/register", userData);
  return res.data;
};

export const getToken = () => localStorage.getItem("token");
export const isAuthenticated = () => !!getToken();
