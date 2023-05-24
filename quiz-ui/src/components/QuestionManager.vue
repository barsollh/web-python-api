<template>
  <div class="question-marge">
    <div class="questions-manager">
      <h1 v-if="!quizEnded">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }} - {{
        currentQuestion.title }}</h1>
      <br>
      <br>
      <QuestionDisplay v-if="!quizEnded" :question="currentQuestion" @answer-selected="answerClickedHandler" />
      <br>
      <div class="text-center" style="margin-bottom: 30px;">
        <button class="btn btn-danger" v-if="quizEnded" @click="endQuiz">Terminer le Quiz</button>
      </div>
    </div>
  </div>
</template>

<script>
import QuestionDisplay from './QuestionDisplay.vue';
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsManager",
  components: {
    QuestionDisplay
  },
  data() {
    return {
      currentQuestion: {
        title: "",
        text: "",
        image: "",
        possibleAnswers: []
      },
      currentQuestionPosition: 1,
      totalNumberOfQuestions: 0,
      quizEnded: false,
      answers: []
    };
  },
  async created() {
    const infos = await quizApiService.getQuizInfo();
    // console.log("size : " + infos.data.size);
    this.totalNumberOfQuestions = infos.data.size;
    this.loadQuestionByPosition();
  },
  methods: {
    async loadQuestionByPosition() {
      try {
        const response = await quizApiService.getQuestionByPosition(this.currentQuestionPosition);
        this.currentQuestion.title = response.data.title;
        this.currentQuestion.text = response.data.text;
        this.currentQuestion.image = response.data.image;
        this.currentQuestion.possibleAnswers = response.data.possibleAnswers;
      } catch (error) {
        console.error('Erreur lors de la récupération de la question', error);
      }
    },
    async answerClickedHandler(answerIndex) {
      console.log(answerIndex + 1);
      this.answers.push(answerIndex + 1);
      if (this.currentQuestionPosition < this.totalNumberOfQuestions) {
        this.currentQuestionPosition++;
        this.loadQuestionByPosition();
      } else {
        this.quizEnded = true;
      }
    },
    async endQuiz() {
      console.log(`Quiz ended, answers :${this.answers}`);
      const payload = {
        playerName: await participationStorageService.getPlayerName(),
        answers: this.answers
      };
      try {
        const response = await quizApiService.addParticipation(payload);
        const score = response.data.score;
        await participationStorageService.saveParticipationScore(score);
        console.log(`Score: ${score}`);
      } catch (error) {
        console.error('Error while adding participation:', error);
      }
      this.$router.push('/score');
    }
  }
};
</script>
