import React from "react";
import { ReactComponent as WaecLogo } from "../../../svgs/waec-small.svg";
import { ReactComponent as JambLogo } from "../../../svgs/jamb-small.svg";
import { ReactComponent as NecoLogo } from "../../../svgs/neco-small.svg";

/**
 * Renders the second section of the landing page.
 * This component displays information about real-time exam simulations and study resources.
 * It also showcases the Waec Examination Question and Materials.
 *
 * @returns {JSX.Element} The rendered SecondSection component.
 */
const SecondSection = () => {
  return (
    <div className="flex w-full justify-center">
      <div className="flex flex-col items-center 2xl:flex-row w-[90rem] h-[80rem] 2xl:h-[64.313rem] mt-[5rem] gap-[3rem] justify-center">
        <div className="w-[45%] 2xl:w-[47%] 2xl:h-[33.938rem] 2xl:mt-0 -mt-[10rem]">
          <div className="flex flex-col gap-[1.938rem]">
            <div className="flex w-[23.625rem] gap-[0.75rem] items-center">
              <img
                className="w-[1.25rem] h-[1.25rem]"
                src={require("../../../icons/screen.png")}
                alt="Screen icon"
              />
              <div className="font-[700] text-[#2D9CDB] font-sans text-[1rem] leading-[1.362rem]">
                Real Time Exam Simulations and resources.
              </div>
            </div>
            <div className="font-[700] text-[1.75rem] leading-[2.383rem] font-sans">
              Practice Popular Exam Questions <br /> Guaranteed to aid you ace{" "}
              <br />
              your forthcoming Exams.
            </div>
            <div className="flex flex-col gap-[0.625rem]">
              <div className="flex items-center gap-[0.625rem]">
                <img
                  className="w-[1.01rem] h-[1.01rem]"
                  src={require("../../../icons/shield-check.png")}
                  alt="shild icon"
                />
                <div className="font-[500] text-[1.25rem] leading-[1.703rem]">
                  Your One-Stop Solution to Exam Worries.
                </div>
              </div>
              <div className="flex items-center gap-[0.625rem]">
                <img
                  className="w-[1.01rem] h-[1.01rem]"
                  src={require("../../../icons/shield-check.png")}
                  alt="shild icon"
                />
                <div className="font-[500] text-[1.25rem] leading-[1.703rem]">
                  Access a comprehensive library of study resources.
                </div>
              </div>
              <div className="flex items-center gap-[0.625rem]">
                <img
                  className="w-[1.01rem] h-[1.01rem]"
                  src={require("../../../icons/shield-check.png")}
                  alt="shild icon"
                />
                <div className="font-[500] text-[1.25rem] leading-[1.703rem]">
                  Experience real-time exam simulations.
                </div>
              </div>
              <div className="flex items-center gap-[0.625rem]">
                <img
                  className="w-[1.01rem] h-[1.01rem]"
                  src={require("../../../icons/shield-check.png")}
                  alt="shild icon"
                />
                <div className="font-[500] text-[1.25rem] leading-[1.703rem]">
                  Boost your confidence with guaranteed practice questions.
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="flex w-[45%] 2xl:w-[53%] h-[33.938rem] ">
          <div className="w-full 2xl:w-[38.25rem] h-[33.938rem] shadow-custom2">
            <div className="flex h-[8.438rem] w-full 2xl:w-[38.813rem] items-center justify-center gap-[0.938rem] shadow-custom">
              <WaecLogo className="w-[3.938rem] h-[3.938rem]" />
              <div className="font-[500] text-[1.25rem] leading-[1.703rem] font-sans box-s">
                WAEC Examination Question and Materials
              </div>
            </div>
            <div className="flex h-[8.438rem] w-full 2xl:w-[38.813rem] items-center justify-center gap-[0.938rem] shadow-custom">
              <JambLogo className="w-[3.938rem] h-[3.938rem]" />
              <div className="font-[500] text-[1.25rem] leading-[1.703rem] font-sans">
                JAMB Examination Question and Materials
              </div>
            </div>
            <div className="flex h-[8.438rem] w-full 2xl:w-[38.813rem] items-center justify-center gap-[0.938rem] shadow-custom">
              <NecoLogo className="w-[3.938rem] h-[3.938rem]" />
              <div className="font-[500] text-[1.25rem] leading-[1.703rem] font-sans">
                NECO Examination Question and Materials
              </div>
            </div>
            <div className="flex h-[8.438rem] w-full 2xl:w-[38.813rem] items-center justify-center gap-[0.938rem] shadow-custom">
              <NecoLogo className="w-[3.938rem] h-[3.938rem]" />
              <div className="font-[500] text-[1.25rem] leading-[1.703rem] font-sans">
                NCEE Examination Question and Materials
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SecondSection;
