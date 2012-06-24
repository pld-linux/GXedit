Summary: 	A multi-function text editor using GTK+
Summary(es):	Editor de textos multifunciones que usa GTK+
Summary(pl):	Wielofunkcyjny edytor tekstu wykorzystuj�cy GTK+
Summary(pt_BR):	Editor de textos multifun��o que usa o GTK+
Name:		GXedit
Version:	1.23
Release:	8
Group:		X11/Applications/Editors
Group(es):	X11/Aplicaciones/Editores
Group(pl):	X11/Aplikacje/Edytory
Group(pt_BR):	X11/Aplica��es/Editores
Copyright:	GPL
Source0:	http://users.linuxbox.com/~drow/GXedit/%{name}%{version}.tar.gz
Source1:	GXedit.desktop
Patch0:		GXedit-config.patch
Patch1: 	GXedit-makefile.patch
Patch2:		GXedit-nobash.patch
URL:		http://www.linuxbox.com/~drow/GXedit/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	XFree86-devel
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_applnkdir	%{_datadir}/applnk

%description
Here is a fast, easy-to-use editor which is both network oriented and very
secure. GXedit is a graphical text editor which features a toolbar, network
bar and tooltips, spell checking, inline help, the ability to send text as
e-mail, macros and more. GXedit was designed to balance these and many other
features without becoming too bloated.

%description -l es
Editor de textos multifunciones que usa GTK+.

%description -l pl
Oto szybki, �atwy w obs�udze edytor, kt�ry jest nastawiony na prac� w sieci,
a przy tym bardzo bezpieczny. GXedit jest graficznym edytorem tekstu, 
kt�ry dostarcza takich funkcji jak pasek narz�dzi, sprawdzanie pisowni, 
mo�liwo�� wysy�ania tekstu poczt� elektroniczn�, makra i wiele innych.
GXedit zosta� zaprojektowany tak, aby obecno�� tych i wielu innych funkcji 
nie wp�ywa�a zbytnio na obj�to�� samego programu.

%description -l pt_BR
O GXedit � um editor de textos gr�ficos com m�ltiplas fun��es que utiliza o
GTK+.

%prep
%setup -n %{name}%{version} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
sed s^/usr/doc/GXedit/^%{_defaultdocdir}/%{name}-%{version}/^g gxedit.c > gxedit.c.new
mv -f gxedit.c.new gxedit.c

make OPTFLAGS="$RPM_OPT_FLAGS -Wall" gxe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Editors}

make install \
	SHARE=$RPM_BUILD_ROOT%{_datadir}/ \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir}/

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Editors

gzip -9nf docs/manual.txt docs/manual.ps docs/quickref.txt docs/quickref.ps \
	README CHANGELOG docs/DEPENDENCIES

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {docs/manual.txt,docs/manual.ps,docs/quickref.txt,docs/quickref.ps}.gz
%doc {README,CHANGELOG,docs/DEPENDENCIES}.gz example.gxeditrc

%attr(755,root,root) %{_bindir}/*

%{_applnkdir}/Editors/GXedit.desktop
%{_datadir}/GXedit
