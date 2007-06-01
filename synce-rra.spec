%define name     synce-rra
%define shortname rra
%define release  %mkrel 1
%define version  0.10.0

%define major 0

%define libname %mklibname %shortname %major

Summary: SynCE: Communication application
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: System/Libraries
Source: %{name}-%{version}.tar.bz2
Patch0: synce-unused_var.patch
Patch1: synce-rra-fix-build.patch
URL: http://synce.sourceforge.net/
Buildroot: %{_tmppath}/%name-root
BuildRequires: libsynce-devel >= %{version}
BuildRequires: libmimedir-devel
BuildRequires: librapi-devel >= %{version}
BuildRequires: automake
BuildRequires: python-devel
BuildRequries: python-pyrex

%description
%{shortname} is part of the SynCE project:

%package -n %libname
Group: System/Libraries
Summary: SynCE: Communication application
Provides: lib%{shortname} = %{version}-%{release}
Conflicts: %{_lib}synce0 < 0.9.3

%description -n %libname
%{shortname} is part of the SynCE project

%package -n %libname-python
Group: System/Libraries
Summary: SynCE: Communication application
Provides: lib%{shortname}-python = %{version}-%{release}
Provides: %{shortname}-python = %{version}-%{release}

%description -n %libname-python
%{shortname} is part of the SynCE project

%package -n %libname-devel
Group: System/Libraries
Summary: SynCE: Communication application
Provides: lib%{shortname}-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Conflicts: %{_lib}synce0-devel < 0.9.3

%description -n %libname-devel
%{shortname} is part of the SynCE project

%prep
%setup -q
%patch0 -p1 -b .unused-var
#%patch1 -p1 -b .fix-build

perl -pi -e 's/-Werror//' lib/Makefile.in

%build
%configure --with-libsynce=%{_prefix} --includedir=%{_includedir}/rra
%make includedir=%{buildroot}%{_includedir}/rra

%install
%makeinstall includedir=%{buildroot}%{_includedir}/rra

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man?/*

%files -n %{libname}
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_includedir/rra
%_libdir/pkgconfig/librra.pc

%files -n %{libname}-python
%python_sitearch/pyrra.*
