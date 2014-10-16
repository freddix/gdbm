Summary:	GNU database library for C
Name:		gdbm
Version:	1.11
Release:	3
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/gdbm/%{name}-%{version}.tar.gz
# Source0-md5:	72c832680cf0999caedbe5b265c8c1bd
Patch0:		%{name}-zeroheaders.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdbm is a GNU database indexing library, including routines which use
extensible hashing. gdbm works in a similar way to standard UNIX dbm
routines. gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

%package devel
Summary:	development libraries and header files for gdbm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
These are the development libraries and header files for gdbm, the GNU
database system. These are required if you plan to do development
using the gdbm database.

%prep
%setup  -q
# https://bugzilla.redhat.com/show_bug.cgi?id=4457
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-libgdbm-compat
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gdbm_dump
%attr(755,root,root) %{_bindir}/gdbm_load
%attr(755,root,root) %{_bindir}/gdbmtool
%attr(755,root,root) %ghost %{_libdir}/libgdbm.so.?
%attr(755,root,root) %ghost %{_libdir}/libgdbm_compat.so.?
%attr(755,root,root) %{_libdir}/libgdbm.so.*.*.*
%attr(755,root,root) %{_libdir}/libgdbm_compat.so.*.*.*
%{_mandir}/man1/gdbm_dump.1*
%{_mandir}/man1/gdbm_load.1*
%{_mandir}/man1/gdbmtool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdbm.so
%attr(755,root,root) %{_libdir}/libgdbm_compat.so
%{_libdir}/libgdbm.la
%{_libdir}/libgdbm_compat.la
%{_mandir}/man3/*
%{_includedir}/*
%{_infodir}/gdbm*

