document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("mychart");

  if (!ctx) {
    return;
  }

  // Cash flow data for the last 6 months
  const months = [
    __("Jan"),
    __("Feb"),
    __("Mar"),
    __("Apr"),
    __("May"),
    __("Jun"),
  ];
  const incomeData = [42000, 45800, 48500, 51200, 53600, 56800];
  const expensesData = [28400, 29100, 30500, 31200, 31800, 32300];
  const profitData = incomeData.map(
    (income, index) => income - expensesData[index]
  );

  const cashFlowChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: months,
      datasets: [
        {
          label: __("Income"),
          data: incomeData,
          borderColor: "rgb(34, 197, 94)", // green-500
          backgroundColor: "rgba(34, 197, 94 , 0.7)",
          tension: 0.3,
          fill: true,
        },
        {
          label: __("Expenses"),
          data: expensesData,
          borderColor: "rgb(239, 68, 68)", // red-500
          backgroundColor: "rgba(239, 68, 68, 0.7)",
          tension: 0.3,
          fill: true,
        },
        {
          label: __("Profit"),
          data: profitData,
          borderColor: "rgb(59, 130, 246)", // blue-500
          backgroundColor: "rgba(59, 130, 246, 0.7)",
          tension: 0.3,
          fill: true,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          mode: "index",
          intersect: false,
          callbacks: {
            label: function (context) {
              let label = context.dataset.label || "";
              if (label) {
                label += ": ";
              }
              if (context.parsed.y !== null) {
                label += new Intl.NumberFormat("pl-PL", {
                  style: "currency",
                  currency: "PLN",
                  minimumFractionDigits: 0,
                }).format(context.parsed.y);
              }
              return label;
            },
          },
        },
      },
      scales: {
        x: {
          grid: {
            display: false,
          },
        },
        y: {
          beginAtZero: true,
          ticks: {
            callback: function (value) {
              return "zł " + value.toLocaleString();
            },
          },
        },
      },
    },
  });

  const loadingIndicator = document.querySelector(
    "#cashFlowChart .flex.items-center.justify-center"
  );
  if (loadingIndicator) {
    loadingIndicator.style.display = "none";
  }
});
