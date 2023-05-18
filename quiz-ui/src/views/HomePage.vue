<template>
  <h1>Home page</h1>
    <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
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
}
</style>