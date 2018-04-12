// A utility function that will generate some colors for our plot
function generate_colors(num_colors) {
    var colors = [];
    var toRange = (min, max, number) =>
        Number.parseFloat(number * (max - min) + min).toFixed(0);
    for (var i = 0; i < num_colors; ++i) {
        var hue = toRange(0, 360, i / num_colors);
        var sat = 50;
        var lhs = 60;
        colors.push('hsl(' + hue + ',' + sat + '%,' + lhs + '%)');
    }
    return colors;
}

// This function will be called with an array of input objects that need to be
// plotted. It should return an object with plotting descriptions which will be
// passed to Chart.js.
function generate_plot_data(input) {
    //extract interesting data
    var datasets = [];
    if (input.length > 0) {
        datasets.push({
            label: 'double',
            data: input[0].content.double.block_jacobi
        });
        datasets.push({
            label: 'single',
            data: input[0].content.single.block_jacobi
        });
    }
    for (var i = 0; i < input.length; ++i) {
        datasets.push({
            label: 'adaptive double-by-double [' + i + ']',
            data: input[i].content.double.adaptive_block_jacobi
                    .filter(e => e.block_precision === "double")
        });
        datasets.push({
            label: 'adaptive single-by-double [' + i + ']',
            data: input[i].content.double.adaptive_block_jacobi
                    .filter(e => e.block_precision === "single")
        });
        datasets.push({
            label: 'adaptive half-by-double [' + i + ']',
            data: input[i].content.double.adaptive_block_jacobi
                    .filter(e => e.block_precision === "half")
        });
    }

    //process each dataset
    var colors = generate_colors(datasets.length);
    var labels = [];
    for (var i = 0; i < datasets.length; ++i) {
        var dataset = datasets[i];
        var max_blocks = Math.max(...dataset.data.map(el => el.num_blocks));
        if (i === 0) {
            labels = dataset.data
                .filter(elem => elem.num_blocks === max_blocks)
                .map(elem => elem.block_size);
        }
        dataset.data = dataset.data
            .filter(elem => elem.num_blocks === max_blocks)
            .map(elem => elem.apply.bandwidth / 2**30);
        dataset.backgroundColor = colors[i];
        dataset.borderColor = colors[i];
        dataset.fill = false;
    }
    return {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Block-Jacobi apply bandwidth (#blocks = 50000)'
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
    };
}

return {
    generate_plot_data: generate_plot_data
};
