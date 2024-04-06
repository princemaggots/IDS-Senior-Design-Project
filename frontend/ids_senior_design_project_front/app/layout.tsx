import type { Metadata } from "next";
import Navbar from "./components/navbar";
import "./styles/globals.css";


export const metadata: Metadata = {
  title: "IDS",
  description: "A system to assist researchers in developing machine learning based algorithms for Intrusion Detection Systems (IDSs) that can detect and identify malicious cyber-attacks. The system allows the users to easily and effectively run and compare algorithms by providing a GUI (Graphic User Interface) based Web application and database functionality. Additionally, the system provides functionality to present detection results that are easy to understand by the user",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main className="mx-20 my-10 ">
          {children}
        </main>
      </body>
    </html>
  );
}
