Summary:	Indexing tool to manage cds collection
Summary(pl.UTF-8):   Program do katalogowania płyt CD
Name:		biblos
Version:	0.35
Release:	1
License:	GPL or QPL
Group:		X11/Applications
Source0:	http://biblos.f2g.net/%{name}-%{version}.tar.gz
# Source0-md5:	eb430f123edd636ab1e75e7b56252034
Source1:	%{name}.desktop
Patch0:		%{name}-qt_mt.patch
URL:		http://biblos.f2g.net/
BuildRequires:	expat-devel
BuildRequires:	qmake
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Biblos is intended to be an easy to use file indexing tool that
can manage your MP3 collection, your cds collection and even
local directories. It is distributed under GNU General Public License
and Q Public License and it is a work in progress. The following
things are not implemented:

- Delete object button
- Properties button
- Biblos Manual button
- the program does not index links

%description -l pl.UTF-8
Biblos ma być łatwym w użyciu narzędziem do indeksowania plików,
mogącym zarządzać kolekcją plików MP3, płyt CD lub nawet lokalnymi
katalogami. Jest rozpowszechniany na Powszechnej Licencji Publicznej
GNU (GPL) oraz Licencji Publicznej Q (QPL, Q Public License) i jest
w trakcie tworzenia. Następujące rzeczy jeszcze nie zostały
zaimplementowane:

- przycisk usuwania obiektu
- przycisk właściwości
- przycisk podręcznika
- program nie indeksuje dowiązań

%prep
%setup -qcT
tar xzf %{SOURCE0} -C . 
chmod -R +x %{name}-%{version}
%patch0 -p0

%build
mv %{name}-%{version}/* .
qmake biblos.pro
%{__make} QTDIR="/usr" CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install images/logo.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}-logo.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,HISTORY,TODO,WARNING,WHATIS}
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
