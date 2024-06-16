import React, { Component } from "react";
import Checkmark from "../../../../icons/checkmark.png";
import Cancelmark from "../../../../icons/cancelmark.png";
import PropTypes from "prop-types";
import { fetchUserScore } from "../../../../Actions/Quiz";
import { withRouterHooks } from "../../../../withRouters/withRoutersHook";
import { connect } from "react-redux";

class SummaryPage extends Component {
  static propTypes = {
    testInstances: PropTypes.object.isRequired,
    navigate: PropTypes.func.isRequired,
    fetchUserScore: PropTypes.func.isRequired,
    userScores: PropTypes.object.isRequired,
  };

  state = {
    visibility: [],
    loading: true,
  };

  componentDidMount() {
    const { fetchUserScore, testInstances, userScores } = this.props;
    if (this.props.testInstances) {
      fetchUserScore(testInstances.id && userScores);
      this.setState({ loading: false });
    }
  }

  toggleVisibility = (index) => {
    this.setState((prevState) => {
      const newVisibility = [...prevState.visibility];
      newVisibility[index] = !newVisibility[index];
      return { visibility: newVisibility };
    });
  };

  renderSection = (index, question, answer) => {
    const { visibility } = this.state;
    return (
      <div key={index} className="mb-4">
        <div className="font-[600] text-[1.5rem] font-sans leading-[2.043rem] w-[36.438rem] h-fit">
          {question}
        </div>
        <div className={visibility[index] ? "" : "hidden"}>{answer}</div>
        <button
          onClick={() => this.toggleVisibility(index)}
          className="text-blue-500"
        >
          {visibility[index] ? "Show less" : "Show more"}
        </button>
      </div>
    );
  };

  render() {
    if (this.state.loading) {
      return <div>Loading...</div>;
    }
    const { userScores } = this.props;

    // Prepare sections from incorrect questions
    const sections =
      userScores.incorrect_questions?.map((item, index) => {
        const correctOptionKey = `option_${item.answer}`;
        return {
          question: item.question,
          answer: `Correct answer: ${item[correctOptionKey]} (${item.answer})`,
        };
      }) || [];

    return (
      <div className="flex w-screen h-screen">
        <div className="fixed flex flex-col w-[35%] bg-purple-primary h-full text-white justify-center items-center gap-5">
          <div className="flex flex-col w-[20.375rem] h-[26.563rem] items-center justify-between">
            <div className="font-[700] text-[2.5rem] leading-[8.171rem] font-sans">
              Your Total Score
            </div>
            <div className="flex w-[19.75rem] h-[19.75rem] rounded-[50%] justify-center items-center border-white border-[9px]">
              <div>
                <div className="font-[700] text-[6rem] text-center leading-[8.171rem]">
                  {userScores.score}
                </div>
                <div className="font-[600] text-[2.5rem] leading-[3.404rem]">
                  OF {userScores.total_questions}
                </div>
              </div>
            </div>
          </div>
          <div className="font-[500] text-[1.5rem] w-[23.625rem] text-center lead-[2.043rem]">
            Average, Try again to understand concepts
          </div>
        </div>
        <div className="flex w-full h-full justify-end">
          <div className="w-[65%] h-screen">
            <div className="mt-[7.5rem] ml-[3.75rem]">
              <div className="font-[700] text-[2rem] font-sans leading-[2.724rem]">
                Summary
              </div>
              <div className="flex flex-row gap-[0.688rem]">
                <img
                  src={Checkmark}
                  className="w-[3rem] h-[3rem] p-2"
                  alt="check mark"
                />
                <div className="flex flex-col font-[600] text-[1rem] gap-[0.625rem] leading-[1.362rem]">
                  <div>
                    Total Number of Incorrect questions answered:{" "}
                    {userScores.correct_questions?.length}
                  </div>
                  <div>View all</div>
                </div>
              </div>

              <div className="flex gap-[0.688rem] ">
                <img
                  src={Cancelmark}
                  className="w-[3rem] h-[3rem] p-2"
                  alt="cancel mark"
                />
                <div className="flex flex-col font-[600] text-[1rem] gap-[0.625rem] leading-[1.362rem]">
                  <div>
                    Total Number of Correct questions answered:{" "}
                    {userScores.incorrect_questions?.length}
                  </div>
                  <div>View all</div>
                </div>
              </div>
              <div>
                <div>Corrections</div>
                {sections.map((section, index) =>
                  this.renderSection(index, section.question, section.answer)
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  testInstances: state.quiz.testInstances,
  userScores: state.quiz.userScores,
});

const mapDispatchToProps = {
  fetchUserScore,
};

export default withRouterHooks(
  connect(mapStateToProps, mapDispatchToProps)(SummaryPage)
);
