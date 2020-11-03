<template>
  <form class="mt-5" @submit.prevent="registerUser">
    <div class="align-self-center">
      <label for="text">Регистарция</label>
    </div>
    <div class="form-group">
      <label for="password">Ваш username:</label>
      <input type ="text" class="form-control" id="username" placeholder="Введите username:" required v-model="user.username">
    </div>
    <div class="form-group">
      <label for="email">Ваш email:</label>
      <input type ="email" class="form-control" id="email" placeholder="Введите email:"  v-model="user.email">
    </div>
    <div class="form-group">
      <label for="password">Ваш password:</label>
      <input type ="password" class="form-control"
       id="password" placeholder="Введите password:"
       v-model="user.password">
    </div>
    <div class="form-group">
      <label for="password2">Подтвердите password:</label>
      <input type ="password" class="form-control" id="confirmPassword"
       placeholder="Введите password:"  v-model="user.confirmPassword">
    </div>
    <button type="submit" class="button">Зарегистрироваться</button>
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
        email: '',
        company: '',
        username: '',
        password: '',
        password1: ''
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
    registerUser () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/',
        type: 'POST',
        data: {
          email: this.user.email,
          username: this.user.username,
          password: this.user.password,
          password1: this.user.password1
        },
        success: (response) => {
          console.log(response)
          console.log(this.user)
        },
        error: (response) => {
          alert('Произошла ошибка')
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
  font-size: 0.9em;
  cursor: pointer;
  margin: 10px;
  padding: 10px 60px;
}

.button:hover {
  color: #d3d3d3;
}
</style>
