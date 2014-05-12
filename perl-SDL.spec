%define	modname	SDL
%define modver 2.543.1

Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library


Name:		perl-SDL
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	1
License:	LGPLv2.1+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/F/FR/FROGGS/%{modname}-2.543_1.tar.gz

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
BuildRequires:	perl(PDL)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Tie::Simple)
BuildRequires:	perl(YAML)
BuildRequires:	perl-devel

%description
SDL Perl is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -qn SDL-2.543_1
# this test requires a sound device
rm -f t/mixerpm.t

%build
%__perl Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install  destdir=%{buildroot}

%files
%doc README INSTALL CHANGELOG TODO META.yml
%{perl_vendorarch}/SDL*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/pods/*
%{perl_vendorarch}/Module/Build/SDL.pm
%{_mandir}/man3/*



