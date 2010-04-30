%define upstream_name    SDL_Perl
%define upstream_version v2.2.6

Name:       perl-SDL
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3
Epoch:      1

Summary:    Wrapper around the cross platform Simple DirectMedia Layer game library
License:    LGPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/~dgoehrig/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: libSDL_image-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libSDL_net-devel
BuildRequires: libSDL_ttf-devel
BuildRequires: libSDL_gfx-devel >= 2.0.8
BuildRequires: libungif-devel
BuildRequires: mesaglu-devel
BuildRequires: perl(Module::Build)
BuildRequires: perl(PDL)
BuildRequires: perl(YAML)
BuildRequires: perl-devel

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
SDL Perl is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%doc README BUGS TODO 
%{_mandir}/*/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/SDL*
