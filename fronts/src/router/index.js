import { createRouter, createWebHashHistory } from 'vue-router'

import SignUp from '../components/SignUp.vue'
import SignIn from '../components/SignIn.vue'
import PersonalAccount from '../components/PersonalAccount.vue'
import Hello from '../views/Hello.vue'
const routes = [
  {
    path: '/registration',
    name: 'Register',
    meta: {},
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    meta: {},
    component: SignIn
  },
  {
    path: '/',
    name: 'Main',
    meta: {},
    component: Hello
  },
  {
    path: '/lk',
    name: 'LK',
    meta: {},
    component: PersonalAccount
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
