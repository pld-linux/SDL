Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		SDL
Version:	0.9.9
Release:	1
Group:		X11/Libraries
Copyright:	LGPL
Source:		http://www.devolution.com/~slouken/projects/SDL/SDL-0.9/src/%{name}-%{version}.tar.gz
Source1:	SDL-demos.tar.gz
URL:		http://www.devolution.com/~slouken/projects/SDL
BuildRoot:	/tmp/%{name}-%{version}-root

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable, low
level access to a video framebuffer, audio output, mouse, and keyboard. It
can support both windowed and DGA modes of XFree86, and it is designed to be
portable - applications linked with SDL can also be built on Win32 and BeOS.

%package devel
Group:		X11/Libraries
Summary:	SDL - Header files & static libraries

%description devel
SDL - Header files & static libraries

%package extras
Group:		X11/Utilities
Summary:	SDL - Test programs and demos

%description extras
SDL - Test programs and demos

%prep
%setup -q
tar -xvzf %{SOURCE1}
chown -R 0.0 *
make config <<EOF

EOF

%build
make DEBUG="$RPM_OPT_FLAGS"
cd test
make
cd ..
cd SDL-demos
for i in PTC aliens draw fire flxplay maclib mixer plasma scrap screenlib stars ttflib warp xflame; do (cd $i;make SDL=../../);done;
cd ..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin/SDL
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/include/SDL
cp -a lib/* $RPM_BUILD_ROOT/usr/lib
cp -a include/* $RPM_BUILD_ROOT/usr/include/SDL
for i in checkkeys graywin loopwave pixelformat testalpha testbitmap testhread testkeys testlock testtimer testtypes testver testwin testwm; do cp -a test/$i $RPM_BUILD_ROOT/usr/bin/SDL; done;
for i in PTC aliens draw fire flxplay maclib mixer netlib plasma scrap screenlib stars ttflib warp xflame; do cp -a SDL-demos/$i $RPM_BUILD_ROOT/usr/bin/sdl; done;
find $RPM_BUILD_ROOT/usr/bin/SDL -name "*.[hco]" | xargs rm -f

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COPYING INSTALL README TODO WhatsNew docs docs.html
/usr/lib/libSDLx11.so.*.*

%files devel
%defattr(644,root,root,755)
/usr/include/SDL

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%files extras
%defattr(644,root,root,755)
/usr/bin/SDL
