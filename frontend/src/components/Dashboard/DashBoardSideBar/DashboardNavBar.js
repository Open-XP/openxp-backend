import React from "react";
import { BellIcon, MoonIcon, UserCircleIcon } from "@heroicons/react/24/solid";
import OpenxpSVG from "../../../svgs/openxp.js";
import { createAvatar } from "@dicebear/core";
import { adventurer } from "@dicebear/collection";

export function DashboardNavBar() {
  const avatar = createAvatar(adventurer, {
    seed: "custom-seed", // Custom seed
    dataUri: true,
  });
  const svg = avatar.jpeg();
  return (
    <div className="flex fixed w-full py-4 px-4 justify-between items-center shadow-xl shadow-blue-gray-900/5 font-semibold bg-white z-20">
      <div className="flex ml-10 gap-2">
        <OpenxpSVG className="w-16 h-16 m-auto" />
        <div className=" text-3xl py-4">openxp</div>
      </div>

      <input
        placeholder="What do you want to learn"
        className="w-1/4 h-16 pl-8 rounded-3xl bg-purple-900 placeholder-white text-white text-lg outline-none"
      ></input>
      <div className="flex gap-8">
        <div className="w-16 h-16" style={{ transform: "rotate(15deg)" }}>
          <MoonIcon />
        </div>

        <div className="flex h-16 w-20">
          <BellIcon />
          <div className="w-6 h-6 bg-blue-600 absolute ml-8 rounded-full text-white text-center">
            3
          </div>
        </div>
        <div className="w-16 h-16">
          <UserCircleIcon />
        </div>
      </div>
      <button className="w-56 p-4 text-center font-semibold text-2xl text-white rounded-full bg-green-600">
        Start Drill
      </button>
    </div>
  );
}

export default DashboardNavBar;
