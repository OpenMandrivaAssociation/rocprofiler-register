Name:		rocprofiler-register
Version:	10.0.0
Release:	2
# Upstream library version
%global libver 0.6.0
Summary:	Helper library for modifying API tables of the ROCprofiler library
License:	MIT
Group:		System/Libraries
URL:		https://github.com/ROCm/rocprofiler-register
Source0:	https://github.com/ROCm/rocm-systems/releases/download/therock-10.0/rocprofiler-register.tar.gz#/rocprofiler-register-%{version}.tar.gz

BuildRequires:	rocm-rpm-macros
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(fmt)
BuildRequires:	cmake(glog)
# ng-log provides glog::glog for compatibility
BuildRequires:	lib64ng-log-devel
BuildRequires:	lib64fmt-devel
BuildRequires:	stdc++-static-devel
BuildRequires:	git-core

%description
The rocprofiler-register library coordinates modification of the intercept
API table(s) of the HSA/HIP/ROCTx runtime libraries by ROCprofiler.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and CMake package for rocprofiler-register.

%prep
%autosetup -n rocprofiler-register -p1
# Upstream hardcodes lib/ (ROCm non-FHS); force multi-lib libdir
sed -i -e 's|set(CMAKE_INSTALL_LIBDIR "lib")|set(CMAKE_INSTALL_LIBDIR "%{_lib}")|' CMakeLists.txt

%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DROCPROFILER_REGISTER_BUILD_GLOG=OFF \
	-DROCPROFILER_REGISTER_BUILD_FMT=OFF \
	-DROCPROFILER_REGISTER_BUILD_TESTS=OFF \
	-DROCPROFILER_REGISTER_BUILD_SAMPLES=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%license LICENSE.md
%doc README.md
%exclude %{_docdir}/rocprofiler-register/LICENSE.md
%{_libdir}/librocprofiler-register.so.%{libver}
%{_libdir}/librocprofiler-register.so.0
%{_datadir}/modulefiles/rocprofiler-register/
%{_datadir}/rocprofiler-register/setup-env.sh
%exclude %{_datadir}/rocprofiler-register/tests

%files devel
%{_includedir}/rocprofiler-register/
%{_libdir}/librocprofiler-register.so
%{_libdir}/cmake/rocprofiler-register/
