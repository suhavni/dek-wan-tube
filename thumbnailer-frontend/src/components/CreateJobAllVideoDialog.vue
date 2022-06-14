<template>
  <div>
    <v-btn text color="#81a36f" class="justify-end" @click="dialog = true">
      <v-icon right dark class="mr-2"> mdi-pencil-outline </v-icon>
      Create Job for All Video
    </v-btn>
    <v-dialog v-model="dialog" max-width="350">
      <v-card>
        <v-card-title class="text-h5">
          Create Job for All Videos?
        </v-card-title>

        <v-divider class="mx-3"></v-divider>

        <v-card-text class="mt-3">
          Are you sure you want to create job for all videos?
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="#81a36f" text @click="dialog = false"> Disagree </v-btn>

          <v-btn color="#81a36f" text @click="createJob()"> Agree </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  name: "CreateJobAllVideoDialog",
  data() {
    return {
      dialog: false,
    };
  },

  methods: {
    async createJob() {
      let data = {
        bucket_name: "gif",
      };
      let response = await Vue.axios.post("/api/submit-all-videos", data);
      if (response.data.title !== undefined) {
        this.$emit("update:error", response.data.title);
        this.error = response.data.title;
      } else {
        this.$emit("update:submitted", true);
      }
      this.dialog = false;
    },
  },
};
</script>

<style scoped></style>
