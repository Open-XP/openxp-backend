import React from "react";

export function AreaOfImprovement() {
  return (
    <div className="bg-white rounded-lg h-[16rem]">
      <div className="flex justify-between text-left text-white bg-[#2D9CDB] p-2 rounded gap-4">
        <div className="w-1/3 text-center">Area of Improvements</div>
        <div className="w-1/3 text-center">Scores</div>
        <div className="w-1/3 text-center">Grades</div>
      </div>
      <div className="flex justify-between p-2 border-b">
        <div className="w-1/3 text-center">English</div>
        <div className="w-1/3 text-center">40%</div>
        <div className="w-1/3 text-center">D</div>
      </div>
      <div className="flex justify-between p-2 border-b">
        <div className="w-1/3 text-center">Mathematics</div>
        <div className="w-1/3 text-center">70%</div>
        <div className="w-1/3 text-center">A</div>
      </div>
      <div className="flex justify-between p-2 border-b">
        <div className="w-1/3 text-center">Chemistry</div>
        <div className="w-1/3 text-center">70%</div>
        <div className="w-1/3 text-center">A</div>
      </div>
      <div className="flex justify-between p-2 border-b">
        <div className="w-1/3 text-center">Biology</div>
        <div className="w-1/3 text-center">60%</div>
        <div className="w-1/3 text-center">B</div>
      </div>
      <div className="flex justify-between p-2">
        <div className="w-1/3 text-center">Physics</div>
        <div className="w-1/3 text-center">50%</div>
        <div className="w-1/3 text-center">C</div>
      </div>
    </div>
  );
}

export default AreaOfImprovement;
