<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app">
    <header>
      <div class="wrapper">
        <nav class="fixed-top navbar navbar-expand-lg bg-body-tertiary navbar-light bg-light">
          <div class="container-fluid">
            <RouterLink to="/" class="navbar-brand">Home</RouterLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <RouterLink to="/about" class="nav-link">About</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink to="/admin" class="nav-link">Admin</RouterLink>
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

<style scoped></style>
