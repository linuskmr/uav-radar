<template>
  <div id="app">
    <Flightmap/>
    <DroneInfo></DroneInfo>
  </div>
</template>

<script>
import Flightmap from './components/Flightmap.vue'
import DroneInfo from "@/components/DroneInfo";

export default {
  name: 'App',
  components: {
    DroneInfo,
    Flightmap
  }
}
</script>

<style>
#app {
  font-family: 'DM Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
}

h1, h2, h3, h4, h5 {
  font-weight: 400;
}

p {
  margin: 10px;
}
</style>
