Summary:	DCRAW plugin for GIMP
Summary(pl.UTF-8):	Wtyczka DCRAW dla GIMP-a
Name:		gimp-plugin-dcraw
# RCS revision of source file
Version:	1.32
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://www.cybercom.net/~dcoffin/dcraw/rawphoto.c
# Source0-md5:	2bf4adc85b60aeeaffd7dc65bf9e96ad
URL:		http://www.cybercom.net/~dcoffin/dcraw/
BuildRequires:	gimp-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	dcraw
Requires:	gimp >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins

%description
DCRAW (rawphoto) plugin provides a simple dialog box for loading raw
files into the GIMP.

%description -l pl.UTF-8
Wtyczka DCRAW (rawphoto) udostępnia proste okno dialogowe pozwalające
na wczytywanie plików surowych zdjęć do GIMP-a.

%prep
%setup -q -c -T

%build
gimptool --build %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT

install -D rawphoto $RPM_BUILD_ROOT%{gimpplugindir}/rawphoto

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/rawphoto
