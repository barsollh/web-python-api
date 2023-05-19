<template>
  <div class="about">
    <h1>Start new quiz</h1>
    <span>
        <p>
          <label>Player Name:</label>
          <input type="text" v-model="username" />
        </p>
        <div>{{ username }}</div>
        <button class="btn btn-primary" @click="launchNewQuiz">Start Quiz</button>
    </span>
  </div>
</template>

<script>
import ParticipationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ""
    };
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      ParticipationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
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
