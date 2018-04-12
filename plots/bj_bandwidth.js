var dataset_name = 'data/adaptive2.json'

var process_data = input => ({
    type: 'line',
    data: {
        labels: input.double.block_jacobi.map(elem => elem.num_blocks),
        datasets: [
            {
                label: 'double',
                data: input.double.block_jacobi.map(elem => elem.apply.bandwidth / 2**30),
                backgroundColor: window.chartColors.red,
                borderColor: window.chartColors.red,
                fill: false,
            },
            {
                label: 'single',
                data: input.single.block_jacobi.map(elem => elem.apply.bandwidth / 2**30),
                backgroundColor: window.chartColors.yellow,
                borderColor: window.chartColors.yellow,
                fill: false,
            },
            {
                label: 'adaptive [double x double]',
                data: input.double.adaptive_block_jacobi
                    .filter(elem => elem.block_precision == "double")
                    .map(elem => elem.apply.bandwidth / 2**30),
                backgroundColor: window.chartColors.blue,
                borderColor: window.chartColors.blue,
                fill: false,
            },
            {
                label: 'adaptive [single x double]',
                data: input.double.adaptive_block_jacobi
                    .filter(elem => elem.block_precision == "single")
                    .map(elem => elem.apply.bandwidth / 2**30),
                backgroundColor: window.chartColors.green,
                borderColor: window.chartColors.green,
                fill: false,
            },
            {
                label: 'adaptive [half x double]',
                data: input.double.adaptive_block_jacobi
                    .filter(elem => elem.block_precision == "half")
                    .map(elem => elem.apply.bandwidth / 2**30),
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
            text: 'Block-Jacobi apply bandwidth (block_size = 32)'
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
                    labelString: 'Number of diagonal blocks'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'GB/s'
                },
                ticks : {
                    min: 0
                }
            }]
        }
    }
});
