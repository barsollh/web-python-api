<template>
  <div class="question-display">
    <h2>{{ question.title }}</h2>
    <img v-if="question.image" :src="question.image" />
    <p>{{ question.text }}</p>
    <ul>
      <li v-for="(answer, index) in question.possibleAnswers" :key="index">
        <a @click.prevent="selectAnswer(index)">{{ answer.text }}</a>
      </li>
    </ul>
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
    }
  },
  emits: ["answer-selected"]
};
</script>
