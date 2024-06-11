import React, { Component } from "react";
import { ArrowLeftIcon } from "@heroicons/react/24/solid";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouterHooks } from "../../../../withRouters/withRoutersHook";
import {
  fetchSubjectQuestions,
  startTest,
  completeTest,
  deleteTestInstance,
  submitAnswer,
} from "../../../../Actions/Quiz";
import { resetStateOnLeavePage } from "../../../../Actions/Reset";

class Evaluation extends Component {
  static propTypes = {
    subjectQuestions: PropTypes.array.isRequired,
    testInstances: PropTypes.object.isRequired,
    startTest: PropTypes.func.isRequired,
    navigate: PropTypes.func.isRequired,
    fetchSubjectQuestions: PropTypes.func.isRequired,
    deleteTestInstance: PropTypes.func.isRequired,
    completeTest: PropTypes.func.isRequired,
    resetStateOnLeavePage: PropTypes.func.isRequired,
    navigate: PropTypes.func.isRequired,
    submitAnswer: PropTypes.func.isRequired,
  };

  state = {
    currentQuestionIndex: 0,
    selectedOption: null,
    loading: true,
    nextIndex: 0,
    remainingTime: null,
    selectedOptions: {},
  };

  timerInterval = null;

  handleTimesUp = () => {
    this.props.completeTest(this.props.testInstances.id);
    this.props.navigate("/summary");
  };

  componentWillUnmount() {
    this.stopTimer();
  }

  startTimer = () => {
    this.timerInterval = setInterval(() => {
      this.setState(
        (prevState) => ({
          remainingTime: prevState.remainingTime - 1,
        }),
        () => {
          if (this.state.remainingTime <= 0) {
            this.stopTimer();
            this.handleTimesUp();
          }
        }
      );
    }, 1000);
  };

  stopTimer = () => {
    clearInterval(this.timerInterval);
  };

  componentDidMount() {
    const { testInstances, fetchSubjectQuestions } = this.props;
    if (testInstances && testInstances.id) {
      this.setState({ loading: true });
      fetchSubjectQuestions(testInstances.id)
        .then((data) => {
          this.setState({ loading: false });
        })
        .catch((error) => {
          console.error("Fetching questions failed:", error);
          this.setState({ loading: false });
        });
    }
    const { duration } = this.props.testInstances;
    if (duration) {
      this.setState({ remainingTime: duration });
      this.startTimer();
    }
  }

  handleNextQuestion = () => {
    this.setState((prevState, props) => {
      const nextIndex = prevState.currentQuestionIndex + 1;
      if (nextIndex < props.subjectQuestions.length) {
        return { currentQuestionIndex: nextIndex };
      }
    });
  };

  handlePreviousQuestion = () => {
    this.setState((prevState) => {
      const newIndex = Math.max(0, prevState.currentQuestionIndex - 1);
      return { currentQuestionIndex: newIndex };
    });
  };

  handleOptionChange = (option, index) => {
    const { subjectQuestions } = this.props;
    const questionId = subjectQuestions[this.state.currentQuestionIndex].id;
    const optionLetter = ["A", "B", "C", "D", "E"][index];

    this.setState(
      (prevState) => ({
        selectedOptions: {
          ...prevState.selectedOptions,
          [questionId]: optionLetter,
        },
      }),
      () => {
        this.props.submitAnswer(
          this.props.testInstances.id,
          questionId,
          optionLetter
        );
      }
    );
  };

  handleCancelTest = () => {
    const shouldCancel = window.confirm(
      "Are you sure you want to cancel the test? Your progress would be lost."
    );

    if (shouldCancel) {
      const testInstanceId = this.props.testInstances.id;

      this.props.resetStateOnLeavePage();
      this.props.deleteTestInstance(testInstanceId);
      this.props.navigate("/dashboard");
    }
  };

  handleCompleteTest = () => {
    const shouldComplete = window.confirm(
      "Are you sure you want to submit your answers?"
    );
    const { testInstances } = this.props;
    if (testInstances && testInstances.id && shouldComplete) {
      this.props.completeTest(testInstances.id);
      this.props.navigate("/dashboard/summary");
    }
  };

  handleTimesUp = () => {
    this.props.completeTest(this.props.testInstances.id);
    this.props.navigate("/dashboard/summary");
  };

