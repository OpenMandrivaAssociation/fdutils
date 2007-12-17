Summary:	Programs for dealing with floppy disks
Name:		fdutils
Version:	5.5
Release:	%mkrel 1
URL:		http://fdutils.linux.lu/
Source0:	http://fdutils.linux.lu/%{name}-%{version}.tar.bz2
#Patch0:		fdutils-5.4-20030718.diff
Patch1:		fdutils-manpages.patch
Patch2:		fdutils-Makefile-fixes.patch
Patch3:		fdutils-5.4-linux2.6-buildfix.patch
License:	GPL
Group:		System/Kernel and hardware
ExclusiveOS:	Linux
BuildRequires:	flex tetex-latex texinfo e2fsprogs-devel

%description
This package contains utilities for configuring and debugging the
Linux floppy driver, for formatting extra capacity disks (up to 1992K
on a high density disk), for sending raw commands to the floppy
controller, etc.

NOTE:
This package contains files which supercede corresponding versions
in the man-pages and util-linux packages.  Therefore, the --replacefiles
(or --force) option to rpm may be needed to install this package.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .peroyvind

%build
%configure
# %make is broken with this Makefile
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/{man1,man4}/
mkdir -p $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

%makeinstall

#cp src/mediaprm $RPM_BUILD_ROOT/%{_sysconfdir}

rm -f $RPM_BUILD_ROOT%{_bindir}/{diskd,diskseekd,setfdprm}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -z "$DURING_INSTALL" ]; then
  %_install_info fdutils.info 
fi

%preun
if [ "$1" = 0 ]; then
  %{__install_info} --delete fdutils.info
fi
      
%files
%defattr(755,root,floppy,-)
%{_bindir}/xdfcopy
%{_bindir}/floppycontrol
%{_bindir}/floppymeter
%{_bindir}/superformat
%{_bindir}/getfdprm
%{_bindir}/MAKEFLOPPIES
%{_bindir}/fdrawcmd
%{_bindir}/fdmount
%{_bindir}/fdumount
%{_bindir}/xdfformat
%{_bindir}/fdlist
%{_bindir}/fdmountd
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/mediaprm
%{_mandir}/man1/*
%{_mandir}/man4/*
%{_infodir}/*


