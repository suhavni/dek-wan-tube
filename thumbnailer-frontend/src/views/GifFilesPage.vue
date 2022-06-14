<template>
  <div class="mt-4 mb-4">
    <v-container align="start">
      <div>
        <v-row>
          <h2>All GIFs</h2>
          <v-spacer></v-spacer>
          <v-btn outlined color="#81a36f" class="justify-end" @click.stop="dialog = true">
            Delete All
            <v-icon right dark> mdi-trash-can-outline </v-icon>
          </v-btn>
        </v-row>
      </div>
      <v-divider class="mt-5"></v-divider>
      <v-container class="pa-0 mt-3" v-if="gifs.length !== 0">
        <v-row v-for="i in Math.ceil(gifs.length / 3)" :key="i">
          <v-col v-for="j in 3" :key="j">
            <gif-card
              v-if="(i - 1) * 3 + (j - 1) < gifs.length"
              :gif="gifs[(i - 1) * 3 + (j - 1)]"
            ></gif-card>
          </v-col>
        </v-row>
        <v-dialog
            v-model="dialog"
            max-width="290"
        >
          <v-card>
            <v-card-title>
              Delete All GIFs?
            </v-card-title>

            <v-card-text>
              Are you sure you want to delete all the GIF files?
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                  color="#81a36f"
                  text
                  @click="dialog = false"
              >
                Disagree
              </v-btn>

              <v-btn
                  color="#81a36f"
                  text
                  @click="deleteAllGIFs()"
              >
                Agree
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
      <v-container v-else>
        <v-card color="#00000000" elevation="0">
          <v-card-title class="justify-center">No GIFs Found</v-card-title>
          <v-card-text class="text-center">Why don't you submit a new job?</v-card-text>
          <v-row  no-gutters justify="space-around">
            <v-img
              src="https://www.roots.tech/web/image/13846-cb303eb9/No%20data-cuate.png"
              max-width="370"
            />
          </v-row>
        </v-card>
      </v-container>
    </v-container>
    {{gifs.length}}
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
    dialog: false,
  }),
  methods: {
    async getAllGIFs() {
      const data = { "bucket_name" : "gif" }
      this.gifs = (await Vue.axios.post("/api/gif-list", data)).data.file_names;
    },
    async deleteAllGIFs() {
      const data = {
        "bucket_name": "gif",
      }
      await Vue.axios.post('api/delete-all-gifs', data);
      window.location.reload();
    }
  },
  created() {
    // FIXME: change when connected to MinIO
    this.getAllGIFs();
  }
};
</script>

<style scoped></style>
