<template>
  <div>
    <v-btn color="#81a36f" text @click="dialog = true"> Create Job </v-btn>
    <v-dialog v-model="dialog" max-width="350">
      <v-card>
        <v-card-title class="text-h5"> Create Job? </v-card-title>

        <v-divider class="mx-3"></v-divider>

        <v-card-subtitle class="mt-3 pb-0">
          Are you sure you want to create job for this video
        </v-card-subtitle>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="#81a36f" text @click="dialog = false"> Cancel </v-btn>

          <v-btn color="#81a36f" text @click="submitJob()"> Submit </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Vue from "vue";
export default {
  name: "CreateJobDialog",
  props: ["videoName"],
  data() {
    return {
      dialog: false,
    };
  },

  methods: {
    async submitJob() {
      let outputFileName = this.videoName.replace(/\.[^/.]+$/, ".gif");
      let data = {
        input_file: this.videoName,
        output_file: outputFileName,
      };
      let response = await Vue.axios.post("/api/submit-job", data);
      this.dialog = false;
      if (response.data.error !== undefined) {
        this.$emit(
          "update:error",
          "Backend is currently down or input is wrong "
        );
      } else {
        this.$emit(
          "update:success",
          "[" +
            this.videoName +
            "]: " +
            "Job " +
            response.data.job_id +
            " created"
        );
      }
      console.log(response.data);
    },
  },
};
</script>

<style scoped></style>
