import React, { Component } from "react";
import ExamSetter from "./ExamSetter";

export default class MockExam extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isExamSetterVisible: false,
    };
  }

  showExamSetter = () => {
    this.setState({ isExamSetterVisible: true });
  };

  hideExamSetter = () => {
    this.setState({ isExamSetterVisible: false });
  };

  render() {
    const { isExamSetterVisible } = this.state;
    return (
      <div className="flex flex-wrap w-full h-full gap-5 max-w-[100rem] mx-auto justify-center py-4">
        {isExamSetterVisible && <ExamSetter onClose={this.hideExamSetter} />}
        <button
          className="w-[35rem] h-[21rem] 2xl:w-1/3 p-3 rounded-lg"
          style={{ border: "solid #2D9CDB" }}
          onClick={this.showExamSetter}
        >
          <div className="flex flex-col w-full gap-3 h-[20rem] justify-center items-center">
            <div>
              <img
                src={require("../../../../icons/waec-logo.png")}
                className="w-52 h-52"
                alt="WAEC Logo"
              />
            </div>
            <div className="font-bold text-2xl text-purple-primary w-[15rem] text-center">
              West African Exam Council
            </div>
          </div>
        </button>
        <button
          className="w-[35rem] h-[21rem] 2xl:w-1/3 p-3 rounded-lg"
          style={{ border: "solid #2D9CDB" }}
          onClick={this.showExamSetter}
        >
          <div className="flex flex-col w-full gap-3 h-[20rem] justify-center items-center">
            <div>
              <img
                src={require("../../../../icons/jamb_logo.png")}
                className="w-52 h-52"
                alt="JAMB Logo"
              />
            </div>
            <div className="font-bold text-2xl text-purple-primary w-[15rem] text-center">
              Joint Admissions & Matriculation Board
            </div>
          </div>
        </button>
        <button
          className="w-[35rem] h-[21rem] 2xl:w-1/3 p-3 rounded-lg"
          style={{ border: "solid #2D9CDB" }}
          onClick={this.showExamSetter}
        >
          <div className="flex flex-col w-full gap-3 h-[20rem] justify-center items-center">
            <div>
              <img
                src={require("../../../../icons/neco_logo.png")}
                className="w-57 h-52"
                alt="NECO Logo"
              />
            </div>
            <div className="font-bold text-2xl text-purple-primary w-[16rem] text-center">
              The National Examinations Council
            </div>
          </div>
        </button>
        <button
          className="w-[35rem] h-[21rem] 2xl:w-1/3 p-3 rounded-lg"
          style={{ border: "solid #2D9CDB" }}
          onClick={this.showExamSetter}
        >
          <div className="w-full h-[20rem]">
            <div>General Certificate of Education</div>
          </div>
        </button>
      </div>
    );
  }
}
