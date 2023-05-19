import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info")
    .then(response => {
      //console.log("retour appel quizinfo : ", response);
      return response;
    });
  },
  getQuestionByPosition(position) {
    return this.call("get", `questions?position=${position}`)
    .then(response => {
      // console.log("retour appel getQuestion : ", response);
      return response;
    });
  },
  getQuestionById(id) {
    return this.call("get","questions",id);
  },
  addParticipation(payload) {
    return this.call("post", "participations", payload)
      .then(response => {
        return response;
      });
  }
};