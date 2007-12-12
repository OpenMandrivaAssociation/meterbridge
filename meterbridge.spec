%define name	meterbridge
%define version 0.9.2
%define release 2mdk

Summary:	Software meterbridge for Jack
Name:		%name
Version:	%version
Release:	%release
URL: 		http://plugin.org.uk/meterbridge/
Source: 	%{name}-%{version}.tar.bz2
#Patch0: %{name}-0.9.0-jack-0.41.patch
License: 	GPL
Group: 		Sound
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:	jackit-devel SDL_image-devel

%description
Software meterbridge for the UNIX based JACK audio system. It supports
a number of different types of meter, rendered using the SDL library
and user-editable pixmaps.

%prep
%setup -q
#%patch0 -p1

%build
%configure2_5x
%make CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL
%{_bindir}/%name
%{_datadir}/%name

