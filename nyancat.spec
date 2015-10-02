%define debug_package %nil

Name:		nyancat
Version:	1.2.1
Release:	1
Summary:	Nyancat rendered in your terminal
Group:		Toys
License:	NCSA
URL:		https://github.com/klange/nyancat
Source0:	https://github.com/klange/nyancat/archive/%{name}-%{version}.tar.gz

BuildRequires:	python-devel

%description
Nyancat rendered in your terminal.

%prep
%setup -q

%build
%make LFLAGS="%{ldflags} %{optflags}" CC=%{__cc}

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0755 src/%{name} %{buildroot}/%{_bindir}/%{name}
install -m 0644 nyancat.1 %{buildroot}/%{_mandir}/man1/

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
