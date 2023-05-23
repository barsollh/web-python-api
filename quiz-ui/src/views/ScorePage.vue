<template>
  <div class="container">
    <h1>Fin du Quiz !</h1>
    <h3 style="text-align: center;">Votre score : <b>{{ score }} / {{ question_count }}</b></h3>
    <ScoreManager />
  </div>
  <br>
  <div class="d-flex justify-content-center">
    <RouterLink to="/" class="btn btn-primary">Home</RouterLink>
  </div>
</template>

<script>
import ParticipationStorageService from "@/services/ParticipationStorageService";
import ScoreManager from '../components/ScoreManager.vue';
import QuizApiService from "../services/QuizApiService";

export default {
  name: "ScorePage",
  components: {
    ScoreManager
  },
  data() {
    return {
      score: 0,
      question_count: 0,
      questions: []
    };
  },
  mounted() {
    this.loadQuestions();
  },
  methods: {
    loadQuestions() {
      QuizApiService.getQuestions()
        .then((response) => {
          this.questions = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  async created() {
    this.score = await ParticipationStorageService.getParticipationScore();
    const response = await QuizApiService.getQuizInfo();
    this.question_count = response.data.size;
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

.questions .correct-answer.selected {
  background-color: green;
}

.questions .incorrect-answer.selected {
  background-color: red;
}
</style>
