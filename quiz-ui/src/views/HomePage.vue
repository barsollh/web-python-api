<template>
  <div class="container">
    <h1>Home page</h1>
    <router-link to="/start-new-quiz-page" class="btn btn-primary">Démarrer le quiz !</router-link>
    <div class="score-entry" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      <span>{{ scoreEntry.playerName }}</span>
      &nbsp;
      <span>{{ scoreEntry.score }}</span>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores : []
    };
  },
  async created() {
    try {
      const value = await quizApiService.getQuizInfo();
      this.registeredScores = value.data.scores;
    } catch (error) {
      console.log("Une erreur s'est produite lors de la récupération des scores.", error);
    }
    console.log("Composant Home page 'created'");
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