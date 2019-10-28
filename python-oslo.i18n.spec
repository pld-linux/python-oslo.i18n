#
# Conditional build:
%bcond_with	doc	# build doc (broken)
%bcond_with	tests	# do perform "make test" (broken)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo i18n library
Name:		python-oslo.i18n
Version:	3.17.0
Release:	3
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.i18n/oslo.i18n-%{version}.tar.gz
# Source0-md5:	5750633d9105a972554ea9aeb9662ef0
URL:		https://pypi.python.org/pypi/oslo.i18n
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-babel >= 2.3.4
Requires:	python-pbr >= 2.0.0
Requires:	python-six >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oslo.i18n library contain utilities for working with
internationalization (i18n) features, especially translation for text
strings in an application or library.

%package -n python3-oslo.i18n
Summary:	Oslo i18n library
Group:		Libraries/Python
Requires:	python3-babel >= 2.3.4
Requires:	python3-pbr >= 2.0.0
Requires:	python3-six >= 1.9.0

%description -n python3-oslo.i18n
The oslo.i18n library contain utilities for working with
internationalization (i18n) features, especially translation for text
strings in an application or library.

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
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
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
%doc doc/_build/html/*
%endif
