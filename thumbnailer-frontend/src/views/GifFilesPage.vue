<template>
  <div class="mt-4 mb-4">
    <v-container align="start">
      <div>
        <v-row>
          <h2>All GIFs</h2>
          <v-spacer></v-spacer>
          <v-btn outlined color="#81a36f" class="justify-end">
            Delete All
            <v-icon right dark> mdi-trash-can-outline </v-icon>
          </v-btn>
        </v-row>
      </div>
      <v-divider class="mt-5"></v-divider>
      <v-container class="pa-0 mt-3">
        <v-row v-for="i in Math.ceil(gifs.length / 3)" :key="i">
          <v-col v-for="j in 3" :key="j">
            <gif-card
              v-if="(i - 1) * 3 + (j - 1) < gifs.length"
              :gif="gifs[(i - 1) * 3 + (j - 1)]"
            ></gif-card>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </div>
</template>

<script>
import GifCard from "../components/GifCard";
import Vue from "vue";
export default {
  name: "GifFilesPage",
  components: { GifCard },
  data: () => ({
    gifs: [],
  }),
  methods: {
    async getAllGIFs() {
      const data = { "bucket_name" : "video" }
      this.gifs = await Vue.axios.get("/api/gif-list", data)
    }
  },
  created() {
    // FIXME: change when connected to MinIO
    this.getAllGIFs();
  }
};
</script>

<style scoped></style>
