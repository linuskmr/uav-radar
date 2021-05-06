<template>
  <div class="drone" :style="position">
      <img class="drone-icon" @click="change_selected" src="../assets/drone-icon.png" alt="Drone">
      <p class="drone-name">{{name}}</p>
  </div>
</template>

<script>
export default {
  name: 'Drone',
  props: {
    lat: Number,
    lng: Number,
    name: String,
  },
  methods: {
    change_selected() {
      alert('Not implemented yet.\n\nThe right sidebar should now show with the data of this drone...')
    }
  },
  computed: {
    position() {
      return `position: absolute;
        left: ${this.lat}%;
        top: ${this.lng}%;`
    }
  }
}
</script>

<style scoped>
.drone {
  text-align: center;
}

.drone-name {
  margin: 0;
  font-size: 9pt;
  background-color: rgba(255, 255, 255, 0.5);
  padding: 2px;
  border-radius: 2px;
}

.drone-icon {
  width: 40px;
  cursor: pointer;
}
</style>