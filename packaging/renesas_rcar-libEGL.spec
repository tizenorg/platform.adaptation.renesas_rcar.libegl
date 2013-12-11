Name:           renesas_rcar-libEGL
Version:        1.0.0
Release:	0
License:	Apache-2.0
Summary:	libegl library
Source:       %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
ExclusiveArch:  armv7l
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libkms)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm) >= 2.4.24
BuildRequires:  pkgconfig(libudev) > 150
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-kms)
BuildRequires:  pkgconfig(wayland-egl)

%description
libEGL library for use on Renesas R-Car platform

%package devel
Summary:    libegl library (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
libEGL development files for Renesas R-Car platform

%prep
%setup

%build
autoreconf -vif
%configure
make

%install
%make_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libEGL.so*

%files devel
%exclude %{_libdir}/pkgconfig/egl.pc
%exclude %{_libdir}/pkgconfig/glesv2.pc
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglmesaext.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/GLES2/gl2platform.h
%{_includedir}/KHR/khrplatform.h
