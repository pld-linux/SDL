Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		SDL
Version:	1.0.6
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		http://www.devolution.com/~slouken/SDL/release/%{name}-%{version}.tar.gz
URL:		http://www.devolution.com/~slouken/SDL/
BuildRequires:	XFree86-devel
BuildRequires:	esound-devel
BuildRequires:	gtk+-devel >= 1.2.1
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable, low
level access to a video framebuffer, audio output, mouse, and keyboard. It
can support both windowed and DGA modes of XFree86, and it is designed to
be portable - applications linked with SDL can also be built on Win32 and
BeOS.

%package devel
Summary:	SDL - Header files
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
SDL - Header files.

%package static
Summary:	SDL - static libraries
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description static
SDL - static libraries.

%prep
%setup -q
%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-nasm \
	--enable-pthreads \
	--with-x \
	--enable-video-x11-dga \
	--enable-video-x11-mtrr \
	--enable-esd \
	--disable-video-svga

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=/usr/share/aclocal

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf BUGS README WhatsNew

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz docs.html docs
%attr(755,root,root) %{_bindir}/sdl-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/libSDLmain.a
%{_includedir}/SDL
/usr/share/aclocal/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
