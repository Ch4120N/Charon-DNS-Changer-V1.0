#!/bin/bash

# Make Deb Package for Zphisher (^.^)
_PACKAGE=Charon-DNS-Changer
_VERSION=2.4.1
_ARCH="all"
PKG_NAME="${_PACKAGE}_${_VERSION}_${_ARCH}.deb"

if [[ ! -e "scripts/launch.sh" ]]; then
        echo "lauch.sh should be in the \`scripts\` Directory. Exiting..."
        exit 1
fi

if [[ ${1,,} == "termux" || $(uname -o) == *'Android'* ]];then
        _depend="ncurses-utils, proot, resolv-conf, "
        _bin_dir="data/data/com.termux/files/"
        _opt_dir="data/data/com.termux/files/usr/"
        #PKG_NAME=${_PACKAGE}_${_VERSION}_${_ARCH}_termux.deb
fi

_depend+="python3-full, python3-pip, python3-colorama"
_bin_dir+="usr/bin"
_opt_dir+="opt/${_PACKAGE}"

if [[ -d "build_env" ]]; then rm -fr build_env; fi
mkdir -p build_env
mkdir -p ./build_env/${_bin_dir} ./build_env/$_opt_dir ./build_env/DEBIAN 

cat <<- CONTROL_EOF > ./build_env/DEBIAN/control
Package: ${_PACKAGE}
Version: ${_VERSION}
Architecture: ${_ARCH}
Maintainer: @Ch4120N
Depends: ${_depend}
Homepage: https://github.com/Ch4120N/Charon-DNS-Changer-V1.0
Description: Changing DNS very easy with type a number.
CONTROL_EOF

cat <<- PRERM_EOF > ./build_env/DEBIAN/prerm
#!/bin/bash
rm -fr $_opt_dir
exit 0
PRERM_EOF

chmod 755 ./build_env/DEBIAN
chmod 755 ./build_env/DEBIAN/{control,prerm}
cp -fr scripts/launch.sh ./build_env/$_bin_dir/$_PACKAGE
chmod 755 ./build_env/$_bin_dir/$_PACKAGE
cp -fr .imgs/ log/ modules/ LICENCE README.md chdnschanger.py requirements.txt Settings.json ./build_env/$_opt_dir
dpkg-deb --build ./build_env ${PKG_NAME}
rm -fr ./build_env