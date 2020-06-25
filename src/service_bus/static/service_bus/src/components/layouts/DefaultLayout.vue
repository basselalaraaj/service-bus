<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item :to="{ path: '/dlq-messages' }" link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>DLQ Messages</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item :to="{ path: '/settings' }" link>
          <v-list-item-action>
            <v-icon>mdi-cog</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ title }}</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>

    <v-footer app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  props: {
    source: String
  },
  data: () => {
    return {
      drawer: null,
      title: null
    }
  },
  created() {
    this.$vuetify.theme.dark = false
  },
  watch: {
    $route: {
      handler() {
        this.title = this.$router.currentRoute.meta.title
      },
      immediate: true
    }
  }
}
</script>
