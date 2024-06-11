import React, { useState } from "react";
import { BarChart } from "@mui/x-charts/BarChart";
import Stack from "@mui/material/Stack";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";

export default function ChartsOverviewDemo() {
  const [timeFrame, setTimeFrame] = useState("monthly");

  const handleChange = (event) => {
    setTimeFrame(event.target.value);
  };

  // Define your data arrays
  const monthlyData = [
    {
      data: [44, 24, 34, 74, 62, 34, 56, 63, 83, 54, 46, 69],
      label: "Monthly Sales",
    },
    {
      data: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
      label: "Monthly Baseline",
    },
  ];
  const weeklyData = [
    {
      data: [10, 15, 20, 25, 30, 35, 70, 75, 65, 45, 60, 70],
      label: "Weekly Sales",
    },
    { data: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], label: "Weekly Baseline" },
  ];

  const data = timeFrame === "monthly" ? monthlyData : weeklyData;

  return (
    <div className="z-0">
      <Stack spacing={2}>
        <div className="flex justify-end">
          <FormControl style={{ width: "7rem" }}>
            <Select
              labelId="timeframe-select-label"
              id="timeframe-select"
              value={timeFrame}
              label="Timeframe"
              onChange={handleChange}
              className=""
            >
              <MenuItem value="weekly">Weekly</MenuItem>
              <MenuItem value="monthly">Monthly</MenuItem>
            </Select>
          </FormControl>
        </div>
        <BarChart
          series={data.map((dataset) => ({
            data: dataset.data,
            stack: "",
            color: dataset.label.includes("Sales")
              ? "rgba(45, 156, 219, 1)"
              : "rgba(40, 18, 102, 0.16)",
          }))}
          height={400}
          xAxis={[
            {
              data:
                timeFrame === "monthly"
                  ? [
                      "Jan",
                      "Feb",
                      "Mar",
                      "Apr",
                      "May",
                      "Jun",
                      "July",
                      "Aug",
                      "Sept",
                      "Oct",
                      "Nov",
                      "Dec",
                    ]
                  : [
                      "Week 1",
                      "Week 2",
                      "Week 3",
                      "Week 4",
                      "Week 5",
                      "Week 6",
                      "Week 7",
                      "Week 8",
                      "Week 9",
                      "Week 10",
                      "Week 11",
                      "Week 12",
                    ],
              scaleType: "band",
              categoryGapRatio: 0.7,
            },
          ]}
          borderRadius={18}
        />
      </Stack>
    </div>
  );
}
