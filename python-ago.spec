%define	module	ago
#
Summary:	Makes customizable human readable timedeltas
Summary(pl.UTF-8):	Konfigurowalne, czytelne dla człowieka różnice czasu
Name:		python-ago
Version:	0.0.6
Release:	18
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ago/
Source0:	https://files.pythonhosted.org/packages/source/a/ago/ago-%{version}.tar.gz
# Source0-md5:	e2fdc21fb922b4fc21ec19c6eac6bd46
URL:		https://bitbucket.org/russellballestrini/ago/overview
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makes customizable human readable timedeltas.

%description -l pl.UTF-8
Konfigurowalne, czytelne dla człowieka różnice czasu.

%prep
%setup -q -n ago-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO README.rst
%{_examplesdir}/python-%{module}-%{version}
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/*egg-info
