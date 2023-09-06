# scqbenchmark

Instruction:

1. If you are not using Apple M1/M2 silicon, put the following commands in your terminal one by one (don’t skip anyone!)
```ruby
git clone https://github.com/yunweilu/scqbenchmark
cd scqbenchmark
conda env create -f create_environment.yml
conda env update -f update.yml --prune
conda activate benchmark_scq_v9
cd scqbenchmark
jupyter notebook
```

If you are using Apple M1/M2 arm64 processors, the environment can be configured to build packages that can run directly on the arm64 processors:
```ruby
git clone https://github.com/yunweilu/scqbenchmark
cd scqbenchmark
CONDA_SUBDIR=osx-arm64 conda env create -f create_environment_macarm.yml
CONDA_SUBDIR=osx-arm64 conda env update -f update_macarm.yml --prune
conda activate benchmark_scq_v9
cd scqbenchmark
jupyter notebook
```
Essentially, the mkl-devel requirement is removed.

Otherwise, if you hope to configure the environment such that packages are built to work in x86_64 fashion and are executed under ``compatibility mode" with Rosetta2, run the following lines:
```ruby
git clone https://github.com/yunweilu/scqbenchmark
cd scqbenchmark
CONDA_SUBDIR=osx-64 conda env create -f create_environment.yml
CONDA_SUBDIR=osx-64 conda env update -f update.yml --prune
conda activate benchmark_scq_v9
cd scqbenchmark
jupyter notebook
```
Notice here that `update.yml` is used instead of ·update_macarm.yml·

If you are windows user, and have error message from installing primme, follow the first four steps in https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170. Then, retry installation.

2. Open benchmark.ipynb, give a name in the first line of the code for the output excel file minutes later.
3. Run all codes and send me back the output excel file 
