import Vue from "vue"
import Router from "vue-router"
import {
  publicRoute,
  protectedRoute
} from "./config"

const routes = publicRoute.concat(protectedRoute)

Vue.use(Router)

const router = new Router({
  mode: "history",
  linkActiveClass: "active",
  routes: routes
})

export default router