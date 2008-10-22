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
%bcond_without	static_libs	# don't build static libraries
#
# NOTE: the following libraries are dlopened by soname detected at build time:
# libasound.so.2
# libesd.so.0
# libpulse-simple.so.0
# libX11.so.6
# libXext.so.6
# libXrender.so.1
# libXrandr.so.2
Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(pl.UTF-8):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimediów
Summary(zh_CN.UTF-8):	SDL (Simple DirectMedia Layer) Generic APIs - 游戏/多媒体库
Name:		SDL
Version:	1.2.13
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	c6660feea2a6834de10bc71b2f8e4d88
Patch0:		%{name}-mmx-constraints.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-caca.patch
Patch3:		%{name}-libdir.patch
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
BuildRequires:	pulseaudio-devel >= 0.9
%{?with_svga:BuildRequires:	svgalib-devel >= 1.4.0}
BuildRequires:	tslib-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ppc	-maltivec

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description -l pl.UTF-8
SDL (Simple DirectMedia Layer) jest biblioteką udostępniającą
przenośny, niskopoziomowy dostęp do bufora ramki video, wyjścia audio,
myszy oraz klawiatury. Może obsługiwać zarówno okienkowy tryb XFree86
jak i DGA. Konstruując ją miano na uwadze przenośność: aplikacje
konsolidowane z SDL można również budować w systemach Win32 i BeOS.

%description -l pt_BR.UTF-8
Esse é o Simple DirectMedia Layer, uma API genérica que dá acesso de
baixo nível a áudio, teclado, mouse e vídeo em várias plataformas.

Essa biblioteca é usada por alguns jogos.

%description -l ru.UTF-8
SDL (Simple DirectMedia Layer) это набор функций, предоставляющий
низкоуровневый доступ к звуку, клавиатуре, манипулятору мышь и к
буферу экрана на множестве различных платформ.

%package devel
Summary:	SDL - Header files
Summary(pl.UTF-8):	SDL - Pliki nagłówkowe
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de cabeçalho para aplicações SDL
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ, использующих SDL
Summary(uk.UTF-8):	Файли, необхідні для розробки програм, що використовують SDL
Summary(zh_CN.UTF-8):	SDL (Simple DirectMedia Layer) 开发库
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Suggests:	OpenGL-GLU-devel
%{?with_directfb:Requires:	DirectFB-devel >= 0.9.15}
%{?with_aa:Requires:	aalib-devel}
%{?with_caca:Requires:	libcaca-devel}
%{?with_ggi:Requires:	libggi-devel}
%{?with_nas:Requires:	nas-devel}
%{?with_svga:Requires:	svgalib-devel >= 1.4.0}
Requires:	tslib-devel

%description devel
SDL - Header files.

%description devel -l pl.UTF-8
SDL - Pliki nagłówkowe.

%description devel -l pt_BR.UTF-8
Esse pacote contém bibliotecas, arquivos de cabeçalho e outros
recursos para o desenvolvimento de aplicativos com SDL.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ,
использующих SDL.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм, що
використовують SDL.

%package static
Summary:	SDL - static libraries
Summary(pl.UTF-8):	SDL - biblioteki statyczne
Summary(pt_BR.UTF-8):	Biblioteca estática para desenvolvimento de aplicações com a SDL
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием SDL
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням SDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SDL - static libraries.

%description static -l pl.UTF-8
SDL - biblioteki statyczne.

%description static -l pt_BR.UTF-8
Biblioteca estática para desenvolvimento de aplicações com a SDL.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для разработки программ,
использующих SDL.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки для розробки програм, що
використовують SDL.

%package examples
Summary:	SDL - example programs
Summary(pl.UTF-8):	SDL - programy przykładowe
License:	Public Domain
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
SDL - example programs.

%description examples -l pl.UTF-8
SDL - przykładowe programy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1	# needs rewrite
%patch3 -p1

: > acinclude.m4
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
	--with-x \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -rf test/autom4te.cache
install test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf docs/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS README README-SDL.txt TODO WhatsNew
%attr(755,root,root) %{_libdir}/libSDL-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL-1.2.so.0

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
%{_mandir}/man3/SDL*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL.a
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
