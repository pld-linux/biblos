#
# TODO:
# - remove openoffice-lib dependence,
# - more BRs ?,
Summary:	Indexing tool to manage cds collection
Summary(pl):	Program do katalogowania p�yt cd
Name:		biblos
Version:	0.35
Release:	0.1
License:	GPL or QPL
Group:		X11/Applications
Source0:	http://biblos.f2g.net/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://biblos.f2g.net/
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Biblos is intended to be an easy to use file indexing tool that 
can manage your mp3 collection, your cds collection and even
local directories. It is distributed under GNU Public License 
and Q Public License and it is a work in progress. The following
things are not implemented:
  
- Delete object button
- Properties button
- Biblos Manual button
- the program does not index links

%description -l pl
Biblos ma by� �atwym w u�yciu narz�dziem do indeksowania plik�w,
mog�cym zarz�dza� kolekcj� plik�w mp3, p�yt CD lub nawet lokalnymi
katalogami. Jest rozpowszechniany na Powszechnej Licencji Publicznej
GNU (GPL) oraz Licencji Publicznej Q (QPL, Q Public License) i jest
w trakcie tworzenia. Nast�puj�ce rzeczy jeszcze nie zosta�y
zaimplementowane:

- przycisk usuwania obiektu
- przycisk w�a�ciwo�ci
- przycisk podr�cznika
- program nie indeksuje dowi�za�

%prep
%setup -qcT
tar xzf %{SOURCE0} -C ..
chmod +x . images mc help

%build
qmake biblos.pro
%{__make} QTDIR="/usr" CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Utilities}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install images/logo.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}-logo.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,HISTORY,TODO,WARNING,WHATIS}
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Utilities/*
