<template>
  <div>
    <h2>Question Admin Display</h2>
    <template v-if="question">
      <p>Position : {{ question.position }} - Title : {{ question.title }}</p>
      <p>Text: {{ question.text }}</p>
      <img :src="question.image" alt="Preview" v-if="question.image" class="img-fluid"><br>
      <ul>
        <li v-for="answer in question.possibleAnswers" :key="answer.id">
          {{ answer.text }} ({{ answer.isCorrect ? 'Correct' : 'Incorrect' }})
        </li>
      </ul>
      <br>
      <div class="d-grid gap-3  d-md-block">
        <button @click="editQuestion" class="btn btn-primary">Edit</button> &nbsp;
        <button @click="deleteQuestion" class="btn btn-danger">Delete</button> &nbsp;
        <button @click="back" class="btn btn-warning">Back</button>
      </div>
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
    back() {
      this.$router.go(-1);
    },
  },
};
</script>