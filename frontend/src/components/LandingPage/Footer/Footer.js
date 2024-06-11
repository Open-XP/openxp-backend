import React from "react";
import { Link } from "react-router-dom";

/**
 * Footer component.
 * Renders the footer section of the landing page.
 *
 * @returns {JSX.Element} The rendered JSX element.
 */
const Footer = () => {
  return (
    <div className="flex w-full h-[37.875rem] justify-center">
      <div className="absolute w-full h-[37.875rem] bg-purple-primary mix-blend-multiply -z-10"></div>
      <img
        src={require("../../../icons/footeroverlay.png")}
        alt="logo"
        className="absolute h-[37.875rem] w-[90rem] object-cover -z-20 mix-blend-multiply"
      />
      <div className="flex mt-[8rem] gap-[5rem] text-white font-sans">
        <div className="flex flex-col gap-3">
          <div className="w-107.625rem] h-[2.063rem] font-[700] text-[1.5rem]  text-white">
            Openpx
          </div>
          <div className="flex gap-[1rem]">
            <img
              src={require("../../../icons/instagram-logo-f.png")}
              alt="Instagram logo"
              className="w-[1.563rem] h-[1.563rem]"
            />
            <img
              src={require("../../../icons/facebook-f.png")}
              alt="Facebook logo"
              className="w-[1.563rem] h-[1.563rem]"
            />
            <img
              src={require("../../../icons/twitter-f.png")}
              alt="Twitter logo"
              className="w-[1.563rem] h-[1.563rem]"
            />
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <div className="w-107.625rem] h-[2.063rem] font-[700] text-[1.5rem] ">
            About
          </div>
          <div className="flex flex-col">
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              News
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Impact
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Community
            </Link>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <div className="w-107.625rem] h-[2.063rem] font-[700] text-[1.5rem] ">
            Contact Us
          </div>
          <div className="flex flex-col">
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Mail
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Phone
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Whatsapp
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Slack
            </Link>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <div className="w-107.625rem] h-[2.063rem] font-[700] text-[1.5rem] ">
            Exam Library
          </div>
          <div className="flex flex-col">
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              WAEC
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              JAMB
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              NECO
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              NCEE
            </Link>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <div className="w-107.625rem] h-[2.063rem] font-[700] text-[1.5rem] ">
            Exam Library
          </div>
          <div className="flex flex-col">
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              WAEC
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              JAMB
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              NECO
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              NCEE
            </Link>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <div className="w-107.625rem] h-[2.063rem] font-[700] text-[1.5rem] ">
            Community
          </div>
          <div className="flex flex-col">
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Whatsapp
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Discord
            </Link>
            <Link className="font-[400] text-[1.25rem] leading-[1.703rem]">
              Slack
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
