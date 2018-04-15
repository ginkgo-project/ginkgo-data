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

// set display options
// TODO: make this modifiable for other kinds of plots
var options = {
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
};

// This function will be called with an array of input objects that need to be
// plotted. It should return an object with plotting descriptions which will be
// passed to Chart.js.
function generate_plot_data(inputs) {
    if (inputs.length == 0) {
        return {
            type: 'line',
            data: {
                labels: [],
                datasets: []
            },
            options: options
        };
    }

    var max_blocks =
        Math.max(...inputs[0].content.data.map(e => e.num_blocks));
    // extract x-axis labels from first input
    var labels = inputs[0].content.data
        .filter(e => e.num_blocks == max_blocks)
        .map(e => e.block_size);
    // exract performance from each input
    var datasets = inputs.map(input => ({
        label: input.name,
        data: input.content.data
            .filter(e => e.num_blocks == max_blocks)
            .map(e => (e.flops / e.time) / 1e9)
    }));

    // add display options to each dataset
    var colors = generate_colors(datasets.length);
    for (var i = 0; i < datasets.length; ++i) {
        Object.assign(datasets[i], {
            backgroundColor: colors[i],
            borderColor: colors[i],
            fill: false
        });
    }

    return {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: options
    };
}


return {
    generate_plot_data: generate_plot_data
};
