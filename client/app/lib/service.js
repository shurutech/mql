import { CONNECT_DATABASE, DATABASES, DELETE_DATABASE, LOGIN, QUERIES , QUERY_EXECUTION, UPLOAD_DATABASE, SCHEMA_SYNC } from "@/app/utils/routes";
import axios from "axios";
import Cookies from "js-cookie";
import { toast } from "react-toastify";
import appText from "../assets/strings";

axios.defaults.baseURL = process.env.NEXT_PUBLIC_API_URL;

axios.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const errCode = error.response.status;
    if (
      errCode === 401 &&
      error.response.data.detail !== "Incorrect Password"
    ) {
      toast.error(appText.toast.errSessionExpired);
      setTimeout(() => {
        Cookies.set("token", "");
        window.location.href = "/login";
      }, 2000);
    }
    return Promise.reject(error);
  }
);

axios.interceptors.request.use(async (request) => {
  const token = Cookies.get("token");
  if (token) {
    request.headers.Authorization = `Bearer ${token}`;
  }
  return request;
});

export const login = async (data) => {
  try {
    const res = await axios.post(LOGIN, data);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const getAllDatabase = async () => {
  try {
    const res = await axios.get(DATABASES);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const getDatabase = async (id) => {
  try {
    const res = await axios.get(`${DATABASES}/${id}`);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const connectDatabase = async (data) => {
  try {
    const res = await axios.post(`${CONNECT_DATABASE}`, data);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const uploadSchema = async (formData) => {
  try {
    const res = await axios.post(`${UPLOAD_DATABASE}`, formData);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const askQuery = async (payload) => {
  try {
    const res = await axios.post(`${QUERIES}`, payload);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const getQueries = async (dbId) => {
  try {
    const res = await axios.get(`${QUERIES}?db_id=${dbId}`);
    return res;
  } catch (err) {
        if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const getQuery = async ({ id }) => {
  try {
    const res = await axios.get(`${QUERIES}/${id}`);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
};

export const executeQuery = async (payload) => {
  try {
    const params = new URLSearchParams({
      db_id: payload.db_id,
      sql_query: payload.sql_query
    });

    const res = await axios.get(`${QUERY_EXECUTION}?${params.toString()}`);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
}

export const syncSchema = async (payload) => {
  try {
    const res = await axios.post(`${SCHEMA_SYNC}`, payload);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
}

export const deleteDatabase = async (id) => {
  try {
    const res = await axios.delete(`${DELETE_DATABASE}/${id}`);
    return res;
  } catch (err) {
    if (err.response) throw err.response.data;
    else throw err.message;
  }
}