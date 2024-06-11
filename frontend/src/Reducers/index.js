import { combineReducers } from "redux";
import errors from "./Errors";
import messages from "./Messages";
import auth from "./Auth";
import user from "./User";
import quiz from "./Quiz";

export default combineReducers({
  errors,
  messages,
  auth,
  user,
  quiz,
});
