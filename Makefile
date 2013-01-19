SUBDIRS = $(shell ls -d 0*)

clean:
	@for I in $(SUBDIRS); do \
		[ -f $$I/Makefile ] && $(MAKE) -C $$I clean; \
	done
