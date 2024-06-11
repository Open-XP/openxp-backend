import React from "react";
import { useNavigate, useParams, useLocation } from "react-router-dom";

export function withRouterHooks(Component) {
  return (props) => {
    let navigate = useNavigate();
    let params = useParams();
    let location = useLocation();

    return (
      <Component
        {...props}
        navigate={navigate}
        params={params}
        location={location}
      />
    );
  };
}
