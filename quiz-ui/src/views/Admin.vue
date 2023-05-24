<template>
  <div>
    <template v-if="!token">
      <h2 style="text-align: center;">Bienvenue sur la page Administration</h2>
      <div class="container">
        <div class="login">
          <p style="text-align: center;width: 40%;">Veuillez saisir le mot de passe administrateur afin d'accéder à la
            consultation
            et à
            la gestion des questions du
            Quiz.</p>
          <input type="password" class="form-control" v-model="password" placeholder="Mot de passe" style="width: 20%;">
          <p v-if="errorMessage" class="error mt-3">{{ errorMessage }}</p>
          <button @click="login" class="btn btn-primary mt-3">Connexion</button>
        </div>
      </div>
    </template>
    <template v-else>
      <div class="d-flex flex-column align-items-center">
        <h1 class="text-center">Page d'administration</h1>
        <template v-if="adminMode === 'questionsList'">
          <QuestionsList @question-clicked="displayQuestion" @create-clicked="setAdminMode('questionEdition')" />
        </template>
        <template v-else-if="adminMode === 'questionEdition'">
          <QuestionEdition @cancel-edit="setAdminMode('questionsList')" />
        </template>
        <template v-else-if="adminMode === 'questionAdminDisplay'">
          <QuestionAdminDisplay :question="currentQuestion" />
        </template>
        <div class="d-flex justify-content-center mt-3">
          <button @click="logout" class="btn btn-warning">Déconnexion</button>
        </div>
      </div>
    </template>

  </div>
</template>

<script>
import QuestionsList from '../components/QuestionsList.vue';
import QuestionEdition from '../components/QuestionEdition.vue';
import QuestionAdminDisplay from '../components/QuestionAdminDisplay.vue';
import QuizApiService from '../services/QuizApiService';
import AdministrationStorageService from '../services/AdministrationStorageService';

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Admin',
  components: {
    QuestionsList,
    QuestionEdition,
    QuestionAdminDisplay,
  },
  data() {
    return {
      password: '',
      token: null,
      adminMode: 'questionsList',
      errorMessage: '',
      currentQuestion: null,
    };
  },
  methods: {
    async login() {
      try {
        const token = await QuizApiService.login(this.password);
        if (token) {
          this.token = token;
          AdministrationStorageService.setToken(this.token);
        } else {
          this.errorMessage = 'Erreur lors de l\'authentification';
        }
      } catch (error) {
        this.errorMessage = "Mauvais mot de passe";
        console.error(error);
      }
    },
    logout() {
      this.token = null;
      AdministrationStorageService.clear();
    },
    displayQuestion(question) {
      this.currentQuestion = question;
      this.setAdminMode('questionAdminDisplay');
    },
    setAdminMode(mode) {
      this.adminMode = mode;
    },
  },
  created() {
    const storedToken = AdministrationStorageService.getToken();
    if (storedToken) {
      this.token = storedToken;
    }
  },
};
</script>

<style scoped>
@media (min-width: 1024px) {
  .admin {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

.about {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-wrapper {
  background-color: inherit;
  padding: 20px;
}

.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
}

.login input {
  margin-bottom: 10px;
}

.admin {
  margin-top: 100px;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>
