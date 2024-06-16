import React, { useState, Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { withRouterHooks } from "../../withRouters/withRoutersHook";
import PropTypes from "prop-types";
import { login } from "../../Actions/Auth";
import HideIcon from "../../icons/hide.png";
import ViewIcon from "../../icons/view.png";

export class LogInPage extends Component {
  state = {
    email: "",
    password: "",
  };

  static propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool,
    login: PropTypes.func.isRequired,
  };

  onSubmit = (e) => {
    e.preventDefault();
    this.props.login(this.state.email, this.state.password);
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
    const { email, password, showPassword } = this.state;
    return (
      <div className="flex w-full h-screen justify-center items-center">
        <div className="flex flex-col w-[90rem] h-[70.063rem] justify-center items-center gap-[4rem]">
          <div className="flex flex-col w-[31.5rem] h-[6.313rem] items-center  gap-[0.8rem]">
            <div className="font-[700] text-[2.5rem] font-sans leading-[3.404rem]">
              Login
            </div>
            <div className="font-[500] text-[1.5rem] leading-[2.043rem]">
              Do not have an account?{" "}
              <Link to={"/signup"} className="text-skyblue-secondary">
                Create an account
              </Link>
            </div>
          </div>
          <div className="flex flex-col w-[74.75rem] h-[47.125rem] items-center justify-center gap-[0.938rem] shadow-custom2">
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
                      Email<span className="text-red-700 items-center"> *</span>
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
                    name="email"
                    value={email}
                    onChange={this.onChange}
                    placeholder="Email Address"
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
                    placeholder="Password"
                    className="w-full h-[3.125rem] border-none bg-[#E9F0FA] rounded-[0.625rem] pl-[1.25rem] text-[1.5rem] font-[600] font-sans flex items-center"
                  />
                </div>
                <div className="flex flex-col gap-[1.625rem]">
                  <div className="flex flex-row justify-between">
                    <div className="font-[500] text-[1.25rem] leading-[1.703rem] flex flex-row h-[1.688rem] gap-[1.313rem] items-center">
                      <input
                        className=" font-sans bg-[#D9D9D952] bg-opacity-32 border-none w-[1.25rem] h-[1.25rem]"
                        type="checkbox"
                      />
                      Remember me
                    </div>
                    <Link
                      to="/reset-password"
                      className="font-[500] text-[1.25rem] leading-[1.703rem] pr-[1rem] text-skyblue-secondary"
                    >
                      Forgot Password?
                    </Link>
                  </div>
                  <button
                    onSubmit={this.onSubmit}
                    className="w-[9.438rem] h-[3.438rem] font-sans font-[700] text-[1.438rem] leading-[2.043rem] bg-[#D9D9D952] bg-opacity-32 rounded-xl"
                  >
                    Login
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

export default withRouterHooks(connect(mapStateToProps, { login })(LogInPage));
