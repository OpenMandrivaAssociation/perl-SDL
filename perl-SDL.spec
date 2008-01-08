%define real_name SDL_perl
%define name perl-SDL
%define version 1.20.0
%define release %mkrel 16

Summary: Wrapper around the cross platform Simple DirectMedia Layer game library
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL
Group: Development/Perl
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot/
Source: http://sdlperl.org/downloads/%{real_name}-%{version}.tar.gz
Patch0: SDL_perl-1.20.0-64bit.patch
Patch1:	SDL_perl-1.20.0-SDL_gfx12.patch
URL: http://www.sdlperl.org/
BuildRequires: libungif-devel libSDL_image-devel
BuildRequires: libSDL_mixer-devel mesaglu-devel perl-devel perl-PDL 
BuildRequires: libSDL_net-devel libSDL_ttf-devel
BuildRequires: libSDL_gfx-devel >= 2.0.8
Provides: %{real_name} = %{version}-%{release} sdlpl = %{version}-%{release}

%description
SDL Perl is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -q -n %{real_name}-%{version}
%patch0 -p0
%patch1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BUGS TODO test
%{_mandir}/*/*
%{perl_vendorarch}/auto/SDL*
%{perl_vendorarch}/SDL*


