# build breaks without these, not easily fixable, and contains no
# shared libs anyway - AdamW 2008/09
%define _disable_ld_no_undefined	1
%define _disable_ld_as_needed		1

Summary:	Software meterbridge for Jack
Name:		meterbridge
Version:	0.9.2
Release:	%{mkrel 5}
URL: 		http://plugin.org.uk/meterbridge/
Source0: 	%{name}-%{version}.tar.bz2
# From Debian: fix build by removing duplicate declaration of buf_rect
# AdamW 2008/09
Patch0:		meterbridge-0.9.2-build.patch
License: 	GPL+
Group: 		Sound
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:	jackit-devel
BuildRequires:	SDL_image-devel

%description
Software meterbridge for the UNIX based JACK audio system. It supports
a number of different types of meter, rendered using the SDL library
and user-editable pixmaps.

%prep
%setup -q
%patch0 -p1 -b .build

%build
%configure2_5x
%make CC="gcc %{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL
%{_bindir}/%{name}
%{_datadir}/%{name}



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.2-5mdv2010.0
+ Revision: 430021
- rebuild

* Sat Sep 06 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.2-4mdv2009.0
+ Revision: 281766
- don't package COPYING
- add build.patch (from Debian, fix build)
- disable underlinking protection (breaks build and not needed here)
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import meterbridge

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Jul 17 2004 Austin Acton <austin@mandrake.org> 0.9.2-2mdk
- fix buildrequires
- configure 2.5
- use opt flags

* Mon Jun 9 2003 Austin Acton <aacton@yorku.ca> 0.9.2-1mdk
- 0.9.2
- fix buildrequires (SDL_image)

* Fri Apr 25 2003 Austin Acton <aacton@yorku.ca> 0.9.0-2mdk
- buildrequires libSDL-devel

* Sat Feb 8 2003 Austin Acton <aacton@yorku.ca> 0.9.0-1mdk
- initial package
