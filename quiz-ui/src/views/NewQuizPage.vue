<template>
  <div>
    <div>
      <h1>Nouveau Quiz</h1>
    </div>

    <div class="d-flex justify-content-center">
      <div class="card"
        style="width: 18rem; height: fit-content; margin-top: 5rem; background-color: #222222; color: white;">
        <div class="card-body" style="align-content: center;">
          <h5 class="card-title">Entrez votre pseudo</h5>
          <p class="card-text">
            <input type="text" class="form-control" placeholder="Pseudo" v-model="username" />
            <br>
            <br>
            <button class="btn btn-primary" style="align-content: center;" @click="launchNewQuiz">Commencer</button>
          </p>
        </div>
      </div>
    </div>
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
      if (!this.username) this.username = "Joueur anonyme";
      console.log("Launch new quiz with", this.username);
      ParticipationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  },
};
</script>

<style></style>
