import Cookies from "js-cookie";
import { usePathname } from "next/navigation";
import { useState } from "react";
import appText from "../assets/strings";

type NavigationItem = {
    name: string;
    href: string;
  };

const useGenericViewController = () => {
    const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false);
    const pathname = usePathname();
    const text = appText.header;

    const headerNavigation:NavigationItem[] = [
        { name: text.features, href: "/#features" },
        { name: text.steps, href: "/#steps" },
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