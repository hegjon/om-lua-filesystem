%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luafilesystem

Name:           lua-filesystem
Version:        1.4.2
Release:        4
Summary:        FileSystem Tool for the Lua language

Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/luafilesystem/
Source0:        http://luaforge.net/frs/download.php/3931/%{oname}-%{version}.tar.gz
BuildRequires:  lua-devel >= %{luaver}
Requires:       lua >= %{luaver}

%description
LuaFileSystem offers a portable way to access the
underlying directory structure and file attributes.

%prep
%setup -q -n %{oname}-%{version}

%build
%setup_compile_flags
%make CFLAGS="%{optflags}"

%install
make install PREFIX=%{buildroot}/%{_prefix} LUA_LIBDIR=%{buildroot}/%{lualibdir} LUA_DIR=%{buildroot}/%{luapkgdir} SYS_BINDIR=%{buildroot}/%{_bindir} LUA_INTERPRETER=%{_bindir}/lua

%files
%doc doc/us/*
%doc README
%{lualibdir}/*
