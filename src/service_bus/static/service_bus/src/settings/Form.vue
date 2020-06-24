<template>
  <v-container fluid>
    <v-switch
      v-model="darkMode"
      inset
      :label="`Darkmode ${darkMode == true ? 'On' : 'Off'}`"
    ></v-switch>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      darkMode: this.$vuetify.theme.dark
    }
  },
  watch: {
    darkMode(newValue) {
      this.$vuetify.theme.dark = newValue
    }
  }
}
</script>
