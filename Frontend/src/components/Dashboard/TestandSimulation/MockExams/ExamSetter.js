import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import { XMarkIcon, ChevronDownIcon } from "@heroicons/react/24/solid";
import { connect } from "react-redux";
import { fetchAllSubjects, startTest } from "../../../../Actions/Quiz";
import { withRouterHooks } from "../../../../withRouters/withRoutersHook";

class ExamSetter extends Component {
  static propTypes = {
    fetchAllSubjects: PropTypes.func.isRequired,
    subjects: PropTypes.array.isRequired,
    startTest: PropTypes.func.isRequired,
    testInstances: PropTypes.array.isRequired,
    // onClose: PropTypes.func.isRequired,
    navigate: PropTypes.func.isRequired,
  };

  constructor(props) {
    super(props);
    this.state = {
      subjectDropdownOpen: false,
      yearDropdownOpen: false,
      selectedSubject: null,
      selectedYear: null,
    };
  }

  componentDidMount() {
    this.props.fetchAllSubjects();
  }

  toggleSubjectDropdown = () => {
    this.setState((prevState) => ({
      subjectDropdownOpen: !prevState.subjectDropdownOpen,
    }));
  };

  toggleYearDropdown = () => {
    this.setState((prevState) => ({
      yearDropdownOpen: !prevState.yearDropdownOpen,
    }));
  };

  setSelectedSubject = (subject) => {
    this.setState({
      selectedSubject: subject,
      subjectDropdownOpen: false,
    });
  };

  setSelectedYear = (year) => {
    this.setState({
      selectedYear: year,
      yearDropdownOpen: false,
    });
  };

  handleStartTest = () => {
    const { selectedSubject, selectedYear } = this.state;
    if (selectedSubject && selectedYear) {
      this.props
        .startTest(1, selectedSubject.name, selectedYear)
        .then((data) => {
          // this.props.onClose();
          if (data !== undefined && data !== null) {
            this.props.navigate(`evaluation/${data.id}`);
          }

          console.log(
            "Test started with ID:",
            data.id,
            "Test duration is",
            data.duration
          );
        })
        .catch((error) => {
          console.error("Failed to start test:", error);
        });
    }
  };

  render() {
    const {
      subjectDropdownOpen,
      yearDropdownOpen,
      selectedSubject,
      selectedYear,
    } = this.state;
    const { subjects } = this.props;
    const isSelectionComplete = selectedSubject && selectedYear;

    return (
      <div className="flex w-screen h-screen fixed bg-gray-300 bg-opacity-50 drop-shadow-2xl backdrop-blur-sm justify-center -mt-[3.2rem]">
        <div className="flex w-[30rem] h-[40rem] 2xl:w-[46rem] 2xl:h-[35.938rem] flex-col justify-center bg-white items-center gap-4 mt-[6rem]">
          <div className="flex w-[80%] justify-between items-center">
            <div className="flex items-center text-[2rem] font-[600]">
              Pick Subject of Your Choice
            </div>
            <button
              onClick={this.props.onClose}
              className="w-[2.5rem] h-[2.5rem]"
            >
              <XMarkIcon />
            </button>
          </div>
          <div className="flex flex-col w-[80%] gap-2 relative">
            <div className="text-[1rem] font-[400]">Subject</div>
            <div
              className="flex items-center h-[2.938rem] px-3 cursor-pointer"
              style={{ backgroundColor: "rgba(60, 60, 60, 0.09)" }}
              onClick={this.toggleSubjectDropdown}
            >
              <div className="w-[97.5%]">
                {selectedSubject ? selectedSubject.name : "Select a subject"}
              </div>
              <ChevronDownIcon className="w-5 h-5" />
            </div>
            {subjectDropdownOpen && (
              <div className="absolute top-[4rem] left-0 w-full bg-white border border-gray-300 z-10">
                {subjects.map((subject) => (
                  <div
                    key={subject.name}
                    className="px-3 py-2 cursor-pointer hover:bg-gray-200"
                    onClick={() => this.setSelectedSubject(subject)}
                  >
                    {subject.name}
                  </div>
                ))}
              </div>
            )}
          </div>
          {selectedSubject && (
            <div className="flex flex-col w-[80%] gap-2 relative">
              <div className="text-[1rem] font-[400]">Past Question Year</div>
              <div
                className="flex items-center h-[2.938rem] px-3 cursor-pointer"
                style={{ backgroundColor: "rgba(60, 60, 60, 0.09)" }}
                onClick={this.toggleYearDropdown}
              >
                <div className="w-[97.5%]">
                  {selectedYear || "Select a year"}
                </div>
                <ChevronDownIcon className="w-5 h-5" />
              </div>
              {yearDropdownOpen && (
                <div className="absolute top-[4rem] left-0 w-full bg-white border border-gray-300 z-10">
                  {selectedSubject.years.map((yearObj) => (
                    <div
                      key={yearObj.year}
                      className="px-3 py-2 cursor-pointer hover:bg-gray-200"
                      onClick={() => this.setSelectedYear(yearObj.year)}
                    >
                      {yearObj.year}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
          {isSelectionComplete && (
            <div className="w-[80%]" style={{ color: "red" }}>
              Are you sure you picked the right subject and year? Look over it
              carefully.
            </div>
          )}
          <Link className="flex items-center justify-center w-[80%] h-[4.813rem] text-center text-[2rem] font-[600] text-white bg-purple-primary no-underline">
            <button onClick={this.handleStartTest}>Start Test</button>
          </Link>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  subjects: state.quiz.subjects,
  startTest: state.quiz.startTest,
  testInstances: state.quiz.testInstances,
});

const mapDispatchToProps = {
  startTest,
  fetchAllSubjects,
};

export default withRouterHooks(
  connect(mapStateToProps, mapDispatchToProps)(ExamSetter)
);
