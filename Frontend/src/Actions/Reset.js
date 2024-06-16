import { RESET_QUESTIONS_ON_LEAVE_PAGE } from "./Types";

// Action to reset the state on leaving the page
export const resetStateOnLeavePage = () => (dispatch) => {
  dispatch({
    type: RESET_QUESTIONS_ON_LEAVE_PAGE,
  });
};
