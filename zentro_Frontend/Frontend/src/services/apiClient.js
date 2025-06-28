
import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
});

const token = localStorage.getItem('token');
if (token) {
  apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export default apiClient;
