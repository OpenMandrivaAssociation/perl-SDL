%define	module	SDL
%define upstream_version 2.536

Name:		perl-SDL
Version:	%perl_convert_version %{upstream_version}
Release:	5
Epoch:		1

Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library
License:	LGPLv2.1+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/~kthakore/%{module}-%{upstream_version}.tar.gz

BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	SDL_net-devel
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(SDL_gfx) >= 2.0.8
BuildRequires:	pkgconfig(SDL_Pango)
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(glu)
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
%setup -q -n %{module}-%{upstream_version}
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
%{_mandir}/*/*
%{perl_vendorarch}/SDL*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/pods/*
%{perl_vendorarch}/Module/Build/SDL.pm


%changelog
* Fri Jan 27 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1:2.536.0-1
+ Revision: 769306
- use pkgconfig() dependencies for buildrequires
--Denne linjuse en og de som er under vil bli ignorert--
  M    SPECS/perl-SDL.spec
- clean up
- new version
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.533.0-1
+ Revision: 684824
- update to new version 2.533

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.532.0-2
+ Revision: 667302
- mass rebuild

* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.532.0-1
+ Revision: 649169
- update to new version 2.532

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.529.0-1
+ Revision: 635241
- update to new version 2.529

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.526.0-1mdv2011.0
+ Revision: 627298
- new version

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.524.0-1mdv2011.0
+ Revision: 612254
- update to new version 2.524

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.523.0-1mdv2011.0
+ Revision: 602389
- update to new version 2.523

* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:2.522.0-1mdv2011.0
+ Revision: 596647
- update to 2.522

* Sun Oct 24 2010 Shlomi Fish <shlomif@mandriva.org> 1:2.518.0-3mdv2011.0
+ Revision: 588204
- Bumped the release to 3 in order to rebuild now that Capture-Tiny is in main
- Added some missing dependencies
- Upgraded to 2.518

* Thu Sep 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:2.512.0-1mdv2011.0
+ Revision: 575418
- update to 2.512

* Tue Aug 31 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:2.511.0-1mdv2011.0
+ Revision: 574832
- adding missing buildrequires:
- adding missing buildrequires:
- update to 2.511

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1:2.2.6-5mdv2011.0
+ Revision: 564578
- rebuild for perl 5.12.1

* Tue Jul 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:2.2.6-4mdv2011.0
+ Revision: 556141
- rebuild for perl 5.12

* Fri Apr 30 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:2.2.6-3mdv2010.1
+ Revision: 541187
- downgrade to 2.2.6
- adding missing buildrequires: (adding pango support)

* Thu Apr 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.403.0-1mdv2010.1
+ Revision: 537896
- update missing buildrequires:
- update buildrequires:
- update to 2.4

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.6-2mdv2010.1
+ Revision: 488793
- rebuilt against libjpeg v8

* Thu Dec 31 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.2.6-1mdv2010.1
+ Revision: 484436
- update to v2.2.6

* Sat Nov 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.2.5-1mdv2010.1
+ Revision: 462465
- update to v2.2.5

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 2.2.2.11-3mdv2010.0
+ Revision: 454805
- do not package huge examples

* Sun Sep 27 2009 Funda Wang <fwang@mandriva.org> 2.2.2.11-2mdv2010.0
+ Revision: 449969
- rebuild for new SDL_gfx

* Thu Sep 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.2.2.11-1mdv2010.0
+ Revision: 427882
- update to v2.2.2.11

* Tue Aug 25 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.2.1.8-1mdv2010.0
+ Revision: 421140
- forgot to commit the tarball
- update to 2.2.1.8

* Sun Aug 16 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.2.0-2mdv2010.0
+ Revision: 417018
- force rebuild
- pkgname back to what it was
- update to 2.2.0

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.1.3-4mdv2009.1
+ Revision: 351750
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.1.3-3mdv2009.0
+ Revision: 224051
- rebuild

* Thu Mar 06 2008 Adam Williamson <awilliamson@mandriva.org> 2.1.3-2mdv2008.1
+ Revision: 180292
- use modified tarball with non-free font files (and the test script which uses them) removed (#38257)

* Sun Feb 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.3-1mdv2008.1
+ Revision: 164957
- new version

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.20.0-18mdv2008.1
+ Revision: 152277
- rebuild
- rebuild

* Tue Jan 08 2008 Thierry Vignaud <tv@mandriva.org> 1.20.0-16mdv2008.1
+ Revision: 146728
- fix mesaglu-devel BR
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.20.0-16mdv2007.0
+ Revision: 100649
- unpack patches
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-SDL

* Mon Sep 11 2006 Stefan van der Eijk <stefan@mandriva.org> 1.20.0-15
- %%mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.20.0-14mdk
- Rebuild

* Mon Dec 27 2004 Götz Waschk <waschk@linux-mandrake.com> 1.20.0-13mdk
- rebuild for new SDL_gfx

* Mon Nov 15 2004 Götz Waschk <waschk@linux-mandrake.com> 1.20.0-12mdk
- rebuild for new perl

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.20.0-11mdk
- patch for new SDL_gfx

* Thu May 20 2004 Götz Waschk <waschk@linux-mandrake.com> 1.20.0-10mdk
- drop patch 1 and build against fixed SDL_gfx

* Wed May 19 2004 Götz Waschk <waschk@linux-mandrake.com> 1.20.0-9mdk
- patch for new SDL_gfx

