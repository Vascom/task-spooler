Name:           task-spooler
Version:        1.0
Release:        1%{?dist}
Summary:        Personal job scheduler

License:        GPLv2+
URL:            http://vicerveza.homeunix.net/~viric/soft/ts
Source0:        %{url}/ts-%{version}.tar.gz

# BuildRequires:

%description
Task spooler is a Unix batch system where the tasks spooled run one
after the other. Each user in each system has his own job queue. The tasks are
run in the correct context (that of enqueue) from any shell/process, and its
output/results can be easily watched. It is very useful when you know that
your commands depend on a lot of RAM, a lot of disk use, give a lot of
output, or for whatever reason it's better not to run them at the same time.

%prep
%autosetup -n ts-%{version}
touch configure
chmod +x configure


%build
%configure
%make_build


%install
make PREFIX=%{buildroot}/usr install
mv %{buildroot}%{_bindir}/ts %{buildroot}%{_bindir}/tsp
mv %{buildroot}%{_mandir}/man1/ts.1 %{buildroot}%{_mandir}/man1/tsp.1


%files
%license COPYING
%doc Changelog README TRICKS PROTOCOL
%{_bindir}/tsp
%{_mandir}/man1/tsp.1.*


%changelog
* Tue Apr 17 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0-1
- Initial package for Fedora
