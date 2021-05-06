<template>
  <aside>
    <h1>Selected</h1>
    <div class="drone-info">
      <div class="drone-label">
        <p><img class="drone-icon" src="../assets/drone-icon.png" alt="Drone"></p>
        <p class="small-text">DHL-ARB1</p>
      </div>
      <div class="drone-data">
        <p>Speed: {{speed}} km/h</p>
        <p>Height: {{height}} m</p>
        <p>Battery: {{battery}} %</p>
        <p>Temperature: {{temperature}} °C</p>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  name: "DroneInfo",
  data() {
    return {
      speed: 18.9,
      height: 110.3,
      battery: 74.2,
      temperature: 22.6,
    }
  }
}
</script>

<style scoped>
aside {
  padding: 0 20px;
  background-color: lightgray;
}

.drone-info {
  display: flex;
}

.drone-info > div {
  padding-right: 10px;
}

.drone-info > div:last-child {
  padding-right: 0;
}

.drone-icon {
  width: 40px;
}

.drone-label {
  text-align: center;
}

.small-text {
  font-size: 9pt;
}

.drone-data {
  white-space: nowrap;
}
</style>