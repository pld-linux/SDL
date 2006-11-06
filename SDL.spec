#
# Conditional build:
%bcond_with	aalib		# with aalib graphics support
%bcond_with	caca		# with caca graphics support
%bcond_with	directfb	# with DirectFB graphics support
%bcond_with	ggi		# with GGI graphics support
%bcond_with	nas		# with NAS audio support
%bcond_with	svga		# with svgalib graphics support
%bcond_without	alsa		# without ALSA audio support
%bcond_without	arts		# without aRts audio support
%bcond_without	esd		# without EsounD audio support
#
# NOTE: the following libraries are dlopened by soname detected at build time:
# libasound.so.2
# libesd.so.0
# libX11.so.6
# libXext.so.6
# libXrender.so.1
# libXrandr.so.2
Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(pl):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimediów
Summary(zh_CN):	SDL (Simple DirectMedia Layer) Generic APIs - ÓÎÏ·/¶àÃ½Ìå¿â
Name:		SDL
Version:	1.2.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	418b42956b7cd103bfab1b9077ccc149
Patch0:		%{name}-mmx-constraints.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-caca.patch
URL:		http://www.libsdl.org/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.15}
BuildRequires:	OpenGL-GLU-devel
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{?with_arts:BuildRequires:	artsc-devel >= 1.1}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
BuildRequires:	gcc >= 5:4.0
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libtool >= 2:1.4d
%{?with_nas:BuildRequires:	nas-devel}
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	perl-modules
%{?with_directfb:BuildRequires:	pkgconfig >= 1:0.7}
%{?with_svga:BuildRequires:	svgalib-devel >= 1.4.0}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description -l pl
SDL (Simple DirectMedia Layer) jest bibliotek± udostêpniaj±c±
przeno¶ny, niskopoziomowy dostêp do bufora ramki video, wyj¶cia audio,
myszy oraz klawiatury. Mo¿e obs³ugiwaæ zarówno okienkowy tryb XFree86
jak i DGA. Konstruuj±c j± miano na uwadze przeno¶no¶æ: aplikacje
konsolidowane z SDL mo¿na równie¿ budowaæ w systemach Win32 i BeOS.

%description -l pt_BR
Esse é o Simple DirectMedia Layer, uma API genérica que dá acesso de
baixo nível a áudio, teclado, mouse e vídeo em várias plataformas.

Essa biblioteca é usada por alguns jogos.

%description -l ru
SDL (Simple DirectMedia Layer) ÜÔÏ ÎÁÂÏÒ ÆÕÎËÃÉÊ, ÐÒÅÄÏÓÔÁ×ÌÑÀÝÉÊ
ÎÉÚËÏÕÒÏ×ÎÅ×ÙÊ ÄÏÓÔÕÐ Ë Ú×ÕËÕ, ËÌÁ×ÉÁÔÕÒÅ, ÍÁÎÉÐÕÌÑÔÏÒÕ ÍÙÛØ É Ë
ÂÕÆÅÒÕ ÜËÒÁÎÁ ÎÁ ÍÎÏÖÅÓÔ×Å ÒÁÚÌÉÞÎÙÈ ÐÌÁÔÆÏÒÍ.

%package devel
Summary:	SDL - Header files
Summary(pl):	SDL - Pliki nag³ówkowe
Summary(pt_BR):	Bibliotecas e arquivos de cabeçalho para aplicações SDL
Summary(ru):	æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ SDL
Summary(uk):	æÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ SDL
Summary(zh_CN):	SDL (Simple DirectMedia Layer) ¿ª·¢¿â
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_directfb:Requires:	DirectFB-devel >= 0.9.15}
%{?with_aa:Requires:	aalib-devel}
%{?with_caca:Requires:	libcaca-devel}
%{?with_ggi:Requires:	libggi-devel}
%{?with_nas:Requires:	nas-devel}
%{?with_svga:Requires:	svgalib-devel >= 1.4.0}

%description devel
SDL - Header files.

%description devel -l pl
SDL - Pliki nag³ówkowe.

%description devel -l pt_BR
Esse pacote contém bibliotecas, arquivos de cabeçalho e outros
recursos para o desenvolvimento de aplicativos com SDL.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ,
ÉÓÐÏÌØÚÕÀÝÉÈ SDL.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ SDL.

%package static
Summary:	SDL - static libraries
Summary(pl):	SDL - biblioteki statyczne
Summary(pt_BR):	Biblioteca estática para desenvolvimento de aplicações com a SDL
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ SDL
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ SDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SDL - static libraries.

%description static -l pl
SDL - biblioteki statyczne.

%description static -l pt_BR
Biblioteca estática para desenvolvimento de aplicações com a SDL.

%description static -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ,
ÉÓÐÏÌØÚÕÀÝÉÈ SDL.

%description static -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ SDL.

%package examples
Summary:	SDL - example programs
Summary(pl):	SDL - programy przyk³adowe
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
SDL - example programs.

%description examples -l pl
SDL - przyk³adowe programy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1	# needs rewrite

%{!?with_alsa:echo 'AC_DEFUN([AM_PATH_ALSA],[$3])' >> acinclude.m4}
%{!?with_esd:echo 'AC_DEFUN([AM_PATH_ESD],[$3])' >> acinclude.m4}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
%ifarch %{ix86}
	--enable-nasm \
%else
	--disable-nasm \
%endif
	--disable-rpath \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_arts:--disable-arts} \
	--enable-dga \
	%{!?with_esd:--disable-esd} \
	%{!?with_nas:--disable-nas} \
	--enable-pthreads \
	--enable-pthread-sem \
	%{?with_aalib:--enable-video-aalib} \
	%{?with_caca:--enable-video-caca} \
	%{!?with_directfb:--disable-video-directfb} \
	--enable-video-dga \
	--enable-video-fbcon \
	%{?with_ggi:--enable-video-ggi} \
	--enable-video-opengl \
	%{!?with_svga:--disable-video-svga} \
	--enable-video-x11-dgamouse \
	--enable-video-x11-vm \
	--enable-video-x11-xinerama \
	--enable-video-x11-xme \
	--enable-video-x11-xrandr \
	--enable-video-x11-xv \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf docs/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS README TODO WhatsNew
%attr(755,root,root) %{_libdir}/libSDL-*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs.html docs
%attr(755,root,root) %{_bindir}/sdl-config
%attr(755,root,root) %{_libdir}/libSDL.so
%{_libdir}/libSDL.la
%{_libdir}/libSDLmain.a
%{_includedir}/SDL
%{_aclocaldir}/sdl.m4
%{_pkgconfigdir}/sdl.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
