<template>
  <div class="about">
    <h1>Questions page</h1>
  </div>
</template>

<script>
export default {
  name: "QuestionsPage",
  data() {
    return {
      registeredScores : []
    };
  },
};
</script>


<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
