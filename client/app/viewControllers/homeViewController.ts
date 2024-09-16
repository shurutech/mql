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
import appText from "../assets/strings";



const useHomeViewController = () => {

    const token = cookies().get("token")?.value
    const text = appText.home;

    const features = [
        {
            name: text.insightsEmpowered,
            description: text.insightsEmpoweredDescription,
            icon: LightBulbIcon,
        },
        {
            name: text.simplifiedQueries,
            description:
                text.simplifiedQueriesDescription,
            icon: TableCellsIcon,
        },
        {
            name: text.powerfulDecisions,
            description:
                text.powerfulDecisionsDescription,
            icon: BoltIcon,
        },
        {
            name: text.dataEmpowerment,
            description:
                text.dataEmpowermentDescription,
            icon: ArrowTrendingUpIcon,
        },
    ];

    const setupSteps = [
        {
            name: text.setTheStage,
            description: text.setTheStageDescription,
            icon: CircleStackIcon,
        },
        {
            name: text.askAway,
            description: text.askAwayDescription,
            icon: QuestionMarkCircleIcon,
        },
        {
            name: text.queryDelivered,
            description: text.queryDeliveredDescription,
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