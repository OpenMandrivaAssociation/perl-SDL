%define upstream_name    SDL
%define upstream_version 2.403

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Wrapper around the cross platform Simple DirectMedia Layer game library
License:    LGPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/~dgoehrig/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: libSDL-devel
BuildRequires: libSDL_Pango-devel
BuildRequires: libSDL_gfx-devel
BuildRequires: libSDL_image-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libSDL_net-devel
BuildRequires: libSDL_sound-devel
BuildRequires: libSDL_ttf-devel
BuildRequires: libungif-devel
BuildRequires: mesaglu-devel
BuildRequires: perl(Alien::SDL)
BuildRequires: perl(IO::CaptureOutput)
BuildRequires: perl(Module::Build)
BuildRequires: perl(PDL)
BuildRequires: perl(Test::Most)
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
SDL_AUDIODRIVER=dsp ./Build test

%install
rm -rf %{buildroot}
./Build install  destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO META.yml
%{_mandir}/*/*
%{perl_vendorarch}/SDL*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/pods/*
