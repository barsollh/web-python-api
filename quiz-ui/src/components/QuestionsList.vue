<template>
  <div>
    <h2>Question List</h2>
    <router-link to="/questions/create">Create a Question</router-link>
    <ul>
      <li v-for="question in questions" :key="question.id">
        {{ question.position }} - 
        <router-link :to="'/questions/' + question.id">{{ question.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  data() {
    return {
      questions: [],
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
};
</script>
