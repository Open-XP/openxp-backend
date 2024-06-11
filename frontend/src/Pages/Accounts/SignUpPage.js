import React, { useState, Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { withRouterHooks } from "../../withRouters/withRoutersHook";
import PropTypes from "prop-types";
import { registers } from "../../Actions/Auth";
import { createMessage } from "../../Actions/Messages";
import HideIcon from "../../icons/hide.png";
import ViewIcon from "../../icons/view.png";

export class SignUpPage extends Component {
  state = {
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
    confirm_password: "",
  };

  static propTypes = {
    registers: PropTypes.func.isRequired,
    createMessage: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool,
  };

  onSubmit = (e) => {
    e.preventDefault();
    const {
      first_name,
      last_name,
      username,
      email,
      password,
      confirm_password,
    } = this.state;
    this.props.registers(
      first_name,
      last_name,
      username,
      email,
      password,
      confirm_password
    );
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  toggleShowPassword = () => {
    this.setState((prevState) => ({
      showPassword: !prevState.showPassword,
    }));
  };

  render() {
    if (this.props.isAuthenticated) {
      this.props.navigate("/dashboard");
    }
    const {
      first_name,
      last_name,
      username,
      email,
      password,
      confirm_password,
      showPassword,
    } = this.state;

    return (
      <div className="flex w-full h-full justify-center ">
        <div className="flex flex-col w-[90rem] h-screen items-center gap-[4rem] justify-center">
          <div className="flex flex-col w-[31.5rem] h-[6.313rem] items-center gap-[0.8rem]">
            <div className="font-[700] text-[2.5rem] font-sans leading-[3.404rem]">
              Sign Up
            </div>
            <div className="font-[500] text-[1.5rem] leading-[2.043rem]">
              have an account?{" "}
              <Link to={"/login"} className="text-skyblue-secondary">
                Log in
              </Link>
            </div>
          </div>
          <div className="flex flex-col w-[74.75rem] h-[65.125rem] items-center pt-[5rem] gap-[0.938rem] shadow-custom2">
            <div className="flex w-[66.688rem] justify-around">
              <button className="flex font-[600] text-[1.5rem] leading-[2.043rem] font-sans w-[12.063rem] h-[4.125rem] items-center justify-center shadow-custom2 gap-[1rem]">
                <img
                  className="w-[1.375rem] h-[1.375rem]"
                  src={require("../../icons/google.png")}
                />
                <div>Google</div>
              </button>
              <button className="flex font-[600] text-[1.5rem] leading-[2.043rem] font-sans w-[12.063rem] h-[4.125rem] items-center justify-center shadow-custom2 gap-[1rem]">
                <img
                  className="w-[1.375rem] h-[1.375rem]"
                  src={require("../../icons/linkedin.png")}
                />
                <div>LinkedIn</div>
              </button>
              <button className="flex font-[600] text-[1.5rem] leading-[2.043rem] font-sans w-[12.063rem] h-[4.125rem] items-center justify-center shadow-custom2 gap-[1rem]">
                <img
                  className="w-[1.375rem] h-[1.375rem]"
                  src={require("../../icons/facebook.png")}
                />
                <div>Facebook</div>
              </button>
            </div>
            <div className="flex items-center gap-4">
              <div className="w-[31.875rem] h-[1px] bg-[#3C3C3C45]"></div>
              <div className="font-[600] text-[1.5rem] leading-[2.043rem]">
                OR
              </div>
              <div className="w-[31.875rem] h-[1px] bg-[#3C3C3C45]"></div>
            </div>
            <form onSubmit={this.onSubmit}>
              <div className="flex flex-col w-[65.688rem] h-[23.438rem] gap-[0.938rem]">
                <div className="flex flex-col gap-[0.625rem]">
                  <div className="flex justify-between">
                    <div className="pl-[0.5rem] font-[700] text-[1.5rem] leading-[2.043rem]">
                      First Name
                      <span className="text-red-700 items-center"> *</span>
                    </div>
                    <div className="flex gap-[0.938rem] items-center pr-[1rem]">
                      <div className="font-[500] text-[1.5rem] leading-[2.043rem] ">
                        Show Password
                      </div>
                      <button
                        className="flex w-[1.938rem] h-[1.356rem] items-center"
                        type="button"
                        onClick={this.toggleShowPassword}
                      >
                        {" "}
                        {showPassword ? (
                          <img className="" src={HideIcon} alt="Hide" />
                        ) : (
                          <img className="" src={ViewIcon} alt="View" />
                        )}
                      </button>
                    </div>
                  </div>
                  <input
                    type="text"
                    name="first_name"
                    value={first_name}
                    onChange={this.onChange}
                    autoComplete="off"
                    placeholder="John"
                    className="w-full h-[3.125rem] border-none bg-[#E9F0FA] rounded-[0.625rem] pl-[1.25rem] text-[1.5rem] font-[600] font-sans flex items-center"
                  />
                </div>
                <div className="flex flex-col gap-[0.625rem]">
                  <div className="flex justify-between">
                    <div className="pl-[0.5rem] font-[700] text-[1.5rem] leading-[2.043rem]">
                      Last Name
                      <span className="text-red-700 items-center"> *</span>
                    </div>
                  </div>
                  <input
                    type="text"
                    name="last_name"
                    value={last_name}
                    onChange={this.onChange}
                    autoComplete="off"
                    placeholder="Doe"
                    className="w-full h-[3.125rem] border-none bg-[#E9F0FA] rounded-[0.625rem] pl-[1.25rem] text-[1.5rem] font-[600] font-sans flex items-center"
                  />
                </div>
                <div className="flex flex-col gap-[0.625rem]">
                  <div className="flex justify-between">
                    <div className="pl-[0.5rem] font-[700] text-[1.5rem] leading-[2.043rem]">
                      User Name
                      <span className="text-red-700 items-center"> *</span>
                    </div>
                  </div>
                  <input
                    type="text"
                    name="username"
                    value={username}
                    onChange={this.onChange}
                    autoComplete="off"
                    placeholder="Johndoe"
                    className="w-full h-[3.125rem] border-none bg-[#E9F0FA] rounded-[0.625rem] pl-[1.25rem] text-[1.5rem] font-[600] font-sans flex items-center"
                  />
                </div>
                <div className="flex flex-col gap-[0.625rem]">
                  <div className="flex justify-between">
                    <div className="pl-[0.5rem] font-[700] text-[1.5rem] leading-[2.043rem]">
                      Email
                      <span className="text-red-700 items-center"> *</span>
                    </div>
                  </div>
                  <input
                    type="text"
                    name="email"
                    value={email}
                    onChange={this.onChange}
                    autoComplete="off"
                    placeholder="johndoe@gmail.com"
                    className="w-full h-[3.125rem] border-none bg-[#E9F0FA] rounded-[0.625rem] pl-[1.25rem] text-[1.5rem] font-[600] font-sans flex items-center"
                  />
                </div>
                <div className="flex flex-col gap-[0.625rem]">
                  <div className="pl-[0.5rem] font-[700] text-[1.5rem] leading-[2.043rem]">
                    <div>
                      Password
                      <span className="text-red-700 items-center"> *</span>
                    </div>
                  </div>
                  <input
                    type={showPassword ? "text" : "password"}
                    name="password"
                    value={password}
                    onChange={this.onChange}
                    autoComplete="off"
                    placeholder="Password"
                    className="w-full h-[3.125rem] border-none bg-[#E9F0FA] rounded-[0.625rem] pl-[1.25rem] text-[1.5rem] font-[600] font-sans flex items-center"
                  />
                </div>
                <div className="flex flex-col gap-[0.625rem]">
                  <div className="pl-[0.5rem] font-[700] text-[1.5rem] leading-[2.043rem]">
                    <div>
                      Confirm Password
                      <span className="text-red-700 items-center"> *</span>
                    </div>
                  </div>
                  <input
                    type={showPassword ? "text" : "password"}
                    name="confirm_password"
                    value={confirm_password}
                    onChange={this.onChange}
                    autoComplete="off"
                    placeholder="Password"
                    className="w-full h-[3.125rem] border-none bg-[#E9F0FA] rounded-[0.625rem] pl-[1.25rem] text-[1.5rem] font-[600] font-sans flex items-center"
                  />
                </div>
                <div className="flex flex-col gap-[1.625rem]">
                  <button
                    onSubmit={this.onSubmit}
                    className="w-[9.438rem] h-[3.438rem] font-sans font-[700] text-[1.438rem] leading-[2.043rem] bg-[#D9D9D952] bg-opacity-32 rounded-xl"
                  >
                    Sign Up
                  </button>
                </div>
                <div className="font-[400] text-[1.25rem]">
                  By Continuing, You agree to Openxp{" "}
                  <span className="font-[400] text-[1.25rem] text-skyblue-secondary">
                    Terms
                  </span>{" "}
                  of service and{" "}
                  <span className="font-[400] text-[1.25rem] text-skyblue-secondary">
                    Privacy Policy
                  </span>{" "}
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth?.isAuthenticated,
});

export default withRouterHooks(
  connect(mapStateToProps, { registers })(SignUpPage)
);
