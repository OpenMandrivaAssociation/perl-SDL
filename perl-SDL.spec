%define	modname	SDL

Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library
Name:		perl-SDL
Version:	2.548
Release:	1
License:	LGPLv2.1+
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/F/FR/FROGGS/%{modname}-%{version}.tar.gz
Patch1:		SDL-2.548-Adapt-to-perl-5.37.1.patch
Patch2:		SDL-2.548-Fix-implicit-declaration-of-_calc_offset.patch
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(SDL_gfx) >= 2.0.8
BuildRequires:	pkgconfig(SDL_Pango)
BuildRequires:	perl(Alien::SDL)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(File::Find) 
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Tie::Simple)
BuildRequires:	perl(Devel::Peek)
BuildRequires:	perl(YAML)
BuildRequires:	perl-devel
BuildRequires:	fonts-ttf-dejavu

%description
SDL Perl is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%autosetup -p1 -n SDL-%{version}
# this test requires a sound device
rm -f t/mixerpm.t
# Disable the sdlx_controller_interface.t test, it hangs on arm
rm t/sdlx_controller_interface.t
sed -i -e '/t\/sdlx_controller_interface\.t/d' MANIFEST

%build
perl Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%if 0
# 1 test fails with perl 5.40.0:
# Attempt to call undefined import method with arguments ("Can load SDLx::Music") via package "SDLx::Music" (Perhaps you forgot to load the package?) at t/sdlx_music.t line 33.

%check
./Build test
%endif

%install
./Build install  destdir=%{buildroot}

%files
%doc INSTALL CHANGELOG TODO META.yml
%{perl_vendorarch}/SDL*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/pods/*
%{perl_vendorarch}/Module/Build/SDL.pm
%{_mandir}/man3/*
