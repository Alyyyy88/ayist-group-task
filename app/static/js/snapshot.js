// snapshot.js - Mini Financial Snapshot functionality
document.addEventListener('DOMContentLoaded', function() {
  if (document.getElementById('miniProfitChart')) {
    initMiniProfitChart();
  }
  
  if (document.getElementById('quickDate')) {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('quickDate').value = today;
  }
  
  if (document.getElementById('quickEntryForm')) {
    document.getElementById('quickEntryForm').addEventListener('submit', function(e) {
      e.preventDefault();
      saveQuickEntry();
    });
  }
  
  setupSnapshotToggle();
  
  if (document.querySelector('#quickEntryPopup > div')) {
    document.querySelector('#quickEntryPopup > div').addEventListener('click', function(e) {
      e.stopPropagation();
    });
  }
});

function setupSnapshotToggle() {
  const quickSnapshot = document.getElementById('quickFinancialSnapshot');
  const toggleButton = document.getElementById('toggleFinancialSnapshot');
  const closeButton = document.getElementById('closeQuickSnapshot');
  
  if (quickSnapshot && toggleButton) {
    quickSnapshot.classList.add('hidden');
    
    toggleButton.addEventListener('click', function() {
      quickSnapshot.classList.remove('hidden');
      toggleButton.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
      toggleButton.title = 'Hide Financial Snapshot';
    });
    
    if (closeButton) {
      closeButton.addEventListener('click', function() {
        quickSnapshot.classList.add('hidden');
        toggleButton.innerHTML = '<i class="fa-solid fa-eye"></i>';
        toggleButton.title = 'Show Financial Snapshot';
      });
    }
  }
}

function initMiniProfitChart() {
  const ctx = document.getElementById('miniProfitChart').getContext('2d');
  
  const labels = Array.from({length: 30}, (_, i) => i + 1);
  const data = [620, 580, 610, 650, 600, 640, 630, 660, 680, 650, 670, 690, 
               710, 700, 680, 720, 710, 730, 750, 740, 760, 770, 790, 800, 
               780, 810, 830, 820, 850, 870];
  
  const miniChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Profit',
        data: data,
        borderColor: 'rgb(59, 130, 246)', // blue-500
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        tension: 0.4,
        fill: true,
        pointRadius: 0,
        borderWidth: 2
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
          enabled: true,
          mode: 'index',
          intersect: false,
          callbacks: {
            label: function(context) {
              let label = context.dataset.label || '';
              if (label) {
                label += ': ';
              }
              if (context.parsed.y !== null) {
                label += new Intl.NumberFormat('pl-PL', {
                  style: 'currency',
                  currency: 'PLN',
                  minimumFractionDigits: 0
                }).format(context.parsed.y);
              }
              return label;
            }
          }
        }
      },
      scales: {
        x: {
          display: false
        },
        y: {
          display: false,
          beginAtZero: false
        }
      }
    }
  });
}

function openQuickEntryForm(type) {
  const popup = document.getElementById('quickEntryPopup');
  const title = document.getElementById('quickEntryTitle');
  const submitBtn = document.getElementById('quickSubmitBtn');
  const categorySelect = document.getElementById('quickCategory');
  
  categorySelect.innerHTML = '<option value="">Select category</option>';
  
  if (type === 'income') {
    title.textContent = 'Add Income';
    submitBtn.className = 'px-4 py-2 text-sm text-white bg-green-600 rounded-md hover:bg-green-700';
    
    const incomeCategories = ['Sales', 'Investments', 'Services', 'Other Income'];
    incomeCategories.forEach(cat => {
      const option = document.createElement('option');
      option.value = cat.toLowerCase();
      option.textContent = cat;
      categorySelect.appendChild(option);
    });
  } else {
    title.textContent = 'Add Expense';
    submitBtn.className = 'px-4 py-2 text-sm text-white bg-red-600 rounded-md hover:bg-red-700';
    
    const expenseCategories = ['Supplies', 'Payroll', 'Operations', 'Marketing', 'Other Expenses'];
    expenseCategories.forEach(cat => {
      const option = document.createElement('option');
      option.value = cat.toLowerCase();
      option.textContent = cat;
      categorySelect.appendChild(option);
    });
  }
  
  document.getElementById('quickEntryForm').dataset.type = type;
  
  popup.classList.remove('hidden');
  popup.style.display = 'flex';
}

function closeQuickEntryForm(event) {
  if (event) event.stopPropagation();
  
  const popup = document.getElementById('quickEntryPopup');
  popup.classList.add('hidden');
  popup.style.display = 'none';
  
  document.getElementById('quickEntryForm').reset();
}

function saveQuickEntry() {
  const form = document.getElementById('quickEntryForm');
  const type = form.dataset.type;
  const amount = document.getElementById('quickAmount').value;
  const category = document.getElementById('quickCategory').value;
  const date = document.getElementById('quickDate').value;
  const note = document.getElementById('quickNote').value;
  
  const alertContainer = document.createElement('div');
  alertContainer.className = 'fixed top-4 right-4 bg-white rounded-lg shadow-lg p-4 border-l-4 border-green-500 transform transition-all duration-500 ease-in-out flex items-center z-50';
  alertContainer.style.maxWidth = '350px';

  const iconDiv = document.createElement('div');
  iconDiv.className = 'text-green-500 mr-3 flex-shrink-0';
  iconDiv.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>';

  const textDiv = document.createElement('div');
  textDiv.className = 'flex-grow';
  const title = document.createElement('h4');
  title.className = 'font-medium text-gray-800';
  title.textContent = type === 'income' ? 'Income Added' : 'Expense Added';
  const message = document.createElement('p');
  message.className = 'text-sm text-gray-600';
  message.textContent = `${type === 'income' ? 'Income' : 'Expense'} of $${amount} has been recorded.`;

  textDiv.appendChild(title);
  textDiv.appendChild(message);

  alertContainer.appendChild(iconDiv);
  alertContainer.appendChild(textDiv);
  document.body.appendChild(alertContainer);

  setTimeout(() => {
    alertContainer.style.opacity = '0';
    alertContainer.style.transform = 'translateX(100%)';
    setTimeout(() => {
      document.body.removeChild(alertContainer);
    }, 500);
  }, 3000);
  closeQuickEntryForm();
  
  updateFinancialSnapshot(type, parseFloat(amount));
}

function updateFinancialSnapshot(type, amount) {
  
  const incomeEl = document.querySelector('[data-target="18500"]');
  const expensesEl = document.querySelector('[data-target="10800"]');
  const profitEl = document.querySelector('[data-target="7700"]');
  
  if (type === 'income') {
    const currentIncome = parseFloat(incomeEl.dataset.target);
    const newIncome = currentIncome + amount;
    incomeEl.dataset.target = newIncome.toString();
    incomeEl.textContent = 'zł' + newIncome.toLocaleString();
    
    const currentProfit = parseFloat(profitEl.dataset.target);
    const newProfit = currentProfit + amount;
    profitEl.dataset.target = newProfit.toString();
    profitEl.textContent = 'zł' + newProfit.toLocaleString();
  } else if (type === 'expense') {
    const currentExpenses = parseFloat(expensesEl.dataset.target);
    const newExpenses = currentExpenses + amount;
    expensesEl.dataset.target = newExpenses.toString();
    expensesEl.textContent = 'zł' + newExpenses.toLocaleString();
    
    const currentProfit = parseFloat(profitEl.dataset.target);
    const newProfit = currentProfit - amount;
    profitEl.dataset.target = newProfit.toString();
    profitEl.textContent = 'zł' + newProfit.toLocaleString();
  }
}