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
export default {
  name: "GifFilesPage",
  components: { GifCard },
  data: () => ({
    gifs: [],
  }),
  methods: {
    getObj(i) {
      return {
        id: i,
        name: "Image " + i,
        url: !(i % 4)
          ? "https://ecommerceiq.asia/wp-content/uploads/2020/04/gifs.gif"
          : "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/13532749510923.58b6f17689528.gif",
      };
    },
    initializeRandomList() {
      this.gifs = [...Array(25).keys()].map((i) => this.getObj(i));
      // this.gifs = [obj, obj, obj, obj, obj, obj, obj, obj, obj, obj]
    },
  },
  created() {
    // FIXME: change when connected to MinIO
    this.initializeRandomList();
  },
};
</script>

<style scoped></style>
