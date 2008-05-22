#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Object Oriented Input System
Summary(pl.UTF-8):	Zorientowany obiektowo system wejścia
Name:		ois
Version:	1.2.0
Release:	0.1
License:	zlib/libpng
Group:		Libraries
Source0:	http://dl.sourceforge.net/wgois/%{name}_%{version}.tar.gz
# Source0-md5:	6a8cedad04f095127ca1455162fec955
URL:		http://www.wreckedgames.com/wiki/index.php/WreckedLibs:OIS
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4
BuildRequires:	xorg-lib-libXaw-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of OIS is shield the application programmer from having to
rewrite input systems from scratch for each project.

%description -l pl.UTF-8
Celem projektu OIS jest ochrona twórcy aplikacji przed przepisywaniem
na nowo systemów wejścia w każdym projekcie.

%package devel
Summary:	Header files for OIS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OIS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	xorg-lib-libXaw-devel

%description devel
Header files for OIS library.

%description -l pl.UTF-8
Pliki nagłówkowe biblioteki OIS.

%package static
Summary:	Static OIS library
Summary(pl.UTF-8):	Statyczna biblioteka OIS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OIS library.

%description -l pl.UTF-8
Statyczna biblioteka OIS.

%prep
%setup -q -n %{name}

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
%attr(755,root,root) %{_libdir}/libOIS-*.*.*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOIS.so
%{_libdir}/libOIS.la
%{_includedir}/OIS
%{_pkgconfigdir}/OIS.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libOIS.a
%endif
