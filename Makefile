_default:
	@echo "make"
sources:
	@echo "make sources"
	@tar cvf - conf | xz > fermilab-conf_screenlock.tar.xz
srpm: sources
	@echo "make srpm"
	rpmbuild -bs --define '_sourcedir .' --define '_srcrpmdir .' fermilab-conf_screenlock.spec
