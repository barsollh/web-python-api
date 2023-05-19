<template>
  <div class="container">
    <h1>Home page</h1>
    <router-link to="/start-new-quiz-page" class="btn btn-primary">Démarrer le quiz !</router-link>
    <ScoreManager/>
  </div>
</template>

<script>
import ScoreManager from '../components/ScoreManager.vue';

export default {
  name: "HomePage",
  components:{
    ScoreManager
  },
  data() {
    return {
    };
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

  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .btn-primary {
    margin-top: 20px;
  }

  .score-entry {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
  }
}
</style>
<style>

</style>