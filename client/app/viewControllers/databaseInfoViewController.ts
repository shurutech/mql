import { useState } from "react";

const useDatabaseInfoViewController = () => {
    const [activeIndex, setActiveIndex] = useState<number | null>(null);

    const handleAccordionToggle = (index: number) => {
      setActiveIndex((prevIndex) => (prevIndex === index ? null : index));
    };

    return {
        activeIndex,
        handleAccordionToggle,
    }
}

export default useDatabaseInfoViewController;