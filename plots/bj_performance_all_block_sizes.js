var dataset_name = 'data/adaptive_all_block_sizes.json'

var process_data = input => ({
    type: 'line',
    data: {
        labels: input.double.block_jacobi.map(elem => elem.block_size),
        datasets: [
            {
                label: 'double',
                data: input.double.block_jacobi.map(elem => elem.apply.performance / 1e9),
                backgroundColor: window.chartColors.red,
                borderColor: window.chartColors.red,
                fill: false,
            },
            {
                label: 'single',
                data: input.single.block_jacobi.map(elem => elem.apply.performance / 1e9),
                backgroundColor: window.chartColors.yellow,
                borderColor: window.chartColors.yellow,
                fill: false,
            },
            {
                label: 'adaptive [double x double]',
                data: input.double.adaptive_block_jacobi
                    .filter(elem => elem.block_precision == "double")
                    .map(elem => elem.apply.performance / 1e9),
                backgroundColor: window.chartColors.blue,
                borderColor: window.chartColors.blue,
                fill: false,
            },
            {
                label: 'adaptive [single x double]',
                data: input.double.adaptive_block_jacobi
                    .filter(elem => elem.block_precision == "single")
                    .map(elem => elem.apply.performance / 1e9),
                backgroundColor: window.chartColors.green,
                borderColor: window.chartColors.green,
                fill: false,
            },
            {
                label: 'adaptive [half x double]',
                data: input.double.adaptive_block_jacobi
                    .filter(elem => elem.block_precision == "half")
                    .map(elem => elem.apply.performance / 1e9),
                backgroundColor: window.chartColors.teal,
                borderColor: window.chartColors.teal,
                fill: false,
            },
        ]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Block-Jacobi apply performance (#blocks = 50000)'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Block size'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'GFLOP/s'
                },
                ticks : {
                    min: 0
                }
            }]
        }
    }
});
