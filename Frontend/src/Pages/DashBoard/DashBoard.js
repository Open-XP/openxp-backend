import React from "react";
import { Routes, Route, useLocation } from "react-router-dom";
import SideBar from "../../components/Dashboard/DashBoardSideBar/SideBar";
import DashboardNavBar from "../../components/Dashboard/DashBoardSideBar/DashboardNavBar";
import DashboardContent from "../../components/Dashboard/MainDashHome/DashboardContent";
import Void from "../../components/Dashboard/DashBoardSideBar/void";
import MockExam from "../../components/Dashboard/TestandSimulation/MockExams/MockExam";
import Evaluation from "../../components/Dashboard/TestandSimulation/EvaluationScreen/Evaluation";
import SummaryPage from "../../components/Dashboard/TestandSimulation/SummaryPage/SummaryPage";
import DashContent from "../../components/Dashboard/DashContent";

const NewDashBoard = () => {
  const location = useLocation();

  // Check if the current path includes "evaluation"
  const isEvaluationRoute =
    location.pathname.includes("/mock-exam/evaluation/") ||
    location.pathname.includes("dashboard/summary");

  // return (
  //   <div className="m-0">
  //     <div>
  //       <Routes>
  //         <Route path="/summary" element={<SummaryPage />} />
  //       </Routes>
  //     </div>
  //     {!isEvaluationRoute && <DashboardNavBar />}
  //     <div className="flex w-screen h-screen pt-40 gap-3">
  //       {!isEvaluationRoute && <Void />}
  //       <div className="flex-grow flex items-center justify-center">
  //         <Routes>
  //           <Route path="/" element={<DashboardContent />} />
  //           <Route path="/mock-exam" element={<MockExam />} />
  //           <Route path="/mock-exam/evaluation/:id" element={<Evaluation />} />
  //         </Routes>
  //       </div>
  //     </div>
  //     {!isEvaluationRoute && <SideBar />}
  //   </div>
  // );
  return (
    <div>
      <DashContent />
    </div>
  );
};

export default NewDashBoard;
