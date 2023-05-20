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
    return this.call("get", `questions/${id}`);
  },
  addParticipation(payload) {
    return this.call("post", "participations", payload)
      .then(response => {
        return response;
      });
  },
  login(password) {
    const payload = {
      password: password
    };
  
    return instance
      .post('login', payload)
      .then((response) => {
        return response.data.token;
      })
      .catch((error) => {
        console.error(error);
        throw error;
      });
  },
  addQuestion(payload, token) {
    return this.call("post", "questions", payload, token)
      .then((response) => {
        return response;
      });
  },
  deleteQuestionById(id, token) {
    return this.call("delete", `questions/${id}`, null, token)
      .then((response) => {
        return response;
      });
  },
  deleteAllQuestions(token) {
    return this.call("delete", "questions/all", null, token)
      .then((response) => {
        return response;
      });
  },
  updateQuestion(id, payload, token) {
    return this.call("put", `questions/${id}`, payload, token)
      .then((response) => {
        return response;
      });
  },
  deleteAllParticipations(token) {
    return this.call("delete", "participations/all", null, token)
      .then((response) => {
        return response;
      });
  },
  postParticipation(payload) {
    return this.call("post", "participations", payload)
      .then((response) => {
        return response;
      });
  },
  getQuestions() {
    return this.call("get", "allquestions")
      .then(response => {
        return response;
      });
  }
};