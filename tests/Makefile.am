tests = \
	test_pounit.py

EXTRA_DIST = $(tests)

check-local: test
test:
	@for testcase in $(tests) ; do \
	  PYTHONPATH=$(top_srcdir)/poreplace:$(PYTHONPATH) $(PYTHON) $${testcase}; \
	done
