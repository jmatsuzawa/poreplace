ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}

SUBDIRS = \
	bin\
	data\
	poreplace\
	tests

check-local: test
test:
	cd tests; make test
