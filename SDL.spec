Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		SDL
Version:	0.11.2
Release:	1
Group:		X11/Libraries
Copyright:	LGPL
Source:		http://www.devolution.com/~slouken/projects/SDL/SDL-0.10/src/%{name}-%{version}.tar.gz
URL:		http://www.devolution.com/~slouken/projects/SDL/
BuildRequires:	XFree86-devel
BuildRequires:	esound-devel
BuildRequires:	gtk+-devel >= 1.2.1
BuildRoot:	/tmp/%{name}-%{version}-root

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable, low
level access to a video framebuffer, audio output, mouse, and keyboard. It
can support both windowed and DGA modes of XFree86, and it is designed to be
portable - applications linked with SDL can also be built on Win32 and BeOS.

%package devel
Summary:	SDL - Header files
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description devel
SDL - Header files.

%package static
Summary:	SDL - static libraries
Group:		X11/Libraries
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

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf BUGS README TODO WhatsNew

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
%{_includedir}/SDL
%{_datadir}/aclocal/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
