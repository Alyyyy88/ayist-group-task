const ctx = document.getElementById("revenue-chart").getContext("2d");

    const chartConfig = new Chart(ctx, {
      type: "line",
      data: {
        labels: [
          __("Jan"),
          __("Feb"),
          __("Mar"),
          __("Apr"),
          __("May"),
          __("Jun"),
        ],
        datasets: [
          {
            label: "Revenue",
            data: [12000, 15000, 17000, 13000, 18000],
            borderColor: "#4F46E5",
            backgroundColor: "rgba(79, 70, 229, 0.1)",
            fill: true,
            tension: 0.4,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: false,
          },
          tooltip: {
            mode: "index",
            intersect: false,
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
            grid: {
              color: "#E5E7EB",
            },
          },
        },
      },
    });