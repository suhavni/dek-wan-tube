<template>
  <div>
    <v-btn color="#81a36f" text @click="getStatus()"> View Job Status </v-btn>
    <v-dialog v-model="dialog" max-width="800">
      <v-card>
        <v-card-title class="text-h5">
          Job status

          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          class="mx-5"
          :loading="tableLoading"
          loading-text="Loading... Please wait"
          :headers="headers"
          :items="desserts"
          :search="search"
        >
          <template v-slot:item.status="{ item }">
            <v-chip :color="getColor(item.status)" dark>
              {{ item.status }}
            </v-chip>
          </template>
        </v-data-table>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="#81a36f" text @click="dialog = false"> Cancel </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  name: "ViewJobStatusDialog",
  props: ["videoName"],
  data() {
    return {
      dialog: false,
      tableLoading: false,
      search: "",
      headers: [
        {
          text: "Job ID",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "Input Video Name", value: "inputName" },
        { text: "Output Video Name", value: "outputFilename" },
        { text: "Status", value: "status" },
      ],
      desserts: [],
    };
  },
  methods: {
    async getStatus() {
      this.dialog = true;
      this.tableLoading = true;
      let response_ids = await Vue.axios.post("/api/get-job-ids", {
        input_filename: this.videoName,
      });
      let all_ids = response_ids.data.all_jobs;
      this.desserts = [];
      for (let index = 0; index < all_ids.length; index++) {
        let response_status = await Vue.axios.post("/api/get-job-status", {
          job_id: all_ids[index],
        });
        if (response_status.data.id !== undefined) {
          this.desserts.push(response_status.data);
        }
      }
      this.tableLoading = false;
    },
    getColor(status) {
      if (status === "Sent to Extract Worker") return "lime darken-2";
      else if (status === "Downloading video from MinIO")
        return "light-blue darken-1";
      else if (status === "Started extracting frames")
        return "light-blue darken-2";
      else if (status === "Finished extracting frames. Uploading to MinIO.")
        return "light-blue darken-3";
      else if (status === "Uploaded frames to MinIO. Sending to GIF Composer.")
        return "light-blue darken-4";
      else if (status === "Downloading extracted frames from MinIO")
        return "teal darken-1";
      else if (status === "Started composing GIF") return "teal darken-2";
      else if (status === "Finished composing GIF. Uploading to MinIO.")
        return "teal darken-3";
      else if (status === "Uploaded GIF to MinIO.") return "green";
      else return "red";
    },
  },
};
</script>

<style scoped></style>
