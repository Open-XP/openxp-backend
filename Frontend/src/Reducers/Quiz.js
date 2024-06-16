//Reducers.js
import {
  USER_LOADING,
  START_TEST_SUCCESS,
  START_TEST_FAIL,
  SUBMIT_ANSWER_SUCCESS,
  SUBMIT_ANSWER_FAIL,
  COMPLETE_TEST_SUCCESS,
  COMPLETE_TEST_FAIL,
  FETCH_COMPLETED_TESTS_SUCCESS,
  FETCH_COMPLETED_TESTS_FAIL,
  FETCH_ALL_TEST_INSTANCES_SUCCESS,
  FETCH_ALL_TEST_INSTANCES_FAIL,
  RETRIEVE_INDIVIDUAL_QUESTION_SUCCESS,
  RETRIEVE_INDIVIDUAL_QUESTION_FAIL,
  FETCH_USER_SCORE_SUCCESS,
  FETCH_USER_SCORE_FAIL,
  FETCH_TEST_RESULTS_SUCCESS,
  FETCH_TEST_RESULTS_FAIL,
  FETCH_TOTAL_STUDY_TIME_SUCCESS,
  FETCH_TOTAL_STUDY_TIME_FAIL,
  FETCH_ALL_SUBJECTS_FAIL,
  FETCH_ALL_SUBJECTS_SUCCESS,
  FETCH_SUBJECT_QUESTIONS_SUCCESS,
  FETCH_SUBJECT_QUESTIONS_FAIL,
  FETCH_INDIVIDUAL_SUBJECT_QUESTION_SUCCESS,
  FETCH_INDIVIDUAL_SUBJECT_QUESTION_FAIL,
  RESET_QUESTIONS_ON_LEAVE_PAGE,
} from "../Actions/Types";

const initialState = {
  testInstances: {},
  completedTests: [],
  allTests: null,
  individualQuestion: {},
  userScores: {},
  totalStudyTime: null,
  subjects: [],
  subjectQuestions: [],
  loading: false,
  error: null,
};

export default function (state = initialState, action) {
  switch (action.type) {
    case USER_LOADING:
      return {
        ...state,
        loading: true,
      };
    case START_TEST_SUCCESS:
      return {
        ...state,
        testInstances: { id: action.payload.id, ...action.payload },
        loading: false,
      };
    case START_TEST_FAIL:
    case SUBMIT_ANSWER_FAIL:
    case COMPLETE_TEST_FAIL:
    case FETCH_COMPLETED_TESTS_FAIL:
    case FETCH_ALL_TEST_INSTANCES_FAIL:
    case RETRIEVE_INDIVIDUAL_QUESTION_FAIL:
    case FETCH_USER_SCORE_FAIL:
    case FETCH_TEST_RESULTS_FAIL:
    case FETCH_TOTAL_STUDY_TIME_FAIL:
    case FETCH_ALL_SUBJECTS_FAIL:
    case FETCH_SUBJECT_QUESTIONS_FAIL:
    case FETCH_INDIVIDUAL_SUBJECT_QUESTION_FAIL:
      return {
        ...state,
        error: action.payload,
        loading: false,
      };
    case SUBMIT_ANSWER_SUCCESS:
      return {
        ...state,
        answer: action.payload,
        error: null,
      };
    case COMPLETE_TEST_SUCCESS:
      return {
        ...state,
        testInstance: action.payload,
        error: null,
      };
    case FETCH_COMPLETED_TESTS_SUCCESS:
      return {
        ...state,
        completedTests: action.payload,
        loading: false,
      };
    case FETCH_ALL_TEST_INSTANCES_SUCCESS:
      return {
        ...state,
        allTests: action.payload,
        loading: false,
      };
    case FETCH_INDIVIDUAL_SUBJECT_QUESTION_SUCCESS:
      return {
        ...state,
        individualQuestion: {
          id: action.payload.id,
          question: action.payload.question,
          image: action.payload.image,
          option_A: action.payload.option_A,
          option_B: action.payload.option_B,
          option_C: action.payload.option_C,
          option_D: action.payload.option_D,
          option_E: action.payload.option_E,
        },
        loading: false,
      };
    case FETCH_USER_SCORE_SUCCESS:
      return {
        ...state,
        userScores: action.payload,
        loading: false,
      };
    case FETCH_TOTAL_STUDY_TIME_SUCCESS:
      return {
        ...state,
        totalStudyTime: action.payload,
        loading: false,
      };
    case FETCH_ALL_SUBJECTS_SUCCESS:
      return {
        ...state,
        subjects: action.payload,
        loading: false,
      };
    case FETCH_SUBJECT_QUESTIONS_SUCCESS:
      return {
        ...state,
        subjectQuestions: action.payload,
        loading: false,
      };
    case RESET_QUESTIONS_ON_LEAVE_PAGE:
      return {
        ...state,
        subjectQuestions: [],
      };
    default:
      return state;
  }
}
