%define lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)
%define lualibdir %{_libdir}/lua/%{lua_version}
%define luapkgdir %{_datadir}/lua/%{lua_version}
%define oname luafilesystem
%define tarname	1_8_0

Name:           lua-filesystem
Version:	1.8.0
Release:	3
Summary:        FileSystem Tool for the Lua language

Group:          Development/Other
License:        MIT
URL:            https://lunarmodules.github.io/luafilesystem/
Source0:	https://github.com/keplerproject/luafilesystem/archive/v%{tarname}.tar.gz
BuildRequires:  lua-devel
Requires:       lua

%description
LuaFileSystem offers a portable way to access the
underlying directory structure and file attributes.

%prep
%autosetup -n %{oname}-%{tarname}

%build
%ifarch %{ix86} znver1
%global optflags %{optflags} -fPIC
%endif

%setup_compile_flags
%make_build CFLAGS="%{optflags} -fPIC" CC=%{__cc}

%install
make install PREFIX=%{buildroot}/%{_prefix} LUA_LIBDIR=%{buildroot}/%{lualibdir} LUA_DIR=%{buildroot}/%{luapkgdir} SYS_BINDIR=%{buildroot}/%{_bindir} LUA_INTERPRETER=%{_bindir}/lua

%files
%doc doc/us/*
%doc README.md
%{lualibdir}/*
