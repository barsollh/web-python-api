<template>
  <div>
    <div>
      <h1 class="text-md-start">Bienvenue sur QuizAi !</h1>
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
          Bienvenue sur QuizAi. Cette application a été réalisée par BARSOLLE Hugo et BLITZ Benjamin. Nous sommes deux
          étudiants d'ESIEE Paris en 4ème année dans la filière Informatique et Applications, ingénierie 3D et technologie
          des médais. Ceci est notre toute première application Vuejs créée dans le cadre de l'unité 22_E4FI_4I_IN6 - Web
          Full Stack.
          <br>
          <br>
          Sur cette App, vous pouvez effectuer un Quiz composé de plusieurs questions. Pour chaque question, une œuvre
          d'art s'affiche. Votre objectif est de déterminé qui, parmis les artistes ou IA proposés a réalisé cette œuvre.
          Une seule réponse est possible.
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
