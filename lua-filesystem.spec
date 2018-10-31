%define luaver 5.2
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luafilesystem
%define tarname	1_6_2

Name:           lua-filesystem
Version:        1.6.2
Release:        5
Summary:        FileSystem Tool for the Lua language

Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/luafilesystem/
Source0:	https://github.com/keplerproject/luafilesystem/archive/v%{tarname}.tar.gz
BuildRequires:  lua-devel >= %{luaver}
Requires:       lua >= %{luaver}

%description
LuaFileSystem offers a portable way to access the
underlying directory structure and file attributes.

%prep
%setup -q -n %{oname}-%{tarname}

%build
%setup_compile_flags
%make CFLAGS="%{optflags}" CC=%{__cc}

%install
make install PREFIX=%{buildroot}/%{_prefix} LUA_LIBDIR=%{buildroot}/%{lualibdir} LUA_DIR=%{buildroot}/%{luapkgdir} SYS_BINDIR=%{buildroot}/%{_bindir} LUA_INTERPRETER=%{_bindir}/lua

%files
%doc doc/us/*
%doc README
%{lualibdir}/*
