<template>
  <div>
    <h2>Administration</h2>
    <template v-if="question">
      <h4>{{ question.position }} - {{ question.title }}</h4>
      <div class="justify-content-center">
        <div class="row">
          <div class="col-lg-12 d-flex align-items-center justify-content-center">
            <div class="card" id="card1">
              <img v-if="question.image" :src="question.image" class="card-img-top">
              <div class="card-body">
                <h2 class="card-title text-center">{{ question.text }}</h2>
                <h3 class="card-text text-start"></h3>
                <ul>
                  <li v-for="answer in question.possibleAnswers" :key="answer.id">
                    {{ answer.text }} ({{ answer.isCorrect ? 'Vrai' : 'Faux' }})
                  </li>
                </ul>
                <div class="d-grid gap-3  d-md-block text-center">
                  <button @click="editQuestion" class="btn btn-outline-success">Éditer</button> &nbsp;
                  <button @click="deleteQuestion" class="btn btn-outline-danger">Supprimer</button> &nbsp;
                </div>
                <div class="text-end">
                  <button @click="back" class="btn btn-warning">Retour</button>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
      <br>

    </template>
    <template v-else>
      <p>Chargement de la question...</p>
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
      QuizApiService.deleteQuestionById(questionId, AdministrationStorageService.getToken())
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

<style scoped>
#card1 {
  max-width: 40rem;
  background-color: #222222;
  color: white;
}
</style>