export const handleDate = (date) => {
  const d = new Date(date);
  const month = d.toLocaleString("default", { month: "short" });
  const day = d.getDate();
  const year = d.getFullYear();
  return `${day} ${month} ${year}`;
};
