<template>
  <div>
    <v-container v-if="videos.length !== 0" align="start">
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
      <v-dialog
        v-model="videoLoading"
        hide-overlay
        persistent
        width="300"
      >
        <v-card
          color="primary"
          dark
        >
          <v-card-text>
            Please stand by
            <v-progress-linear
              indeterminate
              color="white"
              class="mb-0"
            ></v-progress-linear>
          </v-card-text>
        </v-card>
      </v-dialog>
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
            <v-img
              class="white--text align-end"
              height="200px"
              src="https://i.ytimg.com/vi/40IC2n5FBag/maxresdefault.jpg"
            >
              <v-card-title>{{ video }}</v-card-title>
            </v-img>

            <v-card-actions class="justify-end">
              <CreateJobDialog
                :video-name="video.name"
                :error.sync="error"
                :success.sync="success"
              ></CreateJobDialog>
              <ViewJobStatusDialog
                :video-name="video"
              ></ViewJobStatusDialog>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-container v-else>
      <h2>All Videos</h2>
      <v-divider class="mt-5"></v-divider>
      <v-card color="#00000000" elevation="0">
        <v-card-title class="justify-center">No Videos Found</v-card-title>
        <v-card-text class="text-center"
          >Please upload at Minio Storage</v-card-text
        >
        <v-row no-gutters justify="space-around">
          <v-img
            src="https://www.roots.tech/web/image/13846-cb303eb9/No%20data-cuate.png"
            max-width="370"
          />
        </v-row>
      </v-card>
    </v-container>
  </div>
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
      videoLoading: true,
    };
  },

  async beforeCreate() {
    let response = await Vue.axios.post("/api/video-list", {
      bucket_name: "video",
    });
    if (response.data.bucket_name === undefined) {
      this.videos = response.data.videos;
    }
    this.videoLoading = false;
    console.log(response.data);
  },
};
</script>
