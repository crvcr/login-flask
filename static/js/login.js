console.log("-- app started ---------------");

var app = new Vue({
  el: '#app',
  data: {
    formUser: {
      username: '',
      password: '',
    },
    message: '',
    error: '',
    state: 'idle'
  },
  methods: {
    login() {
      this.error = '';

      if (!this.formUser.username || !this.formUser.password) {
        this.error = 'Username y password son datos requeridos';
        this.state = 'error';
        return;
      }

      this.state = 'loading';

      setTimeout(() => {
        axios.post('/authenticate', {
          username: this.formUser.username,
          password: this.formUser.password
        }).then((response) => {
          console.log(response);
          var data = response.data;
  
          if (!data.ok) {
            this.error = data.error;
            this.state = 'error';
            return;
          }
          this.message = data.data.message;
          // location.href = "/";
          this.state = 'success';

          // this.formUser.username = "";
          // this.formUser.password = "";
          this.$refs.usernameInput.focus();
        }).catch((error) => {
          console.log(error);
          this.error = error;
          this.state = 'error';
        });
      }, 500);
    }
  }
});