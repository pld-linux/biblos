#
# TODO:
# - remove openoffice-lib dependence,
# - maybe some fix at %prep, 
# - polish description,
# - more BRs ?,
Summary:	indexing tool to manage cds collection
Summary(pl):	program do katalogowania p³yt cd
Name:		biblos
Version:	0.35
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://biblos.f2g.net/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://biblos.f2g.net/
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Biblos is intended to be an easy to use file indexing tool that 
can manage your mp3 collection , your cds collection and even
local directories. It is distributed under GNU Public License 
(for a copy go to http://www.gnu.org/) and Q Public License 
(see http://www.trolltech.com/) and it is a work in progress .
The following things are not implemented :
  
- Delete object button
- Properties button
- Biblos Manual button
- the program does not index links

%description -l pl

%prep
rm -rf ../BUILD/%{name}-%{version}
tar -zxf %{SOURCE0} -C ../BUILD
chmod 700 ../BUILD/%{name}-%{version}
cd ../BUILD/%{name}-%{version}
chmod 700 images mc help

%build
cd %{name}-%{version}
qmake
%{__make} QTDIR="/usr" CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Utilities/}

cd %{name}-%{version}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install images/logo.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}-logo.png
install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Utilities/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/doc
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
