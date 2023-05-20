<template>
  <div class="container">
    <h1>Fin du Quiz !</h1>
    <p>Votre score : {{ score }}</p>
    <ScoreManager/>
  </div>
</template>

<script>
import ParticipationStorageService from "@/services/ParticipationStorageService";
import ScoreManager from '../components/ScoreManager.vue';

export default {
  name: "ScorePage",
  components:{
    ScoreManager
  },
  data() {
    return {
      score: 0,
    };
  },
  methods: {
  },
  async created() {
    this.score = await ParticipationStorageService.getParticipationScore();
  }
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
