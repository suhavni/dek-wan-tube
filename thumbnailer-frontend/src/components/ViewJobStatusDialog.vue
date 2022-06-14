<template>
  <div>
    <v-btn color="#81a36f" text @click="dialog = true"> View Job Status </v-btn>
    <v-dialog v-model="dialog" max-width="700">
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
          :headers="headers"
          :items="desserts"
          :search="search"
        >
          <template v-slot:item.status="{ item }">
            <v-chip :color="getColor(item.calories)" dark>
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
export default {
  name: "ViewJobStatusDialog",
  props: ["videoName"],
  data() {
    return {
      dialog: false,
      search: "",
      headers: [
        {
          text: "Job ID",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "Input Video Name", value: "inputName" },
        { text: "Output Video Name", value: "outputName" },
        { text: "Status", value: "status" },
      ],
      desserts: [
        {
          id: "1",
          inputName: "test.mp4",
          outputName: "out.mp4",
          status: "Sent to Worker",
        },
        {
          id: "2",
          inputName: "test.mp4",
          outputName: "out.mp4",
          status: "Sent to Worker",
        },
      ],
    };
  },
  methods: {
    getColor(status) {
      if (status === "Sent to Extract Worker") return "grey";
      else return "green";
    },
  },
};
</script>

<style scoped></style>
