import React from "react";
import { ReactComponent as Students } from "../../../svgs/study-group-african-people.svg";
import { ArrowLongRightIcon } from "@heroicons/react/24/solid";

/**
 * Renders the CommunitySection component.
 * This component displays information about a global exam preparation community.
 * It includes a description, an image, and practical tools for exam success.
 *
 * @returns {JSX.Element} The rendered CommunitySection component.
 */
const CommunitySection = () => {
  return (
    <div className="flex w-full h-[80rem] 2xl:h-[42.75rem] justify-center ">
      <div className="flex flex-col 2xl:flex-row w-[90rem] h-full  justify-center 2xl:h-[42.75rem] items-center gap-[3rem]  2xl:gap-0">
        <div className="flex flex-col w-1/2 h-[33.25rem] items-center gap-5 justify-center">
          <div className="font-[700] text-[1.75rem] leading-[2.383rem] w-[35.125rem] h-[4.75rem]">
            Beyond Exam Preparations: A Gateway to Guaranteed Exam Success{" "}
          </div>
          <div className="flex w-[34.375rem] h-[12.563rem] justify-center items-center gap-[1rem]">
            <img
              src={require("../../../icons/teamwork.png")}
              className="w-[1.438rem] h-[1.438rem] -mt-[7.2rem]"
            />
            <div className="flex flex-col w-[26.875rem] h-[8.813rem] gap-[0.5rem]">
              <div className="font-[700] text-[1.25rem]">
                Global Exam Preparation Community
              </div>
              <div className="font-[500] font-sans text-[0.938rem] leading-[1.277rem] h-[3.75rem]">
                Join a Top tutors and Students all over the world, and learn
                together in a beautiful Virtual community, tailored to allow you
                thrive
              </div>
              <div className="flex flex-row items-center text-[#2D9CDB] gap-2">
                <div className="font-[400] text-[1rem]">Read More</div>
                <ArrowLongRightIcon className="w-[2rem]" />
              </div>
            </div>
          </div>
          <div className="flex flex-col w-[35.125rem] gap-4">
            <div className="flex h-[3rem] shadow-custom">
              <div className="flex gap-3">
                <img
                  src={require("../../../icons/best-practice.png")}
                  className="h-[1.625rem] w-[1.625rem]"
                />
                <div className="w-[25rem] h-[1.625rem]">
                  Practical Tools to allow you ace your exams
                </div>
              </div>
            </div>
            <div className="flex h-[3rem] shadow-custom">
              <div className="flex gap-3">
                <img
                  src={require("../../../icons/best-practice.png")}
                  className="h-[1.625rem] w-[1.625rem]"
                />
                <div className="w-[25rem] h-[1.625rem]">
                  Practical Tools to allow you ace your exams
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="flex w-1/2 h-[33.25rem] justify-center">
          <Students className="w-[37.875rem] h-[33.25rem]" />
        </div>
      </div>
    </div>
  );
};

export default CommunitySection;
