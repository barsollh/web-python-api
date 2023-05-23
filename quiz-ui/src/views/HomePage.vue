<template>
  <div>

    <div>
      <h1 class="text-md-start" style="text-align: center;">Bienvenue</h1>
    </div>

    <div class="d-flex flex-row" style="justify-content: space-around;/* background-color: red;*/">

      <div class="container d-flex flex-column" style="align-items: center;">
        <div class="row flex-grow-1" style="">
          <div class="card p-0"
            style="height: fit-content; width: fit-content;; margin-top: 0rem; background-color: #222222; color: white;">
            <img src="../assets/QuizAppBanner4.png" class="card-img-top">
            <div class="card-body">
              <h5 class="card-title">Quiz</h5>
              <p class="card-text">Effectuez le quiz et tentez de remporter la première place du classement !
                <br>
                <br>
                <a style="font-weight: bold; color: #2768BF;">Attention ! </a>
                Vous ne pouvez pas revenir en arrière après avoir sélectionné une réponse.
              </p>
              <div>
                <router-link to="/start-new-quiz-page" class="btn btn-primary mt-4">Démarrer le quiz !</router-link>
              </div>
            </div>
          </div>

        </div>
      </div>

      <div class="container d-flex flex-column" style="align-items: center;">
        <div class="row flex-grow-1" style="">
          <ScoreManager />
        </div>

      </div>


    </div>
  </div>
</template>

<script>
import ScoreManager from '../components/ScoreManager.vue';

export default {
  name: "HomePage",
  components: {
    ScoreManager
  },
  data() {
    return {
    };
  }
};
</script>

<style scoped>
@media (min-width: 1024px) {
  .container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
  }

  .btn-primary {
    margin-top: 20px;
  }

  .border-start {
    border-left: 1px solid var(--bs-gray-200);
  }
}
</style>
