<template>
  <div>
    <v-btn color="#81a36f" text @click="dialog = true">
      Create Job
    </v-btn>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="text-h5"> Create Job </v-card-title>

        <v-divider class="mx-3"></v-divider>

        <v-card-subtitle class="mt-3 pb-0">
          Fill name of output file
        </v-card-subtitle>
        <v-card-text class="mt-0 pt-0">
          <v-form class="mt-0 pt-0" v-model="valid">
            <v-text-field
              v-model="outputName"
              :rules="nameRules"
              label="Output Name"
              required
            >
            </v-text-field>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="#81a36f" text @click="dialog = false"> Cancel </v-btn>

          <v-btn color="#81a36f" :disabled="!valid" text @click="submitJob()"> Submit </v-btn>
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
      valid: false,
      outputName: "",
      nameRules: [
        v => !!v || 'This field is required',
        v => v.toString().endsWith(".gif") || 'The name must end with .gif',
      ],
    };
  },

  methods: {
    async submitJob() {
      let data = {
        input_fle: this.videoName,
        output_file: this.outputName,
      };
      let response = await Vue.axios.post("/api/submit-job", data);
      this.dialog = false;
      console.log(response.data);
    },
  },
};
</script>

<style scoped></style>
