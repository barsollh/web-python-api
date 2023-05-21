<template>
  <div>
    <QuestionsManager />
  </div>
</template>

<script>
import QuestionsManager from "@/components/QuestionManager.vue";

export default {
  name: "QuestionsPage",
  components:{
    QuestionsManager
  },
  data() {
    return {
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
