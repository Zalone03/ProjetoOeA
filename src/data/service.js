import { api } from "./api";

export async function getBots() {
  const response = await api.get("/robos");
  return response.data;
}
export async function getStatus() {
  const response = await api.get("/status");
  return response.data;
}

export async function getBot(id) {
  const response = await api.get(`/robos/${id}`);
  return response.data;
}

export async function getExecutions(id) {
  const response = await api.get(`/robos/${id}/execucoes`);
  return response.data;
}

export async function getLogs(id) {
  const response = await api.get(`/execucoes/${id}/logs`);
  return response.data;
}