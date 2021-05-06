<template>
  <div class="map">
    <img src="../assets/map_braunschweig.png" alt="Map">
    <Drone name="DHL-ARB1" lat="50.7" lng="32.4"></Drone>
    <Drone name="DHL-ME45" lat="10.7" lng="22.4"></Drone>
    <Drone name="Amazon-43T" lat="30.7" lng="6.4"></Drone>
  </div>
</template>

<script>
import Drone from "@/components/Drone";

export default {
  name: 'Flightmap',
  components: {Drone}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.map > img {
  width: 100%;
  height: auto;
}
</style>