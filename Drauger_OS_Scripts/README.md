Scripts in here are used for developing Drauger OS.
If they help you with development for Drauger OS or another distro, let me know!

`build.sh` will build a *.deb file for a properly formatted directory current working directory.

`build-kernel` will build a Linux kernel, as well as providing a few other functions to help with kernel packaging.

`make-iso` does what it says on the tin...provided you only have 1 kernel installed in the `chroot` needed and it's in the correct place.

`total-dev-time` reads from a file and provides total development time. The file is written to by scripts which are not in this repo yet.

`update-package` includes a *.deb package into a `reprepro` repo