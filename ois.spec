# TODO:
# - pl descryptions
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define _rc	RC1
Summary:	Object Oriented Input System
Name:		ois
Version:	1.0
Release:	0.%{_rc}.1
License:	zlib/libpng
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/wgois/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	05cbd131fb0477e1cbd4b115ccef2c90
URL:		http://www.wreckedgames.com/wiki/index.php/WreckedLibs:OIS
BuildRequires:	autoconf >= 2.5.0
BuildRequires:	automake >= 1.6
BuildRequires:	libtool >= 2:1.4
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of OIS is shield the application programmer from having to rewrite input systems from scratch for each project.

%package devel
Summary:	Header files for ois library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for ois library.

%package static
Summary:	Static ois library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ois library.

%prep
%setup -q -n %{name}-%{version}%{_rc}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*-*.*.*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOIS.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
