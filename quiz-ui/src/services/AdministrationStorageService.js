export default {
  clear() {
    window.localStorage.clear();
  },
  setToken(token){
    localStorage.setItem('authToken', token);
  },
  getToken(){
    return window.localStorage.getItem("authToken");
  }
};