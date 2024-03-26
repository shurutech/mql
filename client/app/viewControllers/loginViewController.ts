import { toast } from "react-toastify";
import { login } from "@/app/lib/service";
import Cookies from "js-cookie";
import { useRouter } from "next/navigation";
import { useState } from "react";
import appText from "../assets/strings";

const useLoginViewController = () => {
    const { push } = useRouter();
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const handleLogin = async (e: React.ChangeEvent<any>) => {
        e.preventDefault();
        try {
          const formData = new FormData();
          formData.append("email", email);
          formData.append("password", password);
          const res = await login(formData);
          if (res.status === 200) {
            Cookies.set("token", res.headers["x-auth-token"]);
            toast.success(appText.toast.loginSuccess);
            push("/home");
          }
        } catch (error: any) {
          toast.error(error.detail);
        }
      };

    return {
        handleLogin,
        setEmail,
        setPassword,
        email,
        password,
    }
}

export default useLoginViewController;