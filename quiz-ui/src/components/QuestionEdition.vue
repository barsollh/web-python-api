<template>
  <div>
    <h2>Question Edition</h2>
    <form @submit.prevent="saveQuestion">
      <label for="position">Position:</label>
      <input type="number" id="position" v-model="question.position" required><br>
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="question.title" required><br>
      <label for="text">Text:</label>
      <textarea id="text" v-model="question.text" required></textarea><br>
      <label for="image">Image:</label>
      <image-upload @file-change="handleImageChange"></image-upload><br>
      <img :src="imageUrl" alt="Preview" v-if="imageUrl" class="max-dimensions"><br>
      <h3>Possible Answers:</h3>
      <div v-for="(answer, index) in question.possibleAnswers" :key="answer.id">
        <label>
          <input type="text" v-model="answer.text" required>
          <input type="checkbox" v-model="answer.correct">
          Correct Answer
        </label>
        <button type="button" @click="removeAnswer(index)">Remove</button>
      </div>
      <button type="button" @click="addAnswer">Add Answer</button>
      <br>
      <button type="submit">Save</button>
      <button @click="cancelEdit">Cancel</button>
    </form>
  </div>
</template>

<script>
import ImageUpload from './ImageUpload.vue';
import QuizApiService from '../services/QuizApiService';
import AdministrationStorageService from '../services/AdministrationStorageService';

export default {
  components: {
    ImageUpload
  },
  data() {
    return {
      questionId: null,
      question: {
        position: 0,
        title: '',
        text: '',
        image: null,
        possibleAnswers: [],
      },
      imageUrl: '',
    };
  },
  mounted() {
    this.loadQuestion();
  },
  methods: {
    saveQuestion() {
      const token = AdministrationStorageService.getToken();
      if (typeof this.$route.params.id === 'undefined') {
        QuizApiService.addQuestion(this.question,token)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.error(error);
          });
      }
      else{
        QuizApiService.updateQuestion(this.$route.params.id,this.question,token)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    cancelEdit() {
      this.$router.go(-1);
    },
    loadQuestion() {
      this.questionId = this.$route.params.id;
      if (typeof this.questionId !== 'undefined') {
        QuizApiService.getQuestionById(this.questionId)
          .then((response) => {
            this.question = response.data;
            if (this.question.image) {
              this.imageUrl = this.question.image;
            }
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    handleImageChange(fileDataUrl) {
      if (fileDataUrl) {
        this.question.image = fileDataUrl;
        this.imageUrl = fileDataUrl;
      } else {
        this.question.image = null;
        this.imageUrl = '';
      }
    },
    addAnswer() {
      this.question.possibleAnswers.push({ text: '', correct: false });
    },
    removeAnswer(index) {
      this.question.possibleAnswers.splice(index, 1);
    },
  },
};
</script>

<style>
.max-dimensions {
  max-width: 100%;
  max-height: 100%;
}
</style>
