<template>
  <div>
    <h2>Question Admin Display</h2>
    <template v-if="question">
      <p>Title: {{ question.title }}</p>
      <p>Text: {{ question.text }}</p>
      <ul>
        <li v-for="answer in question.possibleAnswers" :key="answer.id">
          {{ answer.text }} ({{ answer.correct ? 'Correct' : 'Incorrect' }})
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
      QuizApiService.deleteQuestionById(questionId)
        .then(() => {
          this.$router.push('/questions');
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
