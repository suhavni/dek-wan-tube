import Vue from "vue";
import VueRouter from "vue-router";
import ControlCenterPage from "@/views/ControlCenterPage";
import GifFilesPage from "@/views/GifFilesPage";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Control Center",
    component: ControlCenterPage,
  },
  {
    path: "/gif-files",
    name: "GIF Files",
    component: GifFilesPage,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
