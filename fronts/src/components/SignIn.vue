<template>
  <form class="mt-5" @submit.prevent="loginUser">
    <div class="align-self-center">
      <label for="text">Вход</label>
    </div>
    <div class="form-group">
      <label for="email">Ваш email:</label>
      <input type ="email" class="form-control" id="email" placeholder="Введите email:"  v-model="user.email">
    </div>
    <div class="form-group">
      <label for="password">Ваш username:</label>
      <input type ="text" class="form-control" id="username" placeholder="Введите username:" required v-model="user.username">
    </div>
    <div class="form-group">
      <label for="password">Ваш password:</label>
      <input type ="password" class="form-control"
       id="password" placeholder="Введите password:"
       v-model="user.password">
    </div>
    <div class="form-group">
      <label for="company">Введите компанию:</label>
      <input type ="text" class="form-control" id="company"
       placeholder="Введите company:"  v-model="user.company">
    </div>
    <button type="submit" class="button">Вход</button>
  </form>
</template>

<script>

import { required, sameAs, minLength } from 'vuelidate/lib/validators'
import $ from 'jquery'
export default {
  name: 'SignUp',
  data () {
    return {
      user: {
        username: '',
        password: '',
        company: ''
      }
    }
  },
  validations: {
    user: {
      password: {
        required,
        minLength: minLength(6)
      },
      confirmPassword: { required, sameAsPassword: sameAs('password') }
    }
  },
  methods: {
    loginUser () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/jwt/create/',
        type: 'POST',
        data: {
          email: this.user.email,
          password: this.user.password,
          username: this.user.username,
          company: this.user.company
        },
        success: (response) => {
          // localStorage.setItem('auth_key', response.access)
          localStorage.setItem('authentication', true)
          localStorage.setItem('company', this.company)
          this.$router.push({ name: 'LK' })
        },
        error: (response) => {
          if (response.status === 401) {
            alert('логин или пароль неверный')
          }
        }
      })
    }
  }
}
</script>

<style scoped>
  .error {
    color: red;
  }
  .mt-5 {
    position: absolute;
    top: 25%;
    left: 50%;
    margin: -100px 0 0 -200px; /* отступы равны половинным размера формы */
    z-index: 9999; /* чтобы форма была поверх всех элементов страницы */
  }
  .form-group {
    margin: 0 auto;
    width:250px;
  }
  .align-self-center{
    padding-bottom: 10px;
    margin-left: auto;
    margin-right: auto;
    width: 6em;
    font-family: "Muli", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  color: #000;
  }
.button {
  float: center;
  color: #7f8084;
  border: 1px solid #22272d;
  border-radius: 3px;
  font-size: 1em;
  cursor: pointer;
  margin: 10px;
  padding: 7px 105px;
}

.button:hover {
  color: #d3d3d3;
}
body {

  font-family: 'Roboto', sans-serif;
}
</style>
