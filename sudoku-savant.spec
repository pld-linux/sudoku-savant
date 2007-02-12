Summary:	Application to solve and generate Sudoku puzzles
Summary(pl.UTF-8):   Program do rozwiązywania i tworzenia układanek Sudoku
Name:		sudoku-savant
Version:	1.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/sudoku-savant/%{name}-%{version}.tar.bz2
# Source0-md5:	12b4582a8645039e72254db26fdf8aa6
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-types.patch
URL:		http://gnomefiles.org/app.php?soft_id=1519
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple GUI-driven application to solve and generate Sudoku puzzles
through logical means.

%description -l pl.UTF-8
Prosta graficzna aplikacja do rozwiązywania i tworzenia układanek
Sudoku.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -i "s/\tdesktop-file-install/#\tdesktop-file-install/g" Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
