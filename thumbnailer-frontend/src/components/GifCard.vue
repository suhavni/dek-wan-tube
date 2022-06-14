<template>
  <div>
    <v-card max-width="370">
      <v-container @mouseover="onHover = true" @mouseleave="onHover = false" >
        <v-row>
          <v-img :src="gif.url"></v-img>
        </v-row>
        <v-row>
          <v-card-title class="pl-4 pr-4 pt-2 pb-2">
            {{ gif.name }}
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
            <v-card-title class="text-h5">
              Delete GIF?
            </v-card-title>

            <v-card-text>
              Are you sure you want to delete the GIF, {{ gif.name }}?
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
                  @click="dialog = false"
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
export default {
  name: "GifCard",
  props: ["gif"],
  data: () => ({
    onHover: false,
    dialog: false,
  }),
};
</script>

<style scoped></style>
