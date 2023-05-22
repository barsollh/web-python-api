<template>
  <div class="d-flex flex-column align-items-center" style="margin-bottom: 30px;">
    <h2>Question Edition</h2>
    <div class="input-group flex-nowrap justify-content-center">
      <form @submit.prevent="saveQuestion">
        <label for="position">Position:</label>
        <input type="number" class="form-control" id="position" v-model="question.position" :min="minPosition"
          :max="maxPosition" required><br>
        <label for="title">Title:</label>
        <input type="text" class="form-control" placeholder="Title" id="title" v-model="question.title" required><br>
        <label for="text">Text:</label>
        <textarea class="form-control" id="text" v-model="question.text" required></textarea><br>
        <label for="image">Image:</label>
        <image-upload @file-change="handleImageChange"></image-upload><br>
        <img :src="imageUrl" alt="Preview" v-if="imageUrl" class="max-dimensions"><br>
        <h3>Possible Answers:</h3>
        <div v-for="(answer, index) in question.possibleAnswers" :key="answer.id">
          <label>
            <div class="input-group mb-3">
              <input type="text" class="form-control" v-model="answer.text" required>
              <div class="input-group-text"> Correct Answer &nbsp;
                <input class="form-check-input mt-0" type="checkbox" v-model="answer.isCorrect">
              </div>
              <button type="button" @click="removeAnswer(index)" class="btn btn-outline-danger">Remove</button>
            </div>
          </label>
        </div>
        <button type="button" @click="addAnswer" class="btn btn-outline-secondary">Add Answer</button>
        <br>
        <br>
        <button type="submit" class="btn btn-success">Save</button>
        &nbsp;
        &nbsp;
        <button @click="cancelEdit" class="btn btn-warning">Cancel</button>
      </form>
    </div>
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
        position: 1,
        title: '',
        text: '',
        image: null,
        possibleAnswers: [],
      },
      minPosition: 1,
      maxPosition: 100,
      creationMode: false,
      imageUrl: '',
    };
  },
  async mounted() {
    if (typeof this.$route.params.id === 'undefined') this.creationMode = true;
    else this.questionId = this.$route.params.id;

    const infos = await QuizApiService.getQuizInfo();
    this.maxPosition = infos.data.size;
    if (this.creationMode) this.maxPosition++;

    this.loadQuestion();
    this.initializeQuestionCopy();
  },
  methods: {
    saveQuestion() {
      const token = AdministrationStorageService.getToken();
      if (this.creationMode) {
        QuizApiService.addQuestion(this.question, token)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.error(error);
          });
      }
      else {
        QuizApiService.updateQuestion(this.questionId, this.question, token)
          .then(() => {
            this.$router.go(-1);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    initializeQuestionCopy() {
      this.questionCopy = { ...this.question };
    },
    cancelEdit() {
      this.question = { ...this.questionCopy };
      this.$router.go(-1);
    },
    loadQuestion() {
      if (!this.creationMode) {
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
      this.question.possibleAnswers.push({ text: '', isCorrect: false });
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
