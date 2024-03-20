import Cookies from "js-cookie";
import { usePathname } from "next/navigation";
import { useState } from "react";


const useGenericViewController = () => {
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
    const pathname = usePathname();

    const headerNavigation = [
        { name: "Features", href: "#features" },
        { name: "Steps", href: "#steps" },
    ];

    const logout = () => {
        Cookies.set("token", "");
        window.location.href = "/";
    };

    return {
        logout,
        headerNavigation,
        setMobileMenuOpen,
        mobileMenuOpen,
        pathname
    };
}

export default useGenericViewController;