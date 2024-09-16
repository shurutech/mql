import React from "react";

type Props = {
    errorMessage: string;
}
const ErrorBox = ({errorMessage}: Props):React.JSX.Element => {
   return (
     <div>
         <div className="w-full mt-4 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <strong className="font-bold">Error! </strong>
            <span className="block sm:inline">{errorMessage}</span>
         </div>
     </div>
   )
}

export default ErrorBox;