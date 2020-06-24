import {
    DefaultLayout
} from "@/components/layouts";

export const publicRoute = [{
    path: "*",
    // component: () => import( /* webpackChunkName: "incident-table" */ "@/topics/Table.vue"),
}, ];

// NOTE: The order in which routes are added to the list matters when evaluated. For example, /incidents/report will take precendence over /incidents/:name.
export const protectedRoute = [{
        path: "/",
        component: DefaultLayout,
        meta: {
            title: "Topics",
            group: "topics",
            icon: "",
        },
        redirect: "/topics",
    },
    {
        path: "/topics",
        component: DefaultLayout,
        meta: {
            title: "Topics",
            icon: "view_compact",
            group: "topics",
            requiresAuth: true,
        },
        children: [{
                path: "/topics",
                name: "TopicsTable",
                meta: {
                    title: "Topics",
                },
                component: () => import( /* webpackChunkName: "topics-table" */ "@/topics/Table.vue"),
            },
            {
                path: "/topics/:name",
                name: "SubscriptionsTable",
                meta: {
                    title: "Subscriptions",
                },
                component: () => import( /* webpackChunkName: "subscriptions-table" */ "@/subscriptions/Table.vue"),
                props: true,
            },
        ],
    }, {
        path: "/dlq-messages",
        component: DefaultLayout,
        meta: {
            title: "Dlq Messages",
            icon: "view_compact",
            group: "dlq-messages",
            requiresAuth: true,
        },
        children: [{
            path: "/dlq-messages/:topic/:subscription",
            meta: {
                title: "Dlq Messages",
            },
            name: "DlqMessagesTable",
            component: () => import( /* webpackChunkName: "dlq-messages-table" */ "@/dlq-messages/Table.vue"),
        }, ],
    },
];