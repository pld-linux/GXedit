Summary: 	A multi-function text editor using GTK+
Summary(pl):	Wielofunkcyjny edytor tekstu wykorzystuj±cy GTK+
Name:		GXedit
Version:	1.23
Release:	5
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Copyright:	Freely distributable
URL:		http://devplanet.fastethernet.net/gxedit.html
Source0:	%{name}%{version}.tar.gz
Source1:	GXedit.desktop
Patch0:		GXedit-config.patch
Patch1: 	GXedit-makefile.patch
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	XFree86-devel
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
Here is a fast, easy-to-use editor which is both network oriented and very
secure. GXedit is a graphical text editor which features a toolbar, network
bar and tooltips, spell checking, inline help, the ability to send text as
e-mail, macros and more. GXedit was designed to balance these and many other
features without becoming too bloated.

%description -l pl
Oto szybki, ³atwy w obs³udze edytor, który jest nastawiony na pracê w sieci,
a przy tym bardzo bezpieczny. GXedit jest graficznym edytorem tekstu, 
który dostarcza takie funkcje jak pasek narzêdziowy, sprawdzanie pisowni, 
mo¿liwo¶æ wysy³ania tekstu poczt± elektroniczn±, makra i wiele innych.
GXedit zosta³ zaprojektowany tak, aby obecno¶æ tych i wielu innych funkcji 
nie wp³ywa³a zbytnio na objêto¶æ samego programu.

%prep
%setup -n %{name}%{version} -q
%patch0 -p1
%patch1 -p1

%build
sed s^/usr/doc/GXedit/^%{_defaultdocdir}/%{name}-%{version}/^g gxedit.c > gxedit.c.new
mv -f gxedit.c.new gxedit.c

make OPTFLAGS="$RPM_OPT_FLAGS -Wall" gxe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/X11/applnk/Editors}

make install \
	SHARE=$RPM_BUILD_ROOT%{_datadir}/ \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir}/

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Editors

gzip -9nf docs/manual.txt docs/manual.ps docs/quickref.txt docs/quickref.ps \
	README CHANGELOG docs/DEPENDENCIES

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {docs/manual.txt,docs/manual.ps,docs/quickref.txt,docs/quickref.ps}.gz
%doc {README,CHANGELOG,docs/DEPENDENCIES}.gz example.gxeditrc

%attr(755,root,root) %{_bindir}/*

/etc/X11/applnk/Editors/GXedit.desktop
%{_datadir}/GXedit
