<template>
  <div>
    <v-card max-width="370">
      <v-container @mouseover="onHover = true" @mouseleave="onHover = false" >
        <v-row>
          <v-img :src="url"></v-img>
        </v-row>
        <v-row>
          <v-card-title class="pl-4 pr-4 pt-2 pb-2">
            {{ gif }}
          </v-card-title>
        </v-row>
        <v-fade-transition>
          <v-overlay
              :value="onHover"
              color="#627362"
              absolute
          >
            <v-btn dark @click.stop="dialog = true">
              Delete
              <v-icon
                  right
                  dark
              >
                mdi-trash-can-outline
              </v-icon>
            </v-btn>
          </v-overlay>
        </v-fade-transition>

        <v-dialog
            v-model="dialog"
            max-width="290"
        >
          <v-card>
            <v-card-title>
              Delete GIF?
            </v-card-title>

            <v-card-text>
              Are you sure you want to delete the GIF, {{ gif }}?
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
                  @click="deleteGIF()"
              >
                Agree
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  name: "GifCard",
  props: ["gif"],
  data: () => ({
    onHover: false,
    dialog: false,
    url: 'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/13532749510923.58b6f17689528.gif',
  }),
  methods: {
    async getPresignedURL() {
      const data = {
        "bucket_name": "gif",
        "file_name": this.gif,
      }
      this.url = (await Vue.axios.post("/api/get-binary-data", data)).data;
      console.log("BINARY DATA", this.url);
      this.url = this.url.binary_data;
    },
    async deleteGIF() {
      const data = {
        "bucket_name": "gif",
        "file_name": this.gif,
      }
      await Vue.axios.post('api/delete-gif', data);
      window.location.reload();
    }
  },
  created() {
    this.getPresignedURL();
  }
};
</script>

<style scoped></style>
