# build breaks without these, not easily fixable, and contains no
# shared libs anyway - AdamW 2008/09
%define _disable_ld_no_undefined	1
%define _disable_ld_as_needed		1

Summary:	Software meterbridge for Jack
Name:		meterbridge
Version:	0.9.2
Release:	%{mkrel 4}
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

