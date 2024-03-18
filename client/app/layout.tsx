import { ToastContainer } from "./components/toast";
import type { Metadata } from "next";
import "react-loading-skeleton/dist/skeleton.css";
import "react-toastify/dist/ReactToastify.css";
import "./styles/globals.css";

export const metadata: Metadata = {
  title: "Analyitcs",
  description: "Tool to convert your natural language queries to SQL queries",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        {children}
        <ToastContainer />
      </body>
    </html>
  );
}
