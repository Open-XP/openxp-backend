import React from "react";

/**
 * Renders a quote section component.
 * @returns {JSX.Element} The rendered quote section.
 */
const QuoteSection = () => {
  return (
    <div className="flex absolute left-1/2 transform -translate-x-1/2 bg-white w-[78.625rem] h-[17.5rem] top-[152rem] 2xl:top-[115.75rem] justify-center items-center shadow-custom2">
      <div className="flex flex-col w-[65rem] h-[9.063rem] gap-[0.55rem]">
        <div className="font-[700] text-[2rem] leading-[2.724rem] text-center font-sans">
          "Education is the most powerful weapon which you can use to change the
          world."
        </div>
        <div className="font-[400] text-[2rem] leading-[2.724rem] font-sans text-center">
          Nelson Mandela
        </div>
      </div>
    </div>
  );
};

export default QuoteSection;
