<template>
  <div>
    <h2>Question Admin Display</h2>
    <template v-if="question">
      <p>Title: {{ question.title }}</p>
      <p>Text: {{ question.text }}</p>
      <img :src="question.image" alt="Preview" v-if="question.image" class="max-dimensions"><br>
      <ul>
        <li v-for="answer in question.possibleAnswers" :key="answer.id">
          {{ answer.text }} ({{ answer.isCorrect ? 'Correct' : 'Incorrect' }})
        </li>
      </ul>
      <button @click="editQuestion">Edit</button>
      <button @click="deleteQuestion">Delete</button>
    </template>
    <template v-else>
      <p>Loading question...</p>
    </template>
  </div>
</template>


<script>
import AdministrationStorageService from '../services/AdministrationStorageService';
import QuizApiService from '../services/QuizApiService';

export default {
  data() {
    return {
      question: null,
    };
  },
  mounted() {
    this.loadQuestion();
  },
  methods: {
    loadQuestion() {
      const questionId = this.$route.params.id;
      QuizApiService.getQuestionById(questionId)
        .then((response) => {
          this.question = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    editQuestion() {
      const questionId = this.$route.params.id;
      this.$router.push(`/questions/${questionId}/edit`);
    },
    deleteQuestion() {
      const questionId = this.$route.params.id;
      QuizApiService.deleteQuestionById(questionId,AdministrationStorageService.getToken())
        .then(() => {
          this.$router.go(-1);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.max-dimensions {
  max-width: 100%;
  max-height: 100%;
}
</style>