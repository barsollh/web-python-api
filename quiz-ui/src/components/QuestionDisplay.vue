<template>
  <div class="justify-content-center">
    <div class="row">
      <div class="col-lg-12 d-flex align-items-center justify-content-center">
        <div class="card" style="background-color: #222222; color: white;">
          <img v-if="question.image" :src="question.image" class="card-img-top" alt="...">
          <div class="card-body">
            <h2 class="card-title text-center">{{ question.text }}</h2>
            <h3 class="card-text text-start"></h3>
            <ul class="list-group list-group-flush">
              <li class="answer-link list-group-item cursor-pointer" v-for="(answer, index) in question.possibleAnswers"
                :key="index" @click.prevent="selectAnswer(index)">
                <a>{{ answer.text }}</a>
              </li>
            </ul>
          </div>
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
  methods: {
    selectAnswer(index) {
      this.$emit('answer-selected', index);
    },
  },
  emits: ["answer-selected", "end-quiz"]
};
</script>

<style scoped>
.answer-link {
  background-color: #373737;
  color: white;
  transition: background-color 0.3s ease;
}

.answer-link:hover {
  background-color: #565656;
}
</style>
