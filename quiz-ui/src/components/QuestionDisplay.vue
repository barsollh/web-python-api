<template>
  <div class="justify-content-center">
    <div class="row">
      <div class="col-lg-12 d-flex align-items-center justify-content-center">
        <div id="card1" class="card" style="background-color: #222222; color: white;">
          <img id="image" v-if="question.image" :src="question.image" class="card-img-top">
          <div class="card-body">
            <h2 class="card-title text-center">{{ question.text }}</h2>
            <h3 class="card-text text-start"></h3>
          </div>
          <ul class="list-group list-group-flush">
            <li class="answer-link list-group-item cursor-pointer" v-for="(answer, index) in question.possibleAnswers"
              :key="index" @click.prevent="selectAnswer(index)" :class="{ 'selected': index === selectedAnswer }"
              :style="{ backgroundColor: selectedAnswerColor(index) }">
              <a style="color: white;">{{ answer.text }}</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object
    }
  },
  data() {
    return {
      selectedAnswer: null,
      previousQuestionIndex: null,
      showColors: false
    };
  },
  methods: {
    selectAnswer(index) {
      this.selectedAnswer = index;
      this.showColors = true;
      setTimeout(() => {
        this.showColors = false;
        this.$emit('answer-selected', index);
      }, 250);
    },
    selectedAnswerColor(index) {
      if (this.showColors) {
        if (index === this.selectedAnswer) {
          if (this.question.possibleAnswers[index].isCorrect) {
            return '#B0F2B6';
          } else {
            return '#FF6961';
          }
        }
      }
      return 'transparent';
    }
  },
  emits: ["answer-selected", "end-quiz"],
};
</script>

<style scoped>
.answer-link {
  background-color: #373737;
  transition: background-color 0.3s ease;
}

.answer-link:hover {
  background-color: #565656;
}

.answer-link.selected {
  background-color: transparent;
}

#card1 {
  max-width: 40rem;
}
</style>
