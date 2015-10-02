#/bin/sh

lcov -c -d . -o a.info
genhtml -o covhtml a.info
