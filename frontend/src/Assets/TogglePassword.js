// PasswordInput.js
import HideIcon from "../icons/hide.png";
import ViewIcon from "../icons/view.png";
import React, { useState } from "react";

const PasswordInput = ({ value, onChange }) => {
  const [showPassword, setShowPassword] = useState(false);

  const toggleShowPassword = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className="">
      <label htmlFor="password">Password:</label>
      <input className=""
        type={showPassword ? "text" : "password"}
        id="password"
        name="password"
        value={value}
        onChange={onChange}
        required
      />
      <button
        className=""
        type="button" // Prevent form submission
        onClick={toggleShowPassword}
      >
        {" "}
        {showPassword ? (
          <img
            className=""
            src={HideIcon}
            alt="Hide"
          />
        ) : (
          <img
            className=""
            src={ViewIcon}
            alt="View"
          />
        )}
      </button>
    </div>
  );
};

export default PasswordInput;
