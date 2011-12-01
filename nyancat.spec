Name:		nyancat
Version:	0.1
Release:	1
Summary:	Nyancat rendered in your terminal
Group:		Toys
License:	NCSA
URL:		https://github.com/klange/nyancat
Source0:	https://nodeload.github.com/klange/nyancat/tarball/klange-nyancat-fbb9a73.tar.gz

BuildRequires:	python-devel

%description
Nyancat rendered in your terminal.

%prep
%setup -q -n klange-%{name}-fbb9a73

%build

%make

%install
mkdir -p %{buildroot}/%{_bindir}/
install -m 0755 src/%{name} %{buildroot}/%{_bindir}/%{name}
install -m 0755 src/%{name}.py %{buildroot}/%{_bindir}/%{name}.py
#telnetsrvlib.py /usr/lib/python2.7/site-packages/
mkdir -p %{buildroot}/%{python_sitelib}/
install -m 0644 src/telnetsrvlib.py %{buildroot}/%{python_sitelib}


%files
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{python_sitelib}/telnetsrvlib.py
