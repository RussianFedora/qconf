Summary:        Allows you to have a nice configure script for your qmake-based project
Name:           qconf
Version:        1.4
Release:        1%{?dist}

Group:          Development/Tools
License:        GPL
URL:            http://delta.affinix.com/qconf/
Source0:        http://delta.affinix.com/download/qconf-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires:  qt-devel


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
* Thu Nov 12 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 1.4-1
- initial build for Fedora
