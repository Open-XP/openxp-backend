import {
  RESET_STATE_ON_LEAVE_PAGE,
  PERSIST_STATE_ON_PAGE,
} from "../Actions/Types";

const managePersistenceMiddleware = (store) => (next) => (action) => {
  const result = next(action);

  if (action.type === PERSIST_STATE_ON_PAGE) {
    // Persist the state when a specific action is dispatched
    persistStore(store);
  }

  if (action.type === RESET_STATE_ON_LEAVE_PAGE) {
    // Reset the specific state when leaving a page
    store.dispatch({ type: RESET_SPECIFIC_STATE });
  }

  return result;
};

export default managePersistenceMiddleware;
