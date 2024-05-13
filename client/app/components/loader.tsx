const Loader = () => {
  return (
    <div
      className="mx-auto h-6 w-6 animate-spin rounded-full border-4 border-solid border-current border-e-transparent text-surface motion-reduce:animate-[spin_1.5s_linear_infinite] text-blue-500"
      role="status"
    >
      <span className="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">
        Loading...
      </span>
    </div>
  );
};

export default Loader;
