import React from "react";
import DashboardContent from "../../components/Dashboard/MainDashHome/DashboardContent";
import SideBar from "./DashBoardSideBar/SideBar";
import DashboardNavBar from "./DashBoardSideBar/DashboardNavBar";
import { Routes, Route } from "react-router-dom";
import Void from "./DashBoardSideBar/void";
import MockExam from "../../components/Dashboard/TestandSimulation/MockExams/MockExam";
import Evaluation from "../../components/Dashboard/TestandSimulation/EvaluationScreen/Evaluation";
import SummaryPage from "./TestandSimulation/SummaryPage/SummaryPage";

export function DashContent() {
  return (
    <div>
      <Routes>
        <Route
          path="/"
          element={
            <div>
              <DashboardNavBar />
              <div className="flex">
                <Void />
                <div className="flex w-full justify-center mt-[10rem]">
                  <DashboardContent />
                </div>
              </div>
              <SideBar />
            </div>
          }
        />
        <Route
          path="/mock-exam"
          element={
            <div>
              <DashboardNavBar className="-mt" />
              <div className="flex">
                <Void />
                <div className="flex w-full justify-center mt-[10rem]">
                  <MockExam />
                </div>
              </div>
              <SideBar />
            </div>
          }
        />
        <Route path="/mock-exam/evaluation/:id" element={<Evaluation />} />
        <Route path="/summary" element={<SummaryPage/>} />
      </Routes>
    </div>
  );
}

export default DashContent;
