const attendanceCtx = document
  .getElementById("attendanceChart")
  .getContext("2d");
const attendanceChart = new Chart(attendanceCtx, {
  type: "bar",
  data: {
    labels: [
      __("Monday"),
      __("Tuesday"),
      __("Wednesday"),
      __("Thursday"),
      __("Friday"),
    ],
    datasets: [
      {
        label: "Attendance Rate (%)",
        data: [95, 88, 92, 97, 96.5],
        backgroundColor: [
          "#16a34a",
          "#16a34a",
          "#16a34a",
          "#16a34a",
          "#16a34a",
        ],
        borderColor: [
          "#16a34a",
          "#16a34a",
          "#16a34a",
          "#16a34a",
          "#16a34a",
          "#16a34a",
          "#16a34a",
        ],
        borderWidth: 2,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        max: 100,
      },
    },
    responsive: true,
    maintainAspectRatio: true,
  },
});
