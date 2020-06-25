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
        redirect: "/dlq-messages",
    },
    {
        path: "/dlq-messages",
        component: DefaultLayout,
        meta: {
            title: "Dlq Messages",
            icon: "view_compact",
            group: "dlq-messages",
        },
        children: [{
                path: "/",
                name: "dlq-messages-topics",
                meta: {
                    title: "Dlq Messages Topics",
                },
                component: () => import( /* webpackChunkName: "topics-table" */ "@/topics/Table.vue"),
            },
            {
                path: "/dlq-messages/subscriptions/:topic",
                name: "dlq-messages-subscriptions",
                meta: {
                    title: "Dlq Messages Subscriptions",
                },
                component: () => import( /* webpackChunkName: "subscriptions-table" */ "@/subscriptions/Table.vue"),
                props: true,
            }, {
                path: "/dlq-messages/messages/:topic/:subscription",
                name: "dlq-messages-messages",
                meta: {
                    title: "Dlq Messages",
                },
                component: () => import( /* webpackChunkName: "dlq-messages-table" */ "@/dlq-messages/Table.vue"),
            },
        ],
    },
    {
        path: "/settings",
        component: DefaultLayout,
        meta: {
            title: "Settings",
            icon: "view_compact",
            group: "settings",
        },
        children: [{
            path: "/settings",
            meta: {
                title: "Settings",
            },
            name: "Settings",
            component: () => import( /* webpackChunkName: "settings" */ "@/settings/Form.vue"),
        }, ],
    },
];