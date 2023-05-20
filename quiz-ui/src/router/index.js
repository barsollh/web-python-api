import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsPage from '../views/QuestionsPage.vue'
import ScorePage from '../views/ScorePage.vue'
import AdminPage from '../views/Admin.vue'
import QuestionAdminDisplay from '../components/QuestionAdminDisplay.vue'
import QuestionsList from '../components/QuestionsList.vue';
import QuestionEdition from '../components/QuestionEdition.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: '/start-new-quiz-page',
      name: 'StartNewQuizPage',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'QuestionsPage',
      component: QuestionsPage
    },
    {
      path: '/score',
      name: 'ScorePage',
      component: ScorePage
    },
    {
      path: '/admin',
      name: 'AdminPage',
      component: AdminPage
    },
    {
      path: '/questions',
      name: 'QuestionsList',
      component: QuestionsList,
    },
    {
      path: '/questions/create',
      name: 'QuestionCreation',
      component: QuestionEdition,
    },
    {
      path: '/questions/:id',
      name: 'QuestionAdminDisplay',
      component: QuestionAdminDisplay,
    },
    {
      path: '/questions/:id/edit',
      name: 'QuestionEdition',
      component: QuestionEdition,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
