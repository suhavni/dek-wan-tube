<template>
  <v-container align="start">
    <div class="justify-center">
      <v-alert
        class="mb-8 mt-2"
        :value="error !== '' || success !== ''"
        :type="success !== '' ? 'success' : 'error'"
        shaped
        dense
        transition="scale-transition"
        dismissible
      >
        <div v-if="success !== ''">{{ success }}</div>
        <div v-else>{{ error }}</div>
      </v-alert>
    </div>
    <div class="mt-4">
      <v-row>
        <h2>All Videos</h2>
        <v-spacer></v-spacer>
        <CreateJobAllVideoDialog
          :error.sync="error"
          :success.sync="success"
        ></CreateJobAllVideoDialog>
      </v-row>
    </div>
    <v-divider class="mt-5"></v-divider>
    <v-row class="mt-5">
      <v-col v-for="video in videos" :key="video.name">
        <v-card class="mx-auto" width="370" elevation="2">
          <iframe
            width="370"
            :src="video.url"
            allowfullscreen
          >
          </iframe>

          <v-card-title class="py-0"> {{ video.name }} </v-card-title>

          <v-card-actions class="justify-end">
            <CreateJobDialog
              :video-name="video.name"
              :error.sync="error"
              :success.sync="success"
            ></CreateJobDialog>
            <ViewJobStatusDialog :video-name="video.name"></ViewJobStatusDialog>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ViewJobStatusDialog from "@/components/ViewJobStatusDialog";
import CreateJobDialog from "@/components/CreateJobDialog";
import CreateJobAllVideoDialog from "@/components/CreateJobAllVideoDialog";
import Vue from "vue";

export default {
  name: "ControlCenterPage",
  components: { CreateJobAllVideoDialog, ViewJobStatusDialog, CreateJobDialog },
  data() {
    return {
      dialog: false,
      error: "",
      success: "",
      videos: [],
    };
  },

  async beforeCreate() {
    let response = await Vue.axios.post("/api/video-list", {
      bucket_name: "video",
    });
    if (response.data.bucket_name === undefined) {
      this.videos = response.data.videos;
    }
    console.log(response.data);
  },
};
</script>
