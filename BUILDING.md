Building Truchas
------------------------------------------------------------------------------
### Quick Start Guide

#### Requirements
The Truchas build system assumes a UNIX-like environment. Current development
and testing is done on 64-bit Linux and Cray CLE platforms.
* Fortran and C/C++ compilers.  The compiler executables must be in your path.
  The following compilers are supported.
  - Intel Fortran and C/C++. Versions 15.0.2 and later, 16.0.2 and later.
  - NAG Fortran 6.0, builds 1067 and 1071, with GNU C/C++

  GFortran is not currently supported due to incomplete and/or flawed support
  for some Fortran 2003 features.
* Cmake version 3.5 or later; but not 3.6.0 and 3.6.1.
* Standard software development tools: make, patch, perl
* Python, versions 2.5, 2.6, or 2.7, including the development libraries
* NumPy
* MPI, if building a parallel executable.  The C compiler wrapper (`mpicc`,
  for example) must be in your path.

Truchas requires some additional libraries, but these can be built by the
third party library build step described below.

#### First Time Users
First time users may find it easiest to use one or more of the build scripts
located in the `scripts` directory.  These scripts are simple-to-use drivers
for the compilation procedure described below.
See [scripts/README.md](./scripts/README.md) for usage instructions.

#### Compiling
Compiling Truchas for the first time is usually a two-stage process.  The
first stage involves building and installing additional third party libraries
(TPL) that Truchas requires and which are not present on your system.  This
only needs to be done once.  A cmake superbuild project for this stage can be
found in the `tpl` subdirectory.  See [tpl/README.md](./tpl/README.md) for
instructions.

Once the required TPLs are installed, the procedure for building Truchas is
straightforward. You create a build directory, run cmake from that directory,
and then run make. What you choose for a build directory is irrelevant (other
than it must be different than the current directory). Here is an example:

    $ mkdir build
    $ cd build
    $ cmake -C ../config/intel-parallel-opt.cmake \
            -D TRUCHAS_TPL_DIR=<truchas_tpl_dir> ..
    $ make
    $ make install

* The `-C` argument pre-loads the cmake cache with settings from the following
  file. The `config` subdirectory contains some examples. If none of those are
  suitable, create your own, or simply define the various variables directly
  on the cmake command line (using the `-D` flag).
* Set the `TRUCHAS_TPL_DIR` variable to the TPL installation directory you
  used in the first stage. It must be an absolute path.
* By default Truchas will be installed into the `install` subdirectory of the
  top-level source directory. Use the `-D CMAKE_INSTALL_PREFIX=<truchas_dir>`
  cmake argument to specify a different directory.

#### Testing
From the build directory run the command

    $ ctest

to run the regression test suite. On multi-core systems use the `-j<n>` option
to tell ctest how many processes it can run simultaneously; `-j8`, for example.
All tests should pass.