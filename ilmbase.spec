
Name:	 ilmbase 
Version: 1.0.1
Release: 6.1%{?dist}
Summary: Abstraction/convenience libraries

Group:	 System Environment/Libraries
License: BSD
URL:	 http://www.openexr.com/
Source0: http://download.savannah.nongnu.org/releases/openexr/ilmbase-%{version}.tar.gz
Source1: http://download.savannah.nongnu.org/releases/openexr/ilmbase-%{version}.tar.gz.sig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: automake libtool
BuildRequires: pkgconfig

# undefined pthread symbols
Patch1: ilmbase-1.0.0-no_undefined.patch
# move pthread linkage to Libs.private, tho probably not needed
# if already using patch1 above.
Patch2: ilmbase-1.0.0-pkgconfig.patch

%description
Half is a class that encapsulates the ilm 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package devel
Summary: Headers and libraries for building apps that use %{name} 
Group:	 Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libGL-devel libGLU-devel
Requires: pkgconfig
%description devel
%{summary}.


%prep
%setup -q

%patch1 -p1 -b .no_undefined
%patch2 -p1 -b .pkgconfig

# for patch1
./bootstrap


%build
%configure --disable-static

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm -f  $RPM_BUILD_ROOT%{_libdir}/lib*.la


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/OpenEXR/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.1-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May  4 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.0.1-5
- Fix spelling error in summary.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-3
- rebuild for pkgconfig deps

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-2
- respin (gcc43)

* Mon Jan 07 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.1-1
- ilmbase-1.0.1

* Fri Oct 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.0-3
- include *.tar.sig in sources

* Mon Oct 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.0-2
- update %%summary
- -devel: +Requires: libGL-devel libGLU-devel
- make install ... INSTALL="install -p" to preserve timestamps


* Thu Aug 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.0-1
- ilmbase-1.0.0 (first try)

