<template>
  <div>
    <div>
      <h1 class="text-md-start">Bienvenue sur QuizApp !</h1>
    </div>
    <div class="d-flex flex-row" style="justify-content: space-around;">
      <br>
      <br>
      <br>
      <span>
        <p>
          Bonjour,
          <br>
          <br>
          Bienvenue sur QuizApp. Cette application a été réalisé par BARSOLLE Hugo et BLITZ Benjamin. Nous sommes deux
          étudiants d'ESIEE Paris en 4ème année dans la filière Informatique et Applications, ingénierie 3D et technologie
          des médais. Ceci est notre toute première application Vuejs.
          <br>
          <br>
          Sur cette App, vous pouvez effectuer un Quiz composé de plusieurs questions.
          À chaque question est associée une liste de réponses. Il peut y avoir plusieurs bonnes réponses mais vous ne
          pouvez sélectionner qu'une seule d'entre elles.
          Attention ! Si vous cliquez sur une réponse, celle-ci sera sélectionnée et vous passerez directement à la
          question suivante sans pouvoir revenir en arrière.
          Une bonne réponse vous rapportera 1 point, une mauvaise réponse vous en raportera 0. À la fin du Quiz vous
          obtiendrez votre score et votre classement parmi les autres participants.
          <br>
          <br>
          Bonne chance à tous !
        </p>
      </span>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
