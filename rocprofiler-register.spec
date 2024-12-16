Name:		rocprofiler-register
Version:	6.3.0
Release:	1
Source0:	rocprofiler-register-%{version}.tar.xz
Summary:	Helper library for modifying API tables of the ROCprofiler library
URL:		https://github.com/ROCm/rocprofiler-register
License:	MIT
Group:		Development/Tools
BuildRequires:	cmake
BuildSystem:	cmake

%patchlist
rocprofiler-register-lib64.patch

%description
The rocprofiler-register library is a helper library that coordinates the
modification of the intercept API table(s) of the HSA/HIP/ROCTx runtime
libraries by the ROCprofiler (v2) library. The purpose of this library is to
provide a consistent and automated mechanism of enabling performance analysis
in the ROCm runtimes which does not rely on environment variables or unique
methods for each runtime library.

When a runtime is initialized (either explicitly and lazily) and the intercept
API table is constructed, it passes this API table to rocprofiler-register.
Rocprofiler-register scans the symbols in the address space and if it detects
there is at least one visible symbol named rocprofiler_configure (which is a
function provided by tools), it passes the intercept API table to the
rocprofiler library (dlopening the rocprofiler library if it is not already
loaded). The rocprofiler library then does an extensive scan for all the
instances of the rocprofiler_configure symbols and invokes each of them.
The rocprofiler_configure function (again, provided by a tool) returns
effectively tells rocprofiler which behaviors it wants to be notified about,
features it wants to use (e.g. API tracing, kernel dispatch timing), etc.

%prep
%autosetup -p1 -n %{name}-rocm-%{version}
git init

%files
%{_includedir}/rocprofiler-register
%{_libdir}/cmake/rocprofiler-register
%{_libdir}/librocprofiler-register.so*
%doc %{_docdir}/rocprofiler-register
%{_datadir}/modulefiles
%{_datadir}/rocprofiler-register
