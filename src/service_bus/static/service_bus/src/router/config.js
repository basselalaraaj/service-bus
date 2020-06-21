import {
    DefaultLayout
} from "@/components/layouts";

export const publicRoute = [{
    path: "*",
    component: () => import( /* webpackChunkName: "incident-table" */ "@/topics/Table.vue"),
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
                component: () => import( /* webpackChunkName: "incident-table" */ "@/topics/Table.vue"),
            },
            {
                path: "/topics/:name",
                name: "TopicsTable",
                component: () => import( /* webpackChunkName: "incident-table" */ "@/topics/Table.vue"),
                props: true,
            },
        ],
    },
];