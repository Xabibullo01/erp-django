function renderPie(labels, data) {
  const ctx = document.getElementById('pieChart').getContext('2d');

  // Destroy old chart if exists (in case of re-render)
  if(window.pieChartInstance) window.pieChartInstance.destroy();

  window.pieChartInstance = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        data: data,
        backgroundColor: generateColorPalette(data.length),
        borderWidth: 1,
        borderColor: '#fff',
      }],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'right',
          labels: {
            boxWidth: 18,
            padding: 15,
            font: { size: 13 },
          },
          maxHeight: 150,
          maxWidth: 250,
        },
        tooltip: {
          enabled: true,
          callbacks: {
            label: ctx => ctx.label + ': ' + ctx.parsed.toLocaleString(),
          }
        }
      },
      cutout: '60%',
    },
  });
}

function renderBarLine(months, revenue, cost, profit) {
  const ctx = document.getElementById('barLineChart').getContext('2d');

  if(window.barLineChartInstance) window.barLineChartInstance.destroy();

  window.barLineChartInstance = new Chart(ctx, {
    data: {
      labels: months,
      datasets: [
        {
          type: 'bar',
          label: 'Tushum',
          data: revenue,
          backgroundColor: 'rgba(0, 123, 255, 0.7)',
          borderRadius: 6,
          barPercentage: 0.5,
        },
        {
          type: 'bar',
          label: 'Xarajat',
          data: cost,
          backgroundColor: 'rgba(220, 53, 69, 0.7)',
          borderRadius: 6,
          barPercentage: 0.5,
        },
        {
          type: 'line',
          label: 'Foyda',
          data: profit,
          borderColor: '#ffc107',
          backgroundColor: '#ffc107',
          borderWidth: 3,
          tension: 0.3,
          fill: false,
          pointRadius: 5,
          pointHoverRadius: 8,
          yAxisID: 'y1',
        }
      ]
    },
    options: {
      responsive: true,
      interaction: {
        mode: 'nearest',
        intersect: false,
      },
      scales: {
        y: {
          beginAtZero: true,
          position: 'left',
          title: {
            display: true,
            text: 'Summa (so‘m)',
          },
          ticks: {
            callback: value => value.toLocaleString(),
          }
        },
        y1: {
          beginAtZero: true,
          position: 'right',
          grid: {
            drawOnChartArea: false,
          },
          title: {
            display: true,
            text: 'Foyda (so‘m)',
          },
          ticks: {
            callback: value => value.toLocaleString(),
          }
        }
      },
      plugins: {
        legend: {
          position: 'top',
          labels: {
            font: { size: 14, weight: '600' },
          },
        },
        tooltip: {
          callbacks: {
            label: ctx => ctx.dataset.label + ': ' + ctx.parsed.y.toLocaleString(),
          },
        },
      },
    }
  });
}

// Helper function to generate color palette dynamically
function generateColorPalette(count) {
  const palette = [];
  const baseColors = [
    '#007bff', '#28a745', '#ffc107', '#dc3545', '#6f42c1', '#20c997', '#fd7e14', '#6610f2', '#e83e8c', '#17a2b8'
  ];
  for(let i = 0; i < count; i++) {
    palette.push(baseColors[i % baseColors.length]);
  }
  return palette;
}
