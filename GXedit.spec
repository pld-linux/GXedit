Summary:	A multi-function text editor using GTK+
Summary(es.UTF-8):   Editor multifuncional de textos que usa GTK+
Summary(pl.UTF-8):   Wielofunkcyjny edytor tekstu wykorzystujący GTK+
Summary(pt.UTF-8):   Editor de textos multifunção que usa o GTK+
Name:		GXedit
Version:	1.23
Release:	14
License:	GPL
Group:		X11/Applications/Editors
# working: ftp://ibiblio.org/pub/Linux/apps/editors/X/%{name}-%{version}.tar.gz
Source0:	%{name}%{version}.tar.gz
# Source0-md5:	afbd834a2fbb73b598e600f23655c13d
Source1:	%{name}.desktop
Patch0:		%{name}-config.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-nobash.patch
Patch3:		%{name}-time.patch
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Here is a fast, easy-to-use editor which is both network oriented and
very secure. GXedit is a graphical text editor which features a
toolbar, network bar and tooltips, spell checking, inline help, the
ability to send text as e-mail, macros and more. GXedit was designed
to balance these and many other features without becoming too bloated.

%description -l pl.UTF-8
Oto szybki, łatwy w obsłudze edytor, który jest nastawiony na pracę w
sieci, a przy tym bardzo bezpieczny. GXedit jest graficznym edytorem
tekstu, który dostarcza takich funkcji jak pasek narzędzi, sprawdzanie
pisowni, możliwość wysyłania tekstu pocztą elektroniczną, makra i
wiele innych. GXedit został zaprojektowany tak, aby obecność tych i
wielu innych funkcji nie wpływała zbytnio na objętość samego programu.

%description -l pt_BR.UTF-8
O GXedit é um editor de textos gráficos com múltiplas funções que
utiliza o GTK+.

%prep
%setup -n %{name}%{version} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{__sed} -i -e s^%{_prefix}/doc/GXedit/^%{_docdir}/%{name}-%{version}/^g gxedit.c

%build
%{__make} OPTFLAGS="%{rpmcflags} -Wall" gxe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

%{__make} install \
	SHARE=$RPM_BUILD_ROOT%{_datadir}/ \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir}/

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/manual.txt docs/manual.ps docs/quickref.txt docs/quickref.ps
%doc README CHANGELOG docs/DEPENDENCIES example.gxeditrc
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/GXedit.desktop
%{_datadir}/GXedit
