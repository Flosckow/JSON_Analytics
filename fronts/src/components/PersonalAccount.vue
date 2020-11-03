<template>
  <div class="format_z">Hello {{getUsCompany()}}</div>
  <form v-on:submit.prevent="submitFile" method="POST" class="mt-5" >
    <label for="myfile">Select a file:</label>
    <input type="file" id="myfile" ref="file" name="file" v-on:change="handleFileUpload()"><br><br>
    <label for="fname">Введите поле по оси х:</label>
    <br><input type="text" id="x_field" name="x_field" ><br>
    <label for="fname">Введите поле по оси y:</label>
    <br><input type="text" id="y_field" name="y_field" ><br>
    <br><input type="submit" value="Отправить"><br>
  </form>
</template>

<style scoped>
.mt-5 {
  position: absolute;
  top: 2%;
  left: 50%;
  margin: -100px 0 0 -200px; /* отступы равны половинным размера формы */
  z-index: 9999; /* чтобы форма была поверх всех элементов страницы */
}
.format_z {
  position: absolute;
  font-size: 30px;
  left: 40%;
}

</style>

<script>
import axios from 'axios'
export default {
  name: 'PersonalAccount',
  data () {
    return {
      file: '',
      x_field: '',
      y_field: ''
    }
  },
  methods: {
    submitFile () {
      const formData = new FormData()

      formData.append('file', this.file)
      formData.append('x_field', this.x_field)
      formData.append('y_field', this.y_field)
      for (var pair of formData.entries()) {
        console.log(pair[0] + ' - ' + pair[1])
      }

      axios.post('http://127.0.0.1:8000/lk/file/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      ).then(function () {
        console.log('SUCCESS!!')
      }).catch(function (re) {
        console.log('FAILURE!!')
        window.location.href = 'http://127.0.0.1:8000/lk/render'
      })
    },
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    },
    getUsCompany () {
      var company = localStorage.getItem('company')
      return company
    }
  }
}
</script>
