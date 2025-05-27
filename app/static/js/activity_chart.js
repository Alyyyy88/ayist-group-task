// Simple User Activity Chart
document.addEventListener('DOMContentLoaded', function() {
  const chartCanvas = document.getElementById('userActivityChart');
  if (!chartCanvas) return;
  
  const ctx = chartCanvas.getContext('2d');
  
  const labels = [
    __('Monday'), __( 'Tuesday'), __('Wednesday'), __('Thursday'), __('Friday'), __('Saturday'), __('Sunday')
  ];

  const data = [65, 78, 82, 75, 92, 58, 42];
  
  const gradient = ctx.createLinearGradient(0, 0, 0, 300);
  gradient.addColorStop(0, 'rgba(79, 70, 229, 0.6)'); // Indigo
  gradient.addColorStop(1, 'rgba(79, 70, 229, 0.1)');
  
  const userChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'User Activity',
        data: data,
        backgroundColor: gradient,
        borderColor: 'rgb(79, 70, 229)',
        borderWidth: 1,
        borderRadius: 4,
        barPercentage: 0.6,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          backgroundColor: 'rgba(255, 255, 255, 0.9)',
          titleColor: '#333',
          bodyColor: '#666',
          borderColor: '#e2e8f0',
          borderWidth: 1,
          padding: 10,
          bodyFont: {
            size: 13
          },
          callbacks: {
            label: function(context) {
              return `Users: ${context.parsed.y}`;
            }
          }
        }
      },
      scales: {
        x: {
          grid: {
            display: false
          },
          ticks: {
            color: '#6b7280'
          }
        },
        y: {
          beginAtZero: true,
          ticks: {
            color: '#6b7280'
          },
          grid: {
            color: 'rgba(156, 163, 175, 0.1)'
          }
        }
      }
    }
  });
});