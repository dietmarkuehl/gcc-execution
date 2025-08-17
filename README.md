# GCC Execution

Organise the implementation of
[`std::execution`](https://eel.is/c++draft/exec) for libstdc++.
The actual implementation will reside in the [gcc](git://gcc.gnu.org/git/gcc.git) repository and applied via the normal
means for the gcc implementation.

The file [`dependency-order.txt`](dependency-order.txt) contains a
list of components in dependency order from least dependent to most
dependent. The list is currently produced automatically based on
the header files in [beman.execution](https://github.com/beman.execution)
and contains some artifacts.
