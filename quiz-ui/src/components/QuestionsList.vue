<template>
  <div class="card" style="background-color: #222222; color: white;">
    <div class="card-body">
      <h2 class="card-title text-center">Question List</h2>
      <ul class="list-group list-group-flush">
        <li class="answer-link list-group-item cursor-pointer" v-for="question in questions" :key="question.id">
          {{ question.position }} -
          <router-link :to="'/questions/' + question.id">{{ question.title }}</router-link>
        </li>
      </ul>
      <br>
      <div>
        <router-link to="/questions/create" class="btn btn-outline-success">Create a Question</router-link>
      </div>
    </div>
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


<style scoped>
.answer-link {
  background-color: #373737;
  color: white;
  transition: background-color 0.3s ease;
}

.answer-link:hover {
  background-color: #565656;
}
</style>
