Ginkgo Data
-----------

This repository contains performance data for the
[Ginkgo library](https://github.com/ginkgo-project/ginkgo).
The performance data hosted in this repository is regularly updated to reflect
the latest version of the library via the CI system. To interactively generate
different visualizations of the data collected here, check out
[Ginkgo Performance Explorer](https://ginkgo-project.github.io/gpe).


## Repository structure and metadata

This repository contains two types of information:
1. Benchmark data of the Ginkgo library on different hardware in the [`data`
   folder](data);
2. Plot scripts for the GPE in the [`plots` folder](plots).

For most use cases, only benchmark `data` (1) are relevant.

### Repository structure

In the [`data/` folder](data), you can find the actual benchmark data listed.
The data is organized in a hierarchy of folders, with the following levels:

1. The hardware that is benchmarked, e.g. `MI100`
2. The Ginkgo executor controlling that hardware, e.g. `hip`
3. The type of data used by the benchmark, e.g. `SuiteSparse` for matrices from
   the [SuiteSparse Collection](https://sparse.tamu.edu/), or `blas.json` for
   synthetic Dense Linear Algebra benchmarks.
4. In some cases, extra levels are provided as data classification. For
   `SuiteSparse`, the matrices are put into different directories based on the
   collection they belong to.
5. The final benchmark data is always in standalone benchmark files.


Note that aggregated benchmark data can be present in the root `data` folder,
but they are only convenience files for the Ginkgo Performance Explorer and are
not always up to date. Scripts are provided also in the main `data` folder to
aggregate the standalone SuiteSparse JSON files.

Most of the data can be found in the `master` branch. Data can also be found in
other branches, either because the data was uploaded for debugging purposes, or
in the context of a scientific paper.

### Commits and data sources

The data can be added by:
1. The @ginkgo-bot account;
2. Any users who want to share their Ginkgo data benchmarks.

In the first case, the commit message will contain some benchmark metadata, usually in the form:
Benchmark <benchmark type> on <executor> with <hardware> of <ginkgo commit>

### [TODO]: Benchmark metadata file
For future benchmarks posted by the @ginkgo-bot account, a metadata file will be
added to provide extra information on the benchmark, such as the benchmark
configuration and the benchmarking environment.

## Benchmark data format

The benchmark data format and sometimes the data structure will change depending
on the benchmark type. They are usually defined by the `BENCHMARK` variable of
the [`run_all_benchmarks.sh`
script](https://github.com/ginkgo-project/ginkgo/tree/develop/benchmark/run_all_benchmarks.sh).
Ginkgo benchmarking is explained in detail in the [`BENCHMARKING.md`
file](https://github.com/ginkgo-project/ginkgo/tree/develop/BENCHMARKING.md). In
this section, we focus on the format of the specific JSON files.

The type can be (not necessarily up to date):

+ spmv: benchmark sparse matrix-vector product. This produces a SuiteSparse type
  of benchmark data.
+ solver: benchmark solvers, includes SpMV data and can include multiple
  preconditioners. This produces a SuiteSparse type of benchmark data.
+ preconditioner: synthetic preconditioner-only benchmarks, like for the
  Block-Jacobi preconditioner. This produces a preconditioner-specific type of
  data.
+ conversions: benchmark conversions between matrix formats. This produces a
  SuiteSparse type of benchmark data.
+ blas: benchmark Ginkgo dense BLAS functionality, like dot products, etc. This
  produces an array of data points for different synthetic sizes.
+ sparse_blas: a benchmark of Ginkgo Sparse BLAS functionality, like SpGEMM. 


### SuiteSparse data format
Since it is the most common data type, we mostly describe the SuiteSparse type
of benchmark data. The other benchmark data types are usually similar but
simpler.

For SuiteSparse data type, every matrix is in a different `.json` file. They can
easily be put together into a large array of data points. For each matrix, the
following data are always available:
+ filename: the full path to the matrix file that was benchmarked
+ problem: information about the matrix itself, like its unique SuiteSparse
  `id`, the `name` of the matrix, the `group` it is part of, etc, but also simple
  statistics about the row and column distribution of the nonzero elements in
  `row_distribution` and `col_distribution`.

The following data are benchmark dependent:
+ spmv: contains a list of data named after the benchmarked SpMV format. The
  memory consumption is available in `storage`, `completed` is true if the SpMV
  format could be run successfully (e.g., did not run out of memory), and `time`
  contains the time for each `repetition`.
  + the `optimal` SpMV format is also set as the fastest SpMV format
+ conversions: contains a list of data points each name in the form
  `source-destination` matrix formats. It contains `completed`, `repetitions`
  and `time` similarly to the SpMV benchmark.
+ solver: each solver data is provided under its solver name. If the solver is
  preconditioned, the preconditioner will be listed in the name. 
  + `recurrent`, `true` and `implicit` residual norms can be provided if a
    detailed benchmark was run (more time-consuming).
  + Also for a detailed run, `iteration_timestamps` are also listed in a corresponding array.
  + The two main subparts of the solver data are the `generate` which lists the
    amount of time taken to generate the solver from its factory, and the
    `apply` which tries to solve the problem with a specific Right Hand Side
    (RHS). The norm of the RHS is given in `rhs_norm`.
  + In `apply`, the number of `iterations` taken for solving and the `time` are
    always provided.
  + For both `generate` and `apply` in the case of a detailed run, the time
    taken for every solver sub-component (kernel, copies, etc) is given under
    `components`.
  + The `repetitions` and `completed` are the same as for the SpMV benchmark.

## Licensing

The Ginkgo benchmark data is available under the [CC-BY license](LICENSE.md).
All contributions to the project are added under this license. By pushing to
this repository, you agree to provide your data under the CC-BY license.
