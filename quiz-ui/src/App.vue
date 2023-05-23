<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app">
    <header>
      <div class="wrapper">
        <nav class="fixed-top navbar navbar-expand-lg navbar-light custom-navbar">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">
              <img src="./assets/QuizAppLogo4.png" alt="Logo" class="navbar-logo">
            </a>
            <RouterLink to="/" class="navbar-brand" style="color: white;"><b>Home</b></RouterLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <RouterLink to="/about" class="nav-link" style="color: white;">About</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink to="/admin" class="nav-link" style="color: white;">Admin</RouterLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </header>
    <main class="content" style="margin-top: 70px;">
      <div class="container">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<style scoped>
.navbar-logo {
  max-height: 40px;
}

.custom-navbar {
  /* background-color: #C4FF61; */
  /* background-color: #4182D8; */
  background-color: #4F8BDB;

}
</style>
