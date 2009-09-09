%define	name	xmms-find
%define	oname	xmmsfind
%define version 0.5.2
%define	rel	3
%define release %mkrel %{rel}

Name:		%{name} 
Summary:	XmmsFind plugin for xmms
Version:	%{version} 
Release:	%{release} 
Source0:	http://heanet.dl.sourceforge.net/sourceforge/xmmsfind/%{oname}-%{version}.tar.bz2
URL:		http://xmmsfind.sourceforge.net/
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:	GPL
BuildRequires:	xmms-devel gtk+1.2-devel

%description
XmmsFind is a small plugin for XMMS that enables you to quickly search for a
file in the current playlist, and at your command, play it.
The plugin is very similar to the built-in "jump to file" util, but since it is
launched by an external program, it can be invoked by a windowmanager shortcut
(without having xmms in focus).

%prep
%setup -q -n %{oname}-%{version}

%build
%make FLAGS="-rdynamic $RPM_OPT_FLAGS -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
make \
	PLUGIN_INSTALL_DIR=$RPM_BUILD_ROOT`xmms-config --general-plugin-dir` \
	REMOTE_INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir} \
	install

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc BUGS README TODO VERSION
%{_bindir}/xmmsfind_remote
%{_libdir}/xmms/General/libxmmsfind.so

