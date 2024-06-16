import axios from "axios";
import { createMessage, returnErrors } from "./Messages";
import { tokenConfig } from "./Auth";

import { GET_USER } from "./Types";

// GET LEADS
export const getUser = () => (dispatch, getState) => {
  axios
    .get("http://127.0.0.1:8000/api/auth/user/me", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_USER,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
