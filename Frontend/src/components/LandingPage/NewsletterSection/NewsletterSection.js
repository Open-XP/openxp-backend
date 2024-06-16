import React from "react";

/**
 * Renders the NewsletterSection component.
 * This component displays a newsletter subscription section with a background image, title, description, and input field.
 * Users can enter their email address and subscribe to the newsletter.
 *
 * @returns {JSX.Element} The rendered NewsletterSection component.
 */
const NewsletterSection = () => {
  return (
    <div className="flex w-full h-[36.875rem] justify-center z-20">
      <img
        src={require("../../../icons/Asset.png")}
        alt="Newsletter Background"
        className="absolute w-[64.813rem] h-[36.875rem] -z-10"
      />
      <div className="flex flex-col w-[90rem] h-[36.875rem] justify-center items-center gap-[4rem]">
        <div className="w-[64.813rem] h-[11.125rem]">
          <div className="font-[700] text-[2.5rem] leading-[3.404rem] text-center text-purple-primary font-sans">
            Subscribe To Our Newsletter
          </div>
          <div className="font-[500] text-[2rem] leading-[2.724rem] text-center">
            Get news and information for any examination problem and <br />{" "}
            questions you may have
          </div>
        </div>
        <div className="flex">
          <input
            className="w-[50.813rem] h-[5rem] rounded-l-[3.438rem] px-[5rem] placeholder-white bg-purple-primary border-none font-sans font-[400] text-[2rem] text-white"
            placeholder="johndoe@gmail.com"
          />
          <button className="flex w-[20.625rem] h-[5rem] rounded-r-[3.438rem] font-[600] font-sans text-[2rem] leading-[2.724rem] bg-white border-1 border-custom-border justify-center items-center">
            Subscribe Now
          </button>
        </div>
      </div>
    </div>
  );
};

export default NewsletterSection;
