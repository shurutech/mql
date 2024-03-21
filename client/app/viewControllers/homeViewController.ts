import {
    ArrowTrendingUpIcon,
    BoltIcon,
    LightBulbIcon,
    TableCellsIcon,
} from "@heroicons/react/24/outline";

import {
    ChatBubbleOvalLeftEllipsisIcon,
    CircleStackIcon,
    QuestionMarkCircleIcon,
} from "@heroicons/react/24/solid";

import { cookies } from "next/headers";

const useHomeViewController = () => {

    const token = cookies().get("token")?.value

    const features = [
        {
            name: "Insights Empowered",
            description:
                "Discover the power of AI-driven insights, as we revolutionise the way you interact with your data.",
            icon: LightBulbIcon,
        },
        {
            name: "Simplified Queries",
            description:
                "Simplify intricate queries through our user-friendly natural language interface, enabling non-technical users to make informed choices.",
            icon: TableCellsIcon,
        },
        {
            name: "Powerful Decisions",
            description:
                "Unleash the true potential of your business with effortless data-driven decision-making.",
            icon: BoltIcon,
        },
        {
            name: "Data Empowerment",
            description:
                "Unlock the power of AI to harness insights easily, from individual shoppers to global corporations.",
            icon: ArrowTrendingUpIcon,
        },
    ];

    const setupSteps = [
        {
            name: "Set the Stage",
            description: "Begin by Uploading Your Database Schema!",
            icon: CircleStackIcon,
        },
        {
            name: "Ask Away",
            description:
                "Pop Your Questions, something like 'How many bookings done in last week?'",
            icon: QuestionMarkCircleIcon,
        },
        {
            name: "Voila, Query Delivered",
            description: "AI generated working SQL query in your hands!",
            icon: ChatBubbleOvalLeftEllipsisIcon,
        },
    ];

    return {
        features,
        setupSteps,
        token,
    };
}

export default useHomeViewController;