#
# Conditional build:
# _without_alsa - without ALSA support
# _without_esound - without esound support
# _without_arts - without arts support
# _with_svga - with svgalib support
# _with_aalib - with aalib support
# _with_ggi - with GGI support
#
%ifarch	alpha
%define _without_arts 1
%endif

Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(es):	Simple DirectMedia Layer
Summary(pl):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimediów
Summary(pt_BR):	Simple DirectMedia Layer
Name:		SDL
Version:	1.2.4
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-byteorder.patch
Patch1:		%{name}-fixlibs.patch
Patch2:		%{name}-amfix.patch
Patch3:		%{name}-lpthread.patch
Patch4:		%{name}-ac25x.patch
URL:		http://www.libsdl.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_esound:BuildRequires:	esound-devel}
%{!?_without_arts:BuildRequires:	arts-devel}
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	OpenGL-devel
BuildRequires:	perl-modules
%ifarch %{ix86}
BuildRequires:	nasm
%endif
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
%{?_with_svgalib:BuildRequires:	svgalib-devel}
%{?_with_aalib:BuildRequires:	aalib-devel}
%{?_with_ggi:BuildRequires:	libggi-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description -l pl
SDL (Simple DirectMedia Layer) jest bibliotek± udostêpniaj±c±
przeno¶ny, niskopoziomowy dostep do bufora ramki video, wyj¶cia audio,
myszy oraz klawiatury, Moze obs³ugiwaæ zarówno okienkowy tryb XFree86
jak i DGA. Konstruuj±c j± miano na uwadze przeno¶no¶æ: aplikacje
konsolidowane z SDL mo¿na równie¿ budowac w systemach Win32 i BeOS.

%description -l pt_BR
Esse é o Simple DirectMedia Layer, uma API genérica que dá acesso de
baixo nível a áudio, teclado, mouse e vídeo em várias plataformas.

Essa biblioteca é usada por alguns jogos.

%package devel
Summary:	SDL - Header files
Summary(pl):	SDL - Pliki nag³ówkowe
Summary(pt_BR):	Bibliotecas e arquivos de cabeçalho para aplicações SDL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
%ifnarch sparc sparc64
%{!?_without_alsa:Requires:	alsa-lib-devel}
%endif
%{!?_without_esound:Requires:	esound-devel}
%{!?_without_arts:Requires:	arts-devel}
Requires:	XFree86-devel >= 4.0.2

%description devel
SDL - Header files.

%description devel -l pl
SDL - Pliki nag³ówkowe.

%description devel -l pt_BR
Esse pacote contém bibliotecas, arquivos de cabeçalho e outros
recursos para o desenvolvimento de aplicativos com SDL.

%package static
Summary:	SDL - static libraries
Summary(pl):	SDL - biblioteki statyczne
Summary(pt_BR):	Biblioteca estática para desenvolvimento de aplicações com a SDL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
SDL - static libraries.

%description static -l pl
SDL - biblioteki statyczne.

%description static -l pt_BR
Biblioteca estática para desenvolvimento de aplicações com a SDL.

%package examples
Summary:	SDL - example programs
Summary(pl):	SDL - programy przyk³adowe
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
SDL - example programs.

%description examples -l pl
SDL - przyk³adowe programy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
%{__autoconf}
# Another hack
cp -f src/hermes/Makefile.in Makefile.in.ok
automake -a -c --foreign
cp -f Makefile.in.ok src/hermes/Makefile.in
%configure \
%ifarch %{ix86}
	--enable-nasm \
%else
	--disable-nasm \
%endif
	--enable-pthreads \
	--enable-pthread-sem \
	--with-x \
	--enable-dga \
	--enable-video-dga \
	--enable-video-x11-dgamouse \
	--enable-video-x11-vm \
	--enable-video-x11-xv \
	--enable-video-opengl \
	--enable-video-fbcon \
	%{?_with_svga:--enable-video-svga} \
	%{?_with_aalib:--enable-video-aalib} \
	%{?_with_ggi:--enable-video-ggi} \
%ifnarch sparc sparc64
	%{!?_without_alsa:--enable-alsa} \
%endif
	%{!?_without_esound:--enable-esd} \
	%{!?_without_arts:--enable-arts}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -rf docs/man3 docs/Makefile* docs/html/Makefile*

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf BUGS CREDITS README TODO WhatsNew

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {BUGS,CREDITS,README,TODO,WhatsNew}.gz docs.html docs
%attr(755,root,root) %{_bindir}/sdl-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/libSDLmain.a
%{_includedir}/SDL
%{_aclocaldir}/*
%{_mandir}/man3/*

%files examples
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL.a
