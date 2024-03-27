import { ToastContainer } from "../components/toast";
import type { Metadata } from "next";
import "react-loading-skeleton/dist/skeleton.css";
import "react-toastify/dist/ReactToastify.css";
import "../styles/globals.css";
import appText from "../assets/strings";

export const metadata: Metadata = {
  title: appText.metadata.title,
  description: appText.metadata.description,
}

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
