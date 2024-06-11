import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import { logout } from "../../../Actions/Auth";
import { withRouterHooks } from "../../../withRouters/withRoutersHook";
import {
  List,
  ListItem,
  ListItemPrefix,
  Accordion,
  AccordionHeader,
  AccordionBody,
} from "@material-tailwind/react";
import {
  PresentationChartBarIcon,
  ChevronDownIcon,
  LockClosedIcon,
  ChartBarIcon,
  CircleStackIcon,
  CubeTransparentIcon,
  AtSymbolIcon,
  SwatchIcon,
  PuzzlePieceIcon,
  PowerIcon,
} from "@heroicons/react/24/solid";
import { connect } from "react-redux";

class SideBar extends Component {
  state = {
    activeIndex: null,
  };

  static propTypes = {
    logout: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool,
    navigate: PropTypes.func.isRequired,
  };

  handleLogout = () => {
    this.props.logout();
  };

  handleToggle = (index, title) => {
    if (title === "Logout") {
      this.handleLogout();
    } else {
      this.setState((prevState) => ({
        activeIndex: prevState.activeIndex === index ? null : index,
      }));
    }
  };

  accordionData = [
    {
      id: 1,
      title: "Dashboard",
      Icon: PresentationChartBarIcon,
      Arrow: "none",
      link: "/dashboard",
    },
    {
      id: 2,
      title: "Test and Simulation",
      subtitle: [
        { name: "Mock Test", link: "/dashboard/mock-exam" },
        { name: "Exam Drill", link: "/exam-drill" },
      ],
      Icon: CubeTransparentIcon,
      Arrow: ChevronDownIcon,
      rotate: true,
    },
    {
      id: 3,
      title: "Exam Catalog",
      Icon: CircleStackIcon,
      Arrow: LockClosedIcon,
      rotate: false,
    },
    {
      id: 4,
      title: "Performance Analytics",
      Icon: ChartBarIcon,
      Arrow: LockClosedIcon,
      rotate: false,
    },
    {
      id: 5,
      title: "Resources",
      Icon: SwatchIcon,
      Arrow: LockClosedIcon,
      rotate: false,
    },
    {
      id: 6,
      title: "Study Planner",
      Icon: PuzzlePieceIcon,
      Arrow: LockClosedIcon,
      rotate: false,
    },
    {
      id: 7,
      title: "Community",
      Icon: AtSymbolIcon,
      Arrow: LockClosedIcon,
      rotate: false,
    },
    {
      id: 8,
      title: "Logout",
      Icon: PowerIcon,
      Arrow: "none",
      rotate: false,
    },
  ];

  render() {
    const { activeIndex } = this.state;

    return (
      <div className="fixed top-32 h-screen w-full max-w-[30rem] p-4 shadow-xl bg-white">
        {this.accordionData.map(
          ({ id, title, subtitle, Icon, Arrow, rotate, link }) => (
            <List key={id}>
              <Accordion open={activeIndex === id}>
                <ListItem className="flex flex-col">
                  <AccordionHeader
                    onClick={() => this.handleToggle(id, title)}
                    className="border-b-0 p-3 flex justify-between items-center w-full"
                  >
                    <div className="flex items-center gap-2">
                      <div
                        className={`h-10 w-2 bg-blue-500 transition-all duration-300 ${
                          activeIndex === id && title !== "Logout"
                            ? "visible"
                            : "hidden"
                        }`}
                      ></div>
                      {link ? (
                        <Link
                          to={link}
                          className="flex items-center gap-2 no-underline text-black"
                        >
                          <ListItemPrefix>
                            <Icon className="h-5 w-5" />
                          </ListItemPrefix>
                          <span className="font-bold text-lg">{title}</span>
                        </Link>
                      ) : (
                        <>
                          <ListItemPrefix>
                            <Icon className="h-5 w-5" />
                          </ListItemPrefix>
                          <span className="font-bold text-lg">{title}</span>
                        </>
                      )}
                    </div>
                    {Arrow !== "none" && (
                      <Arrow
                        strokeWidth={2.5}
                        className={`h-4 w-4 transition-transform ${
                          activeIndex === id && rotate ? "rotate-180" : ""
                        }`}
                        style={{ marginLeft: "auto" }}
                      />
                    )}
                  </AccordionHeader>
                </ListItem>
                {subtitle && (
                  <AccordionBody className="flex flex-col items-start ml-[5rem] p-0">
                    <List>
                      {subtitle.map((sub, index) => (
                        <ListItem key={index}>
                          <Link
                            to={sub.link}
                            className="text-xl no-underline text-black"
                          >
                            {sub.name}
                          </Link>
                        </ListItem>
                      ))}
                    </List>
                  </AccordionBody>
                )}
              </Accordion>
            </List>
          )
        )}
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth?.isAuthenticated,
  error: state.error,
  logout: state.auth.isAuthenticated,
});

const mapDispatchToProps = {
  logout,
};

export default withRouterHooks(
  connect(mapStateToProps, mapDispatchToProps)(SideBar)
);
