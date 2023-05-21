<template>
  <div class="border rounded" style="height: fit-content;">
    <h3 style="width: 600px;">Meilleurs scores :</h3>
    <table class="table" style="color: white;text-align: center;">
      <thead>
        <tr>
          <th scope="col"><b>Name</b></th>
          <th scope="col"><b>Score</b></th>
        </tr>
      </thead>
      <tbody>
        <tr class="score-entry" v-for="(scoreEntry, index) in paginatedScores" :key="index">
          <td>{{ scoreEntry.playerName }}</td>
          <td>{{ scoreEntry.score }}</td>
        </tr>
      </tbody>
    </table>
    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li class="page-item" :class="{ active: page === currentPage }" v-for="page in totalPages" :key="page">
          <a class="page-link" href="#" @click="goToPage(page)">{{ page }}</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

  
<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "ScoreManager",
  data() {
    return {
      registeredScores: [],
      currentPage: 1,
      pageSize: 10,
    };
  },
  computed: {
    paginatedScores() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;

      return this.registeredScores.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.registeredScores.length / this.pageSize);
    },
  },
  async created() {
    try {
      const value = await quizApiService.getQuizInfo();
      this.registeredScores = value.data.scores;
    } catch (error) {
      console.log("Une erreur s'est produite lors de la récupération des scores.", error);
    }
    console.log("Composant Home page 'created'");
  },
  methods: {
    goToPage(page) {
      this.currentPage = page;
    },
  }
};
</script>
