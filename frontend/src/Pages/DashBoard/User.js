import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getUser } from "../../Actions/User";
import { logout } from "../../Actions/Auth";

function greeting() {
  var hours = new Date().getHours();
  var greeting = "";

  if (hours >= 0 && hours < 12) {
    greeting = "Good Morning";
  } else if (hours >= 12 && hours < 18) {
    greeting = "Good Afternoon";
  } else if (hours >= 18 && hours <= 23) {
    greeting = "Good Evening";
  }
  return greeting;
}

export class User extends Component {
  static propTypes = {
    user: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired,
    getUser: PropTypes.func.isRequired,
  };

  onClick = (e) => {
    e.preventDefault();
    this.props.logout();
  };

  componentDidMount() {
    this.props.getUser();
  }

  render() {
    const { user } = this.props;
    return (
      <Fragment>
        <h1>
          {greeting()} {user ? user.username : "Guest"}
        </h1>
        <button onClick={this.onClick}>Logout</button>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  user: state.user.user,
});

export default connect(mapStateToProps, { getUser, logout })(User);
