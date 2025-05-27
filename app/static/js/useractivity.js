
  document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.activity-filter button');
    const activities = document.querySelectorAll('.activity-item');
    const tabPanes = document.querySelectorAll('.tab-pane');


    const performanceCtx = document.getElementById('performanceChart').getContext('2d');
    const performanceChart = new Chart(performanceCtx, {
      type: 'line',
      data: {
        labels: [
          __('Jan'), __('Feb'), __('Mar'), __('Apr'), __('May'), __('Jun')
        ],
        datasets: [{
          label: 'Performance Rating',
          data: [4.2, 4.5, 4.3, 4.6, 4.7, 4.5],
          borderColor: '#6366f1',
          backgroundColor: 'rgba(99, 102, 241, 0.2)',
          fill: true,
          tension: 0.3
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            max: 5
          }
        },
        responsive: true,
        maintainAspectRatio: true
      }
    });
    
    buttons.forEach(button => {
      button.addEventListener('click', function () {
        buttons.forEach(btn => {
          btn.classList.remove('bg-indigo-100', 'text-indigo-800');
          btn.classList.add('bg-gray-100', 'text-gray-800');
        });
        this.classList.remove('bg-gray-100', 'text-gray-800');
        this.classList.add('bg-indigo-100', 'text-indigo-800');
        
        const tabId = this.getAttribute('data-tab');
        tabPanes.forEach(pane => {
          pane.classList.add('hidden');
        });
        document.getElementById(tabId).classList.remove('hidden');
        
        const filter = this.getAttribute('data-filter');
        if (filter === 'all') {
          activities.forEach(activity => {
            activity.style.display = 'flex';
          });
        } else {
          activities.forEach(activity => {
            if (activity.classList.contains(filter)) {
              activity.style.display = 'flex';
            } else {
              activity.style.display = 'none';
            }
          });
        }
      });
    });
  });