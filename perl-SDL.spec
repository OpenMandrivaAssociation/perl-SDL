%define real_name SDL_Perl
%define name perl-SDL
%define version 2.1.3
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Wrapper around the cross platform Simple DirectMedia Layer game library
License:    LGPL
Group:      Development/Perl
URL:        http://www.sdlperl.org/
Source:     http://sdlperl.org/downloads/%{real_name}-%{version}.tar.gz
# stolen from gentoo
Patch0:     perl-SDL-2.1.3-build.patch
Patch1:     perl-SDL-2.1.3-gfxPie.patch
BuildRequires: perl-devel
BuildRequires: perl(Module::Build)
BuildRequires: perl-PDL 
BuildRequires: mesaglu-devel
BuildRequires: libungif-devel
BuildRequires: libSDL_image-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libSDL_net-devel
BuildRequires: libSDL_ttf-devel
BuildRequires: libSDL_gfx-devel >= 2.0.8
Buildroot: %{_tmppath}/%{name}-%{version}

%description
SDL Perl is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -q -n %{real_name}-%{version}
%patch0 -p1
%patch1 -p0
# this test requires a sound device
rm -f t/mixerpm.t

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install  destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README BUGS TODO test
%{_mandir}/*/*
%{perl_vendorarch}/auto/SDL*
%{perl_vendorarch}/SDL*


