// Chart.js
const incomeCanvas = document.getElementById('income-chart');
const incomeCtx = incomeCanvas.getContext('2d');
const incomeDataElement = document.getElementById('income-data');
const incomeData = JSON.parse(incomeDataElement.textContent);

const incomePlugin = {
    id: 'centerText',
    afterDraw: function(chart) {
        let sum = 0;
        chart.data.datasets.forEach((dataset) => {
            sum += dataset.data.reduce((a, b) => a + b, 0);
        });

        const ctx = chart.ctx;
        ctx.save();
        ctx.font = '15px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'green';

        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 2;
        ctx.fillText(`R$ ${sum}`, centerX, centerY);
        ctx.restore();
    }
};

const incomeChart = new Chart(incomeCtx, {
    type: 'doughnut',
    data: {
        labels: incomeData.labels,
        datasets: [{
            label: 'Expenses',
            data: incomeData.data,
            backgroundColor: [
                'darkgreen',
                'forestgreen',
                'greenyellow',
                'lawngreen',
                'lime',
                'limegreen',
                'mediumseagreen',
                'olivedrab',
                'palegreen',
            ],
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false,
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return `R$ ${context.raw.toFixed(2)}`;
                    },
                },
                position: 'nearest',
                displayColors: false
            },
        },
        cutout: '70%',
    },
    plugins: [incomePlugin],
});

const expenseCanvas = document.getElementById('expense-chart');
const expenseCtx = expenseCanvas.getContext('2d');
const expenseDataElement = document.getElementById('expense-data');
const expenseData = JSON.parse(expenseDataElement.textContent);

const expensePlugin = {
    id: 'centerText',
    afterDraw: function(chart) {
        let sum = 0;
        chart.data.datasets.forEach((dataset) => {
            sum += dataset.data.reduce((a, b) => a + b, 0);
        });

        const ctx = chart.ctx;
        ctx.save();
        ctx.font = '15px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'red';

        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 2;
        ctx.fillText(`R$ ${sum}`, centerX, centerY);
        ctx.restore();
    }
};

const expenseChart = new Chart(expenseCtx, {
    type: 'doughnut',
    data: {
        labels: expenseData.labels,
        datasets: [{
            data: expenseData.data,
            backgroundColor: [
                'darkred',
                'brown',
                'firebrick',
                'indianred',
                'lightcoral',
                'maroon',
                'orangered',
                'palevioletred',
                'salmon',
            ],
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false,
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return `R$ ${context.raw.toFixed(2)}`;
                    },
                },
                position: 'nearest',
                displayColors: false
            },
        },
        cutout: '70%',
    },
    plugins: [expensePlugin],
});

const balanceCanvas = document.getElementById('balance-chart');
const balanceCtx = balanceCanvas.getContext('2d');
const balanceDataElement = document.getElementById('balance-data');

const totalIncome = balanceDataElement.getAttribute('data-income');
const totalExpense = balanceDataElement.getAttribute('data-expense');

const balanceData = {
    labels: ['Income', 'Expense'],
    data: [totalIncome, totalExpense],
};

const balancePlugin = {
    id: 'centerText',
    afterDraw: function(chart) {
        const sum = (totalIncome - totalExpense).toFixed(2);

        const ctx = chart.ctx;
        ctx.save();
        ctx.font = '15px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = sum >= 0 ? 'green' : 'red';

        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 2;
        ctx.fillText(`R$ ${sum}`, centerX, centerY);
        ctx.restore();
    }
};

const balanceChart = new Chart(balanceCtx, {
    type: 'doughnut',
    data: {
        labels: balanceData.labels,
        datasets: [{
            label: 'Expenses',
            data: balanceData.data,
            backgroundColor: [
                'green',
                'red',
            ],
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false,
            },
        },
        cutout: '70%',
    },
    plugins: [balancePlugin],
});
