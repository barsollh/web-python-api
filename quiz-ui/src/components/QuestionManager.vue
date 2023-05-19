<template>
  <div class="questions-manager">
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
    <button v-if="quizEnded" @click="endQuiz">End Quiz</button>
  </div>
</template>

<script>
import QuestionDisplay from './QuestionDisplay.vue';
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionsManager",
  components: {
    QuestionDisplay
  },
  data() {
    return {
      currentQuestion: {
        title:"",
        text:"",
        image:"",
        possibleAnswers:[]
      },
      currentQuestionPosition: 1,
      totalNumberOfQuestions: 0,
      quizEnded: false,
      answers: []
    };
  },
  async created() {
    const infos = await quizApiService.getQuizInfo();
    console.log("size : " + infos.data.size);
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
      console.log(answerIndex+1);
      this.answers.push(answerIndex+1);
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
        playerName: "test",
        answers: this.answers
      }
      await quizApiService.addParticipation(payload)
    }
  }
};
</script>
