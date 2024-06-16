import React from "react";

/**
 * CourseCard component displays a card with information about different courses.
 * It includes images, titles, and descriptions for each course category.
 *
 * @returns {JSX.Element} The CourseCard component.
 */
const CourseCard = () => {
  return (
    <div className="flex flex-col h-[100rem] 2xl:h-[58.313rem] justify-center items-center z-10 -mt-[9.5rem] gap-[4rem]">
      <img
        src={require("../../../icons/pexels-pixabay.png")}
        alt="Newsletter Background"
        className="absolute w-full h-[100rem] 2xl:h-[58.313rem] object-cover -z-10"
      />
      <div className="font-[700] text-[2.25rem] leading-[3.064rem] text-center text-white w-[63.125rem] h-[6.125rem]">
        Gear Towards Getting Your desired Result for <br /> Scholarship Exams
        Internationally and Locally.
      </div>
      <div className="flex flex-col 2xl:flex-row gap-[4rem] 2xl:gap-[2rem]">
        <div className="flex flex-col bg-white w-[23rem] h-[16.5rem] justify-center items-center rounded">
          <img
            src={require("../../../icons/technology.png")}
            className="w-[5.313rem] h-[5.313rem]"
          />
          <div className="font-[700] text-[2rem] leading-[2.724rem] font-sans w-[13.063rem] text-center">
            Science & Engineering
          </div>
        </div>
        <div className="flex flex-col bg-[#2D9CDB] w-[23rem] h-[16.5rem] justify-center items-center rounded-lg">
          <img
            src={require("../../../icons/paint-board-and-brush.png")}
            className="w-[5.313rem] h-[5.313rem]"
          />
          <div className="font-[700] text-[2rem] leading-[2.724rem] font-sans w-[13.063rem] text-center">
            Creative Art & Craft
          </div>
        </div>
        <div className="flex flex-col bg-white w-[23rem] h-[16.5rem] justify-center items-center rounded">
          <img
            src={require("../../../icons/briefcase.png")}
            className="w-[5.313rem] h-[5.313rem]"
          />
          <div className="font-[700] text-[2rem] leading-[2.724rem] font-sans w-[13.063rem] text-center">
            Business & Accounting
          </div>
        </div>
      </div>
      <div className="font-[500] text-[1.5rem] w-[70.375rem] h-[6.188rem] text-center leading-[2.043rem] text-white font-sans">
        our curriculum is geared towards all kinds of professional courses
        across the world, our aim is solely creating an effective and efficient
        method for students to pass exams without hassle, through our intense
        level of online preparation
      </div>
      <button className="w-[18.875rem] h-[4.375rem] bg-white text-[1.5rem] font-sans font-[700] rounded-lg">
        More
      </button>
    </div>
  );
};

export default CourseCard;
