Summary:	A multi-function text editor using GTK+
Summary(es):	Editor de textos multifunciones que usa GTK+
Summary(pl):	Wielofunkcyjny edytor tekstu wykorzystuj±cy GTK+
Summary(pt):	Editor de textos multifunção que usa o GTK+
Name:		GXedit
Version:	1.23
Release:	11
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://users.linuxbox.com/~drow/GXedit/%{name}%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-config.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-nobash.patch
Patch3:		%{name}-time.patch
URL:		http://www.linuxbox.com/~drow/GXedit/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Here is a fast, easy-to-use editor which is both network oriented and
very secure. GXedit is a graphical text editor which features a
toolbar, network bar and tooltips, spell checking, inline help, the
ability to send text as e-mail, macros and more. GXedit was designed
to balance these and many other features without becoming too bloated.

%description -l es
Editor de textos multifunciones que usa GTK+.

%description -l pl
Oto szybki, ³atwy w obs³udze edytor, który jest nastawiony na pracê w
sieci, a przy tym bardzo bezpieczny. GXedit jest graficznym edytorem
tekstu, który dostarcza takich funkcji jak pasek narzêdzi, sprawdzanie
pisowni, mo¿liwo¶æ wysy³ania tekstu poczt± elektroniczn±, makra i
wiele innych. GXedit zosta³ zaprojektowany tak, aby obecno¶æ tych i
wielu innych funkcji nie wp³ywa³a zbytnio na objêto¶æ samego programu.

%description -l pt_BR
O GXedit é um editor de textos gráficos com múltiplas funções que
utiliza o GTK+.

%prep
%setup -n %{name}%{version} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
sed s^/usr/doc/GXedit/^%{_defaultdocdir}/%{name}-%{version}/^g gxedit.c > gxedit.c.new
mv -f gxedit.c.new gxedit.c

%{__make} OPTFLAGS="%{rpmcflags} -Wall" gxe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Editors}

%{__make} install \
	SHARE=$RPM_BUILD_ROOT%{_datadir}/ \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir}/

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Editors

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/manual.txt docs/manual.ps docs/quickref.txt docs/quickref.ps
%doc README CHANGELOG docs/DEPENDENCIES example.gxeditrc

%attr(755,root,root) %{_bindir}/*

%{_applnkdir}/Editors/GXedit.desktop
%{_datadir}/GXedit
