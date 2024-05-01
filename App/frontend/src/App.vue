<script>
  export default {
    data() {
      return {
        respo: [],
        i: 0,
        nb: 0,
        all: 0,
        gift: "",
        gender: "she",
        question: "",
        questions: [
          {
            question: "Your gift is for a women?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he/she like to travel?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he/she like pets?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he/she play music?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he/she play video games?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he/she practice a sport?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he/she like to read?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he/she like beauty accessories?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he have a driver's license?",
            options: ["Yes", "No"],
            selected: null,
          },
          {
            question: "Does he like buying new clothes?",
            options: ["Yes", "No"],
            selected: null,
          },
        ],
        quizComped: false,
        currentQuestion: 0,
      };
    },
    methods: {
      SetAnswer() {
        this.respo[this.i] = this.questions[this.currentQuestion].selected;
        console.log(this.respo[this.i]);
        this.respo[1] == 0;
      },

      NextQuestion() {
        if (this.currentQuestion < this.questions.length - 1) {
          this.currentQuestion++;

          this.i++;

          console.log(this.questions.length);
          if (this.respo[0] == 1) this.gender = "he";
          return;
        }
        for (var j = 1; j < this.respo.length; j++) {
          if (this.respo[j] == 1) this.nb++;
        }
        if (this.nb == this.respo.length - 1) {
          this.all = 1;
        }
        this.postData();
        this.quizComped = true;
      },

      postData() {
        fetch("http://localhost:5000/post", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            genre: this.respo[0],
            travel: this.respo[1],
            pets: this.respo[2],
            music: this.respo[3],
            videogames: this.respo[4],
            sport: this.respo[5],
            reading: this.respo[6],
            accessoires: this.respo[7],
            drive: this.respo[8],
            clothes: this.respo[9],
            all: this.all,
          }),
        })
          .then((resp) => resp.json())
          .then((data) => {
            console.log(data);
            this.gift = data["cadeau"];
          });
      },
      changeKey() {
        window.location.reload();
      },
    },
    computed: {
      getCurrentQuestion() {
        var question;
        question = this.questions[this.currentQuestion];
        question.index = this.currentQuestion;
        return question;
      },
    },
  };
</script>

<template>
  <main class="app">
    <div class="statsWrapper">
      <div class="row">
        <div class="first-col" v-if="!quizComped">
          <div class="col">
            <div>
              <span class="question">
                <p class="locationTitle">Confused?</p></span
              >
            </div>
            <div>
              <span class="question">
                <p class="question">Fill in this form</p></span
              >
            </div>
            <div class="img">
              <img
                src="./assets/boite-cadeau.png"
                alt="alternatetext"
                width="150"
                height="150"
              />
            </div>
          </div>
        </div>
        <div class="first-col" v-else>
          <div class="col">
            <div>
              <span class="question">
                <p class="locationTitle">
                  Hope {{ this.gender }} likes it!
                </p></span
              >
            </div>
            <div></div>
            <div class="img">
              <img
                src="./assets/finger.png"
                alt="alternatetext"
                width="150"
                height="150"
              />
            </div>
          </div>
        </div>
        <div class="col">
          <section class="quiz" v-if="!quizComped">
            <div class="quiz-info">
              <span class="question">{{ getCurrentQuestion.question }}</span>
              <span class="score"
                >Question {{ i + 1 }}/{{ this.questions.length }}</span
              >
            </div>

            <div class="options">
              <label
                v-for="(option, index) in getCurrentQuestion.options"
                :key="index"
                :for="'option' + index"
                :class="`option ${
                  getCurrentQuestion.selected == index
                    ? index == 0
                      ? 'correct'
                      : 'wrong'
                    : ''
                } `"
              >
                <input
                  type="radio"
                  :id="'option' + index"
                  :name="getCurrentQuestion.index"
                  :value="index"
                  v-model="getCurrentQuestion.selected"
                  @change="SetAnswer"
                />
                <span>{{ option }}</span>
              </label>
            </div>

            <button
              @click="this.NextQuestion()"
              :disabled="getCurrentQuestion.selected == null"
            >
              {{
                getCurrentQuestion.index == this.questions.length - 1
                  ? "Finish"
                  : getCurrentQuestion.selected == null
                  ? "Select an option"
                  : "Next question"
              }}
            </button>
          </section>

          <section v-else>
            <br />
            <h2>You have finished the quiz!</h2>
            <span
              ><p>Your best gift :</p>
              <p class="locationTitle">{{ gift }}</p></span
            >
            <div class="try_again">
              <button @click="this.changeKey()">Try again</button>
            </div>
          </section>
        </div>
      </div>
    </div>
  </main>
</template>

<style>
  @font-face {
    font-family: "Montserrat";
    src: url("../Montserrat/static/Montserrat-Bold.ttf");
  }

  @font-face {
    font-family: "Montserrat1";
    src: url("../Montserrat/static/Montserrat-Medium.ttf");
  }
  .locationTitle {
    color: black;
    font-size: 38px;
    margin-bottom: 10px;
    font-family: "Montserrat";
  }
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-size: inherit;
    font-weight: inherit;
  }
  blockquote,
  dd,
  dl,
  figure,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  hr,
  p,
  pre {
    margin: 0;
    margin-bottom: 0px;
  }
  .try_again {
    text-align: center;
    margin-top: 30px;
  }
  .statsWrapper {
    margin-top: 150px;
    background-color: #ede6d6;
    padding: 30px;
    /* text-align: left;*/
    border-radius: 30px 30px 30px 30px;
    box-shadow: 2px 2px 2px 1px rgba(0.2, 0.2, 0.2, 0.2);
    --tw-ring-shadow: 0 0 transparent;
    width: 50%;
    font-family: "Montserrat1";
  }
  body {
    color: #fff;
  }

  .img {
    margin-top: 20px;
    margin-left: 60px;
  }

  .app {
    background-color: #f6f2eb;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    height: 100vh;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
  .first-col {
    background-color: eae0c8;

    border-radius: 30px;
    width: 300px;
  }

  .quiz {
    background: #e3d2bc;
    border-radius: 20px;
    padding: 20px;
    width: 100%;
    margin-top: 15px;
  }

  .quiz-info {
    text-align: left;
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
  }

  .question {
    font-size: 1.5rem;
  }

  .quiz-info.score {
    color: white;
    font-size: 1.4rem;
  }

  .options {
    margin-bottom: 1rem;
  }

  .option {
    padding: 1rem;
    display: block;
    background-color: #d4b996ff;
    margin-bottom: 0.5rem;
    border-radius: 0.5rem;
    cursor: pointer;
  }

  .option:hover {
    background-color: #dbc2ad;
  }

  .option.correct {
    background-color: #dbc2ad;
  }

  .option.wrong {
    background-color: #dbc2ad;
  }

  .option:last-of-type {
    margin-bottom: 0;
  }

  .option.disabled {
    opacity: 0.5;
  }

  .option input {
    display: none;
  }
  .row {
    margin-top: 15px;
  }

  button {
    appearance: none;
    outline: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem 1rem;
    background-color: #d4b996ff;
    color: white;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 1.2rem;
    border-radius: 0.5rem;
  }

  button:disabled {
    opacity: 0.5;
  }

  h2 {
    font-size: 2rem;
    margin-bottom: 2rem;
    text-align: center;
  }

  p {
    color: #8f8f8f;
    font-size: 1.5rem;
    text-align: center;
  }
</style>
