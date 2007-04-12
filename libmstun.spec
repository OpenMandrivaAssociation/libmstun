%define name	libmstun
%define oname	mstun
%define version 0.5.0
%define cvs	20061210
%define release %mkrel 0.%cvs.1

%define major	0
%define libname %mklibname %oname %major

Name: 	 	%{name}
Summary: 	Stun library from MiniSip
Version: 	%{version}
Release: 	%{release}

Source:		http://www.minisip.org/source/%{name}-%{version}-%{cvs}.tar.bz2
URL:		http://www.minisip.org/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libmutil-devel >= 0.3.1-0.20061210.0
BuildRequires:	libmcrypto-devel >= 0.3.1-0.20061210.0
BuildRequires:	libmnetutil-devel >= 0.3.1-0.20061210.0

%description
The 'libmstun' package provides classes that implement the STUN client,
as used by libminisip.  In the future, this package should contain both
client and server STUN implementations, which will be used by 'ministun'
to provide a re-usable CLI and daemon applications.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
#Provides:	%name
#Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name

%build
./bootstrap
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

