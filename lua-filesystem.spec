%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luafilesystem

Name:           lua-filesystem
Version:        1.4.2
Release:        %mkrel 2
Summary:        FileSystem Tool for the Lua language

Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/luafilesystem/
Source0:        http://luaforge.net/frs/download.php/3931/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  lua-devel >= %{luaver}
Requires:       lua >= %{luaver}

%description
LuaFileSystem offers a portable way to access the
underlying directory structure and file attributes.

%prep
%setup -q -n %{oname}-%{version}

%build
%make

%install
rm -rf %{buildroot}
make install PREFIX=$RPM_BUILD_ROOT/%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT/%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT/%{luapkgdir} SYS_BINDIR=$RPM_BUILD_ROOT/%{_bindir} LUA_INTERPRETER=%{_bindir}/lua


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc doc/us/*
%doc README
%{lualibdir}/*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-2mdv2011.0
+ Revision: 612780
- the mass rebuild of 2010.1 packages

* Mon Feb 01 2010 Rémy Clouard <shikamaru@mandriva.org> 1.4.2-1mdv2010.1
+ Revision: 499354
- update to 1.4.2

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.4.1-2mdv2010.0
+ Revision: 439633
- rebuild

* Sun Dec 28 2008 Jérôme Soyer <saispo@mandriva.org> 1.4.1-1mdv2009.1
+ Revision: 320577
- import lua-filesystem


