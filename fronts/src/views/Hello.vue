<template>
  <div class="custom">
    <a href="#" class="editContent">Welcome to AS</a>
    <ul>
      <li><button @click="goLogin" class="login">Login</button></li>
      <li><button @click="goRegistration" class="login">Registration</button></li>
      <li><button @click="goAP" class="login">Personal Account</button></li>
      <li><button @click="goAbout" class="login">About</button></li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Hello',
  methods: {
    goLogin () {
      this.$router.push({ name: 'Login' })
    },
    goRegistration () {
      this.$router.push({ name: 'Register' })
    },
    goAP () {
      this.$router.push({ name: 'LK' })
    }
  }
}
</script>

<style>
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}
li {
    float: right;
}
.login {
        display: inline-block;
        padding: 10px 15px;
        font-size: 14px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #dd9475;
        border: none;
        border-radius: 15px;
        box-shadow: 0 9px #999;
        margin-left: 5px;
        margin-right: 5px
    }
.login:hover {background-color: ##DCDCDC}
.login:active {
        background-color: #3e8e41;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
.editContent {
        outline: none;
        outline-offset: -2px;
        cursor: inherit;
        position: absolute;
        color: #efca0e;
        font-size: 25px;
        background-color: rgba(0, 0, 0, 0);
        font-family: Source Sans Pro, sans-serif;
    }
</style>
