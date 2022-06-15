<template>
  <v-app>
    <v-app-bar app color="#45734e" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          :src="require('./assets/logo.png')"
          transition="scale-transition"
          width="40"
        />

        <h2>Dek Wan Tube (เด็กแว๊นทูป)</h2>

<!--        <v-img-->
<!--          alt="Vuetify Name"-->
<!--          class="shrink mt-1 hidden-sm-and-down"-->
<!--          contain-->
<!--          min-width="100"-->
<!--          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"-->
<!--          width="100"-->
<!--        />-->
      </div>

      <!--      <v-spacer></v-spacer>-->

      <!--      <v-btn-->
      <!--        href="https://github.com/vuetifyjs/vuetify/releases/latest"-->
      <!--        target="_blank"-->
      <!--        text-->
      <!--      >-->
      <!--        <span class="mr-2">Latest Release</span>-->
      <!--        <v-icon>mdi-open-in-new</v-icon>-->
      <!--      </v-btn>-->
    </v-app-bar>
    <v-navigation-drawer color="#E8F5E9" permanent expand-on-hover absolute>
      <v-list-item class="mt-16">
        <v-list-item-content>
          <v-list-item-title class="text-h6 mt-5" style="color: #37474f"
            >Menu</v-list-item-title
          >
          <v-list-item-subtitle> Select any choice </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.link"
        >
          <v-list-item-icon>
            <v-icon color="#546E7A">{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    items: [
      {
        title: "Control Center",
        icon: "mdi-application-cog-outline",
        link: "/",
      },
      { title: "GIF Files", icon: "mdi-image", link: "/gif-files" },
      { title: "Jobs", icon: "mdi-account-hard-hat", link: "/jobs" },
    ],
    right: null,
  }),
};
</script>
