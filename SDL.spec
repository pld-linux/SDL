%define version 0.8.8
%define release 1TL
Name: SDL
Version: %{version}
Release: %{release}
Group: X11/Libraries
Copyright: LGPL
Source: SDL-0.8.8.tar.gz
Source1: SDL-demos.tar.gz
URL: http://www.devolution.com/~slouken/projects/SDL
BuildRoot: /mnt/c/TEMP/SDL-root
Summary: SDL (Simple DirectMedia Layer) - Game/Multimedia Library

%package devel
Group: X11/Libraries
Summary: SDL - Header files & static libraries

%package extras
Group: X11/Utilities
Summary: SDL - Test programs and demos

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard.  It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description devel
SDL - Header files & static libraries

%description extras
SDL - Test programs and demos

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
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
mkdir -p $RPM_BUILD_ROOT/usr/bin/SDL
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/include/SDL
cp -a lib/* $RPM_BUILD_ROOT/usr/lib
cp -a include/* $RPM_BUILD_ROOT/usr/include/SDL
for i in checkkeys graywin loopwave pixelformat testalpha testbitmap testhread testkeys testlock testtimer testtypes testver testwin testwm; do cp -a test/$i $RPM_BUILD_ROOT/usr/bin/SDL; done;
for i in PTC aliens draw fire flxplay maclib mixer netlib plasma scrap screenlib stars ttflib warp xflame; do cp -a SDL-demos/$i $RPM_BUILD_ROOT/usr/bin/sdl; done;
find $RPM_BUILD_ROOT/usr/bin/SDL -name "*.[hco]" | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc BUGS COPYING INSTALL README TODO WhatsNew docs docs.html
/usr/lib/libSDLx11.so.0.8
/usr/lib/libSDLx11.so.0.8.8

%files devel
/usr/lib/libSDL.a
/usr/include/SDL

%files extras
/usr/bin/SDL
