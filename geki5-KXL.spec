Summary:	Geki5, a video-oriented game
Summary(pl):	Geki5 - gra wideo
Name:		geki5-KXL
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRequires:	KXL-devel >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
2D length scroll shooting game.

%description -l pl
Przewijana strzelanina 2D.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --with-x --with-kxl-prefix=%{_libdir}/ \
    --with-kxl-inc-prefix=%{_includedir}/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/geki5
%dir %{_datadir}/geki5
%{_datadir}/geki5/bmp
%{_datadir}/geki5/wav
%dir %{_datadir}/geki5/data
%{_datadir}/geki5/data/*.dat
#%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/geki5.score
#%config(noreplace) %{_datadir}/geki5/data/.score
