# resamplr - Resample FLACs intelligently
# See LICENSE file for copyright and license details.

include config.mk

SRC = resamplr.py
OBJ = ${SRC:.py=}

all: resamplr

resamplr: $@
	@echo cp ${SRC} ${OBJ}
	@cp ${SRC} ${OBJ}

clean:
	@echo cleaning
	@rm -f resamplr ${OBJ} resamplr-${VERSION}.tar.gz

dist: clean
	@echo creating dist tarball
	@mkdir -p resamplr-${VERSION}
	@cp -R LICENSE Makefile README.md config.mk \
		resamplr.1 ${SRC} resamplr-${VERSION}
	@tar -cf resamplr-${VERSION}.tar resamplr-${VERSION}
	@gzip resamplr-${VERSION}.tar
	@rm -rf resamplr-${VERSION}

install: all
	@echo installing executable file to ${DESTDIR}${PREFIX}/bin
	@mkdir -p ${DESTDIR}${PREFIX}/bin
	@cp -f resamplr ${DESTDIR}${PREFIX}/bin
	@chmod 755 ${DESTDIR}${PREFIX}/bin/resamplr
	@echo installing manual page to ${DESTDIR}${MANPREFIX}/man1
	@mkdir -p ${DESTDIR}${MANPREFIX}/man1
	@sed "s/VERSION/${VERSION}/g" < resamplr.1 > ${DESTDIR}${MANPREFIX}/man1/resamplr.1
	@chmod 644 ${DESTDIR}${MANPREFIX}/man1/resamplr.1

uninstall:
	@echo removing executable file from ${DESTDIR}${PREFIX}/bin
	@rm -f ${DESTDIR}${PREFIX}/bin/resamplr
	@echo removing manual page from ${DESTDIR}${MANPREFIX}/man1
	@rm -f ${DESTDIR}${MANPREFIX}/man1/resamplr.1

.PHONY: all clean dist install uninstall
