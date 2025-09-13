#!/bin/bash

# Make Deb Package for Charon-DNS-Changer (^.^)

_PACKAGE="Charon-DNS-Changer"
_DIR="Charon-DNS-Changer"
_VERSION="1.1"
_ARCH="all"
PKG_NAME="${_PACKAGE}_${_VERSION}_${_ARCH}.deb"

# Check if launch.sh exists
if [[ ! -e "scripts/launch.sh" ]]; then
    echo "launch.sh should be in the \`scripts\` directory. Exiting..."
    exit 1
fi

# Termux-specific adjustments
if [[ "${1,,}" == "termux" || $(uname -o 2>/dev/null) == *'Android'* ]]; then
    _depend="ncurses-utils, proot, resolv-conf, "
    _bin_dir="data/data/com.termux/files/usr/bin"
    _opt_dir="data/data/com.termux/files/usr/opt/${_DIR}"
    # PKG_NAME="${_PACKAGE}_${_VERSION}_${_ARCH}_termux.deb"
else
    _bin_dir="usr/bin"
    _opt_dir="opt/${_DIR}"
fi

# Common dependencies
_depend+="python3, python3-pip, python3-colorama"

# Prepare build environment
if [[ -d "build_env" ]]; then rm -rf build_env; fi
mkdir -p "build_env/${_bin_dir}" "build_env/${_opt_dir}" "build_env/DEBIAN"

# Create DEBIAN/control file
cat << CONTROL_EOF > build_env/DEBIAN/control
Package: ${_DIR}
Version: ${_VERSION}
Architecture: ${_ARCH}
Maintainer: @Ch4120N
Depends: ${_depend}
Homepage: https://github.com/Ch4120N/Charon-DNS-Changer
Description: Easily change DNS by typing a number.
CONTROL_EOF

# Create DEBIAN/prerm file
cat << PRERM_EOF > build_env/DEBIAN/prerm
#!/bin/bash
rm -rf ${_opt_dir}
exit 0
PRERM_EOF

# Set permissions
chmod 755 build_env/DEBIAN/prerm
chmod 644 build_env/DEBIAN/control

# Copy launcher script
cp -f scripts/launch.sh "build_env/${_bin_dir}/ChDNSChanger"
chmod 755 "build_env/${_bin_dir}/ChDNSChanger"

# Copy program files
cp -fr images/ modules/ LICENCE README.md ChDNSChanger.py requirements.txt "build_env/${_opt_dir}"

# Build the .deb package
dpkg-deb --build build_env "${PKG_NAME}"

# Cleanup
rm -rf build_env

echo "[ + ] Package ${PKG_NAME} created successfully!"
