import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import OpenxpSVG from "../../../svgs/openxp.js";
import {
  MagnifyingGlassIcon,
  ChevronDownIcon,
} from "@heroicons/react/20/solid";
import {
  Fragment,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  Transition,
} from "@headlessui/react";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

const menuDetails = [
  {
    label: "Courses",
    items: [
      "Mathematics",
      "Physics",
      "Chemistry",
      "Biology",
      "Computer Science",
      "Agricultural Science",
      "Economics",
      "Accounting",
      "Geography",
      "History",
      "Government",
      "Literature",
      "English Language",
    ],
  },
  {
    label: "Resources",
    items: [
      "Textbooks and eBooks",
      "Past Examination Papers",
      "Study Guides and Notes",
      "Tutorial Videos",
      "Interactive Quizzes and Flashcards",
      "Assignment and Homework Help",
      "Reference Materials",
      "Career Guidance Resources",
    ],
  },
];

const DropdownMenu = ({ label, items }) => (
  <Menu as="div" className="relative">
    <MenuButton className="flex no-underline text-white font-[400] text-[1.3rem] leading-[1.4rem] gap-2">
      {label}
      <ChevronDownIcon
        className="-mr-1 h-5 w-5 text-gray-400"
        aria-hidden="true"
      />
    </MenuButton>
    <Transition
      as="div"
      enter="transition ease-out duration-100"
      enterFrom="transform opacity-0 scale-95"
      enterTo="transform opacity-100 scale-100"
      leave="transition ease-in duration-75"
      leaveFrom="transform opacity-100 scale-100"
      leaveTo="transform opacity-0 scale-95"
    >
      <MenuItems className="absolute left-1/2 transform -translate-x-1/2 mt-2 w-56 origin-top divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
        <div className="py-1">
          {items.map((item) => (
            <MenuItem key={item}>
              {({ active }) => (
                <a
                  href="#"
                  className={classNames(
                    active ? "bg-gray-100 text-gray-900" : "text-gray-700",
                    "block px-4 py-2 text-md font-[500]"
                  )}
                >
                  {item}
                </a>
              )}
            </MenuItem>
          ))}
        </div>
      </MenuItems>
    </Transition>
  </Menu>
);

const Navbar = () => {
  return (
    <div className="flex fixed h-[6rem] w-full justify-center z-20 bg-purple-primary">
      <div className="flex w-[90rem] justify-between p-4 items-center">
        <div className="flex items-center gap-2">
          <OpenxpSVG className="w-10 h-10 text-white" />
          <div className="text-3xl py-4 text-white font-[700] font-sans z-10">
            openxp
          </div>
        </div>
        <div className="w-[23rem] h-[3.25rem] items-center flex">
          <MagnifyingGlassIcon className="w-10 h-6 text-white absolute pl-3" />
          <input
            className="w-full h-full pl-12 rounded-3xl bg-[#FFFFFF33]/25 border-none text-white text-lg outline-none placeholder-white"
            type="text"
            placeholder="What do you want to learn?"
          />
        </div>
        <div className="flex w-[40rem] justify-center">
          <div className="flex flex-row w-full gap-3 justify-around items-center px-3">
            {menuDetails.map((menu) => (
              <DropdownMenu
                key={menu.label}
                label={menu.label}
                items={menu.items}
              />
            ))}
            <Link
              to="/about-us"
              className="no-underline text-[1.3rem] leading-[1.4rem] text-white"
            >
              About Us
            </Link>
            <div className="h-14 w-[1px] bg-white font-[400]"></div>
            <Link
              to="/dashboard"
              className="no-underline text-[1.3rem] leading-[1.4rem] text-white"
            >
              LogIn
            </Link>
            <div className="flex justify-center items-center w-[8rem] h-[3rem] rounded-lg border border-white">
              <Link
                to="/signup"
                className="no-underline text-white text-[1.5rem] items-center"
              >
                Start Free
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
