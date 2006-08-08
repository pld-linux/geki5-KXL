Summary:	Geki5, a video-oriented game
Summary(pl):	Geki5 - gra wideo
Name:		geki5-KXL
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
# note: Source0 URL is dead
Source0:	http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
# Source0-md5:	714152011a45b1b1a758e3d1092b4f87
Patch0:		%{name}-scorepath.patch
# dead, couldn't find working one
#URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRequires:	KXL-devel >= 1.1.1
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	KXL >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
2D length scroll shooting game.

%description -l pl
Pionowo przewijana strzelanina 2D.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(2755,root,games) %{_bindir}/geki5
%dir %{_datadir}/geki5
%{_datadir}/geki5/bmp
%{_datadir}/geki5/wav
%dir %{_datadir}/geki5/data
%{_datadir}/geki5/data/*.dat
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/geki5.score
