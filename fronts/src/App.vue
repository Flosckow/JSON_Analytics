<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<style>
    @import "assets/css/bootstrap.css";
    @import "assets/css/style.css"
</style>

<script>

export default {
  name: 'app',
  data () {
    return {
      sign: 'sign-in',
      signComplete: false
    }
  },
  components: { },
  methods: {
    switchSign (currentSign) {
      this.sign = currentSign
    }
  }
}
</script>
