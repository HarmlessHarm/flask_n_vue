<template>
  <div>
    <div id="map_grid">
      <template v-for="(row, i) in map">
        <template v-for="(c, j) in row">
          <span class="grid_cell" :key="(i+j)"
                :style="get_colour(c)">
          </span>
        </template>
      </template>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Map',
  data() {
    return {
      map: [],
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/map';
      axios.get(path)
        .then((res) => {
          // eslint-disable-next-line
          console.log(res);
          this.map = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    get_colour(val) {
      const num = (val + 1) / 2 * 255;
      return `background-color: rgb(${num},${num},${num});`;
    },
  },
  created() {
    this.getMessage();
  },
};

</script>

<style lang="scss">
#map_grid {
  height: 100%;
  display: grid;
  grid-template-columns: repeat(20, auto);
  grid-template-rows: repeat(20, auto);

  // .grid_cell {
  //   line-height: 1px;
  // }
}
</style>
