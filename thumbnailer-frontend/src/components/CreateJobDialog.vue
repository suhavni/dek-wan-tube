<template>
  <div>
    <v-btn color="#81a36f" text @click="dialog = true">
      {{ buttonName }}
    </v-btn>
    <v-dialog v-model="dialog" max-width="350">
      <v-card>
        <v-card-title class="text-h5"> Create Job? </v-card-title>

        <v-divider class="mx-3"></v-divider>

        <v-card-text class="mt-3">
          Are you sure you want to create job for this video?
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="#81a36f" text @click="dialog = false"> Disagree </v-btn>

          <v-btn color="#81a36f" text @click="dialog = false"> Agree </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "CreateJobDialog",
  props: ["buttonName"],
  data() {
    return {
      dialog: false,
    };
  },
};
</script>

<style scoped>

</style>
