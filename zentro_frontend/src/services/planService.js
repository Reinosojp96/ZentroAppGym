import api from "./api";

export const getPlans = async () => {
  const res = await api.get("/plans/");
  return res.data;
};

export const createPlan = async (planData) => {
  const res = await api.post("/plans/", planData);
  return res.data;
};
