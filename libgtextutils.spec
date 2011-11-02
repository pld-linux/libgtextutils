#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Gordon's text-utility classes
#Summary(pl.UTF-8):	-
Name:		libgtextutils
Version:	0.6
Release:	1
License:	AGPL v3
Group:		Libraries
Source0:	http://hannonlab.cshl.edu/fastx_toolkit/%{name}-%{version}.tar.bz2
# Source0-md5:	d6969aa0d31cc934e1fedf3fe3d0dc63
URL:		http://hannonlab.cshl.edu/fastx_toolkit/index.html
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gordon's text-utility classes.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for libgtextutils library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgtextutils
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgtextutils library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgtextutils.

%package static
Summary:	Static libgtextutils library
Summary(pl.UTF-8):	Statyczna biblioteka libgtextutils
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgtextutils library.

%description static -l pl.UTF-8
Statyczna biblioteka libgtextutils.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--disable-wall

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove .la pollution
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README THANKS
%attr(755,root,root) %{_libdir}/libgtextutils-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtextutils-0.6.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtextutils.so
%{_includedir}/gtextutils
%{_pkgconfigdir}/gtextutils.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgtextutils.a
%endif
