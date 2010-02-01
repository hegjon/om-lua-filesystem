%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luafilesystem

Name:           lua-filesystem
Version:        1.4.2
Release:        %mkrel 1
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
