<template>
  <div>
    <template v-if="!token">
      <div class="login">
        <input type="password" v-model="password" placeholder="Mot de passe">
        <button @click="login">Connexion</button>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </div>
    </template>
    <template v-else>
      <div class="admin">
        <h1>Admin Page</h1>
        <template v-if="adminMode === 'questionsList'">
          <QuestionsList @question-clicked="displayQuestion" @create-clicked="setAdminMode('questionEdition')" />
        </template>
        <template v-else-if="adminMode === 'questionEdition'">
          <QuestionEdition @cancel-edit="setAdminMode('questionsList')" />
        </template>
        <template v-else-if="adminMode === 'questionAdminDisplay'">
          <QuestionAdminDisplay :question="currentQuestion" />
        </template>
        <button @click="logout">Déconnexion</button>
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
          this.errorMessage = 'Mot de passe incorrect';
        }
      } catch (error) {
        this.errorMessage = "Erreur lors de l'authentification";
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
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
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
