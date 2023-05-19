<template>
  <div class="score-entry" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    <span>{{ scoreEntry.playerName }}</span>
    &nbsp;
    <span>{{ scoreEntry.score }}</span>
  </div></template>
  
<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "ScoreManager",
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
  },
  methods: {
  }
};
</script>
