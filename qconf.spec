Summary:        Allows you to have a nice configure script for your qmake-based project
Name:           qconf
Version:        1.4
Release:        3%{?dist}

Group:          Development/Tools
License:        GPL
URL:            http://delta.affinix.com/qconf/
Source0:        http://delta.affinix.com/download/qconf-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires:  qt-devel >= 4.4.0


%description
QConf allows you to have a nice configure script for your
qmake-based project. It is intended for developers who don't need
(or want) to use the more complex GNU autotools. With qconf/qmake,
it is easy to maintain a cross-platform project that uses a
familiar configuration interface on unix.


%prep
%setup -q


%build
./configure --prefix=%{_prefix} \
            --bindir=%{_bindir} \
            --datadir=%{_datadir} \
            --qtdir=%{_libdir}/qt4
make


%install
%{__rm} -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root)
%doc COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Sat Mar 19 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.4-3
- rebuilt

* Fri Dec 31 2010 Alexei Panov <elemc@atisserv.ru> - 1.4-2
- fix build requires

* Thu Nov 12 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 1.4-1
- initial build for Fedora
