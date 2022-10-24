#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-flake8_class_newline
Version  : 1.6.0
Release  : 39
URL      : https://files.pythonhosted.org/packages/17/f3/d93a95971801e0bd28539e7727e90553217ea76d48098ea02d10832f609f/flake8-class-newline-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/f3/d93a95971801e0bd28539e7727e90553217ea76d48098ea02d10832f609f/flake8-class-newline-1.6.0.tar.gz
Summary  : Flake8 lint for newline after class definitions.
Group    : Development/Tools
License  : MIT
Requires: pypi-flake8_class_newline-license = %{version}-%{release}
Requires: pypi-flake8_class_newline-python = %{version}-%{release}
Requires: pypi-flake8_class_newline-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flake8)

%description
===========================================

%package license
Summary: license components for the pypi-flake8_class_newline package.
Group: Default

%description license
license components for the pypi-flake8_class_newline package.


%package python
Summary: python components for the pypi-flake8_class_newline package.
Group: Default
Requires: pypi-flake8_class_newline-python3 = %{version}-%{release}

%description python
python components for the pypi-flake8_class_newline package.


%package python3
Summary: python3 components for the pypi-flake8_class_newline package.
Group: Default
Requires: python3-core
Provides: pypi(flake8_class_newline)
Requires: pypi(flake8)

%description python3
python3 components for the pypi-flake8_class_newline package.


%prep
%setup -q -n flake8-class-newline-1.6.0
cd %{_builddir}/flake8-class-newline-1.6.0
pushd ..
cp -a flake8-class-newline-1.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656405004
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-flake8_class_newline
cp %{_builddir}/flake8-class-newline-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-flake8_class_newline/8aec8ab776c95f72ec18b58a7a68c81d4ddc8408
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-flake8_class_newline/8aec8ab776c95f72ec18b58a7a68c81d4ddc8408

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
