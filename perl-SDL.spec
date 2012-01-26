%define	module	SDL
%define upstream_version 2.536

Name:		perl-SDL
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library
License:	LGPLv2.1+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/~kthakore/%{module}-%{upstream_version}.tar.gz

BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_mixer-devel
BuildRequires:	libSDL_net-devel
BuildRequires:	libSDL_ttf-devel
BuildRequires:	libSDL_gfx-devel >= 2.0.8
BuildRequires:	libSDL_Pango-devel
BuildRequires:	libungif-devel
BuildRequires:	mesaglu-devel
BuildRequires:	perl(Alien::SDL)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(PDL)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Tie::Simple)
BuildRequires:	perl(YAML)
BuildRequires:	perl-devel

%description
SDL Perl is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -q -n %{module}-%{upstream_version}
# this test requires a sound device
rm -f t/mixerpm.t

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install  destdir=%{buildroot}

%files
%doc README INSTALL CHANGELOG TODO META.yml
%{_mandir}/*/*
%{perl_vendorarch}/SDL*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/pods/*
%{perl_vendorarch}/Module/Build/SDL.pm
