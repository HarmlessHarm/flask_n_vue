<template>
  <div class="home">
    <Map id="map" />
    <div id="side"></div>
    <div id="control"></div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue';
import Map from '@/components/Map.vue';

export default {
  name: 'home',
  components: {
    Map,
  },
};
</script>

<style lang="scss" scoped>
.home {
  height: calc(100vh - 50px);
  display: grid;
  grid-template:
    "map     side" auto
    "control side" 100px / auto 200px;


  #map {
    background: yellow;
    grid-area: map;
  }
  #side {
    background: red;
    grid-area: side;
  }
  #control {
    background: green;
    grid-area: control;
  }
}
</style>
