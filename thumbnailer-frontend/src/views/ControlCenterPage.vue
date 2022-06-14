<template>
  <v-container align="start">
    <h2>All Videos</h2>
    <v-divider></v-divider>
    <v-row v-for="n in 3" :key="n" class="mt-5">
      <v-col v-for="k in 3" :key="k">
        <v-card class="mx-auto" width="370" elevation="2">
          <iframe
            width="370"
            src="http://localhost:9000/video/test.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=pkinwza%2F20220614%2F%2Fs3%2Faws4_request&X-Amz-Date=20220614T174154Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=8c60ffa0a896ee1e930325ada00d3ffa7975dd39cf4f32e0887d3b5f42cc8341"
            allowfullscreen
          >
          </iframe>

          <v-card-title class="py-0"> File name </v-card-title>

          <v-card-actions class="justify-end">
            <CreateJobDialog :button-name="'Create Job'"></CreateJobDialog>
            <ViewJobStatusDialog></ViewJobStatusDialog>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ViewJobStatusDialog from "@/components/ViewJobStatusDialog";
import CreateJobDialog from "@/components/CreateJobDialog";

export default {
  name: "ControlCenterPage",
  components: { ViewJobStatusDialog, CreateJobDialog },
  data() {
    return {
      dialog: false,
    };
  },

  // components: {
  //   HelloWorld,
  // },
};
</script>
