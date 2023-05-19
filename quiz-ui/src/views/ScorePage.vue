<template>
  <div class="about">
    <h1>Score page</h1>
    <ScoreManager/>
  </div>
</template>

<script>
//import ParticipationStorageService from "@/services/ParticipationStorageService";
import ScoreManager from '../components/ScoreManager.vue';

export default {
  name: "ScorePage",
  components:{
    ScoreManager
  },
  data() {
    return {
    };
  },
  methods: {
  },
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
