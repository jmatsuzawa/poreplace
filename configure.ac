#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.68])
AC_INIT([poreplace], [0.1], [jmatsuzawa@src.gnome.org])
AC_CONFIG_SRCDIR([poreplace/main.py])

AM_INIT_AUTOMAKE

# Checks for programs.
AM_PATH_PYTHON(2.6)

dnl checks for python modules
tranlsate_toolkit_installed=`$PYTHON -c 'import translate.storage.po;print("OK")' 2>/dev/null`
if test "x$tranlsate_toolkit_installed" = "x"; then
  AC_MSG_ERROR([Could not find a python module of translate-toolkit])
else
  echo 'checking for translate-toolkit... found'
fi

AC_OUTPUT([
Makefile
bin/Makefile
bin/poreplace
poreplace/Makefile
data/Makefile
data/errata/Makefile
tests/Makefile
])
