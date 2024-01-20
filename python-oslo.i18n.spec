#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo i18n library
Summary(pl.UTF-8):	Biblioteka Oslo i18n
Name:		python-oslo.i18n
# keep 3.x for python2 support
Version:	3.25.1
Release:	1
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.i18n/oslo.i18n-%{version}.tar.gz
# Source0-md5:	82e01af1ce6aecfdece62ac5c0dd650a
URL:		https://pypi.org/project/oslo.i18n
%if %{with python2}
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-babel >= 2.5.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	python-testscenarios >= 0.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-babel >= 2.5.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-testscenarios >= 0.4
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	sphinx-pdg-2 >= 1.8.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oslo.i18n library contain utilities for working with
internationalization (i18n) features, especially translation for text
strings in an application or library.

%description -l pl.UTF-8
Biblioteka oslo.i18n zawiera narzędzia do pracy z funkcjonalnością
umiędzynarodowienia (internationalization - i18n), w szczególności
tłumaczenia łańcuchów tekstowych w aplikachach lub bibliotekach.

%package -n python3-oslo.i18n
Summary:	Oslo i18n library
Summary(pl.UTF-8):	Biblioteka Oslo i18n
Group:		Libraries/Python

%description -n python3-oslo.i18n
The oslo.i18n library contain utilities for working with
internationalization (i18n) features, especially translation for text
strings in an application or library.

%description -n python3-oslo.i18n -l pl.UTF-8
Biblioteka oslo.i18n zawiera narzędzia do pracy z funkcjonalnością
umiędzynarodowienia (internationalization - i18n), w szczególności
tłumaczenia łańcuchów tekstowych w aplikachach lub bibliotekach.

%package apidocs
Summary:	API documentation for Python oslo.i18n module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.i18n
Group:		Documentation

%description apidocs
API documentation for Pythona oslo.i18n module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.i18n.

%prep
%setup -q -n oslo.i18n-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/oslo_i18n/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/oslo_i18n/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/oslo_i18n
%{py_sitescriptdir}/oslo.i18n-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oslo.i18n
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslo_i18n
%{py3_sitescriptdir}/oslo.i18n-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,reference,user,*.html,*.js}
%endif
