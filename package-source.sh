#!/bin/sh
# The tarballs released upstream don't work -- they're missing the
# submodules
VERSION=$(cat *.spec |grep ^Version |cut -d: -f2- |xargs echo)
git clone --depth 1 -b rocm-${VERSION} https://github.com/ROCm/rocprofiler-register rocprofiler-register-rocm-${VERSION}
cd rocprofiler-register-rocm-${VERSION}
git submodule init
cd ..
tar cJf rocprofiler-register-${VERSION}.tar.xz rocprofiler-register-rocm-${VERSION}
