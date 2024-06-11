import React from "react";

const TestimonialSection = () => {
  return (
    <div className="flex w-full h-[90rem] 2xl:h-[59.75rem] justify-center items-center">
      <div className="flex flex-col w-[90rem] h-full 2xl:h-[56.875rem] justify-center items-center gap-[4rem]">
        <div className="flex flex-col w-[62.875rem] h-[10rem] items-center justify-between">
          <div className="font-[700] text-[2.5rem] leading-[3.413rem] font-sans">
            Openxp Testimonials{" "}
          </div>
          <div className="font-[500] text-[2rem] leading-[2.724rem] text-center font-sans">
            Join Us Today and beocome a straight A student, below are some of
            our outstanding students, who aced their exams with ease
          </div>
        </div>
        <div className="flex flex-col 2xl:flex-row 2xl:gap-4 gap-[4rem]">
          <div
            className="flex flex-col w-[37.438rem] h-[31.125rem] p-5 gap-3"
            style={{ border: "1px solid #2D9CDB" }}
          >
            <img
              src={require("../../../icons/Mask-group.png")}
              className="w-[6.5rem] h-[6.5rem]"
            />
            <div className="font-[600] text-[1.25rem] leading-[1.703rem] font-sans">
              Joining Openxp was a game-changer for my academic journey. Their
              resources and support network helped me tackle my toughest
              subjects with confidence. Thanks to their comprehensive tools and
              expert guidance, I aced my exams and secured a scholarship to my
              dream university. Openxp truly equips you with everything you need
              to succeed.
            </div>
            <div className="font-[700] text-[1.5rem] text-[#2D9CDB] font-sans">
              Ariana Baker
            </div>
          </div>
          <div className="flex flex-col w-[37.438rem] h-[31.125rem] p-5 gap-3 shadow-custom2">
            <img
              src={require("../../../icons/Mask-group.png")}
              className="w-[6.5rem] h-[6.5rem]"
            />
            <div className="font-[600] text-[1.25rem] leading-[1.703rem] font-sans">
              Openxp has Played a vital role in me becoming a model student, and
              true their help I have been able pass my final exams in order for
              me to study internationally.Growing as up from a humble
              background, I understand how much it means to put your all, and
              openxp gives you a very big community to support and learn.
            </div>
            <div className="font-[700] text-[1.5rem] text-[#2D9CDB] font-sans">
              - Samuel Johnson
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TestimonialSection;
