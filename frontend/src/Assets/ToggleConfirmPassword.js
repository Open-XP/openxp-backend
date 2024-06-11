import HideIcon from "../assets/icons/hide.png";
import ViewIcon from "../assets/icons/view.png";
import React, { useState } from "react";

const TogglePasswordInput = ({
  password,
  confirmPassword,
  onPasswordChange,
  onConfirmPasswordChange,
}) => {
  const [showPassword, setShowPassword] = useState(false);

  const toggleShowPassword = () => setShowPassword(!showPassword);

  return (
    <div className="input-group password-input-group">
      <label htmlFor="password">Password:</label>
      <input
        type={showPassword ? "text" : "password"}
        id="password"
        name="password"
        value={password}
        onChange={onPasswordChange}
        required
      />
      <button
        className="show-password-button"
        type="button"
        onClick={toggleShowPassword}
      >
        {showPassword ? (
          <img
            className="show-password-button-click-2"
            src={HideIcon}
            alt="Hide"
          />
        ) : (
          <img
            className="show-password-button-click-2"
            src={ViewIcon}
            alt="View"
          />
        )}
      </button>
      <label htmlFor="confirm_password">Confirm Password:</label>
      <input
        type={showPassword ? "text" : "password"}
        id="confirm_password"
        name="confirm_password"
        value={confirmPassword}
        onChange={onConfirmPasswordChange}
        required
      />
    </div>
  );
};

export default TogglePasswordInput;