  renderQuestion = () => {
    const { subjectQuestions } = this.props;
    const { currentQuestionIndex, selectedOptions } = this.state;

    if (this.state.loading) {
      return <div>Loading questions...</div>;
    }

    if (!subjectQuestions || subjectQuestions.length === 0) {
      return <div>No questions available.</div>;
    }

    const currentQuestion = subjectQuestions[currentQuestionIndex];
    const questionId = currentQuestion.id;
    const selectedOption = selectedOptions[questionId];

    const options = [
      currentQuestion.option_A,
      currentQuestion.option_B,
      currentQuestion.option_C,
      currentQuestion.option_D,
      currentQuestion.option_E,
    ].filter((option) => option !== undefined && option !== "");

    return (
      <div className="flex flex-col gap-4 mt-4">
        <div className="font-[500] h-fit text-[2.25rem]">
          {currentQuestion.question}
        </div>
        {options.map((option, index) => (
          <div key={index} className="flex items-center gap-4">
            <label className="flex items-center gap-4 cursor-pointer">
              <input
                type="radio"
                name={`option-${questionId}`}
                className="w-[1.938rem] h-[1.938rem]"
                checked={selectedOption === ["A", "B", "C", "D", "E"][index]}
                onChange={() => this.handleOptionChange(option, index)}
              />
              <div className="font-[600] text-[2rem]">{option}</div>
            </label>
          </div>
        ))}
      </div>
    );
  };

  render() {
    const { subjectQuestions, testInstances } = this.props;
    const totalQuestions = subjectQuestions.length;
    const displayIndex = this.state.currentQuestionIndex + 1;
    const { remainingTime } = this.state;
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;

    return (
      <div className=" flex flex-col w-screen h-screen">
        <div className="flex w-screen justify-center shadow-xl">
          <div className="flex flex-row w-[80%] h-[6.375rem] justify-between items-center">
            <div className="flex gap-4 items-center">
              <button
                onClick={this.handleCancelTest}
                className="flex w-[1.8rem] h-[1.8rem]"
              >
                <ArrowLeftIcon />
              </button>
              <div className="font-[700] text-[1.5rem] text-purple-primary">
                {testInstances && testInstances.subject} Question:{" "}
                {testInstances.year}
              </div>
            </div>
            <div className="flex text-[#2D9CDB] text-[1.5rem] font-[700] items-center">
              <div>
                Timer: {minutes}:{seconds < 10 ? `0${seconds}` : seconds}
              </div>
            </div>
          </div>
        </div>
        <div className="flex w-screen justify-center mt-[8.25rem]">
          <div className="flex flex-col w-[80%] mt-[rem] gap-4">
            <div className="font-[400] text-[#3C3C3C] text-[1.5rem]">
              Question {displayIndex}/{totalQuestions}
            </div>
            {this.renderQuestion()}
            <div className="flex justify-between pt-[3rem]">
              {this.state.currentQuestionIndex > 0 && (
                <button
                  className="bg-purple-primary w-[12.25rem] h-[4.5rem] rounded-lg font-[700] text-white text-[1.5rem]"
                  onClick={this.handlePreviousQuestion}
                >
                  Previous
                </button>
              )}
              <button
                className="bg-[#BBE6FF] w-[12.25rem] h-[4.5rem] rounded-lg font-[700] text-[1.5rem]"
                onClick={() => {
                  if (
                    this.state.currentQuestionIndex ===
                    this.props.subjectQuestions.length - 1
                  ) {
                    this.handleCompleteTest();
                  } else {
                    this.handleNextQuestion();
                  }
                }}
                disabled={this.state.loading}
              >
                {this.state.currentQuestionIndex ===
                this.props.subjectQuestions.length - 1
                  ? "Submit"
                  : "Next"}
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  subjectQuestions: state.quiz.subjectQuestions,
  testInstances: state.quiz.testInstances,
  submitAnswer: state.quiz.submitAnswer,
});

const mapDispatchToProps = {
  fetchSubjectQuestions,
  startTest,
  completeTest,
  resetStateOnLeavePage,
  deleteTestInstance,
  submitAnswer,
};

export default withRouterHooks(
  connect(mapStateToProps, mapDispatchToProps)(Evaluation)
);
