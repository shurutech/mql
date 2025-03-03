import { CONNECT_DATABASE, DATABASES, DELETE_DATABASE, LOGIN, QUERIES, QUERY_EXECUTION, UPLOAD_DATABASE, SCHEMA_SYNC } from "@/app/utils/routes";
import axios from "axios";
import Cookies from "js-cookie";
import { toast } from "react-toastify";
import appText from "../assets/strings";

axios.defaults.baseURL = process.env.NEXT_PUBLIC_API_URL;

axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const errCode = error.response?.status;
    if (errCode === 401 && error.response?.data?.detail !== "Incorrect Password") {
      toast.error(appText.toast.errSessionExpired);
      setTimeout(() => {
        Cookies.set("token", "");
        window.location.href = "/login";
      }, 2000);
    }
    return Promise.reject(error);
  }
);

axios.interceptors.request.use((request) => {
  const token = Cookies.get("token");
  if (token) {
    request.headers.Authorization = `Bearer ${token}`;
  }
  return request;
});

const handleRequest = async (method, url, data) => {
  try {
    const res = await axios[method](url, data);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    throw err.message;
  }
};

export const login = (data) => handleRequest('post', LOGIN, data);
export const getAllDatabase = () => handleRequest('get', DATABASES);
export const getDatabase = (id) => handleRequest('get', `${DATABASES}/${id}`);
export const connectDatabase = (data) => handleRequest('post', CONNECT_DATABASE, data);
export const uploadSchema = (formData) => handleRequest('post', UPLOAD_DATABASE, formData);
export const askQuery = (payload) => handleRequest('post', QUERIES, payload);
export const getQueries = (dbId) => handleRequest('get', `${QUERIES}?db_id=${dbId}`);
export const getQuery = ({ id }) => handleRequest('get', `${QUERIES}/${id}`);
export const executeQuery = (payload) => handleRequest('get', `${QUERY_EXECUTION}?db_id=${payload.db_id}&sql_query=${payload.sql_query}`);
export const syncSchema = (payload) => handleRequest('post', SCHEMA_SYNC, payload);
export const deleteDatabase = (id) => handleRequest('delete', `${DELETE_DATABASE}/${id}`);
