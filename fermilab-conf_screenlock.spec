Name:		fermilab-conf_screenlock
Version:	1.0
Release:	3.1%{?dist}
Summary:	Sets a default screenlock for the GUI sessions

Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/fermilab-conf_screenlock
Source0:	%{name}.tar.xz

BuildRequires:	bash coreutils systemd
Requires:	system-release
BuildArch:	noarch

# Top level package should require software specific packages
Requires:	(%{name}-gnome == %{version}-%{release} if gnome-session)
Requires:	(%{name}-gnome == %{version}-%{release} if gnome-shell)

%description
Set screensaver to lock automatically

Per: CS-Doc-1065

%package gnome
Summary:	Sets a default screenlock for GDM
Conflicts:	gnome-session < 3.8

Requires(post):	dconf
Requires(postun):	dconf

%description gnome
Set screensaver to lock automatically for GNOME desktop


%prep
%setup -q -n conf


%build


%install

# for GNOME
%{__install} -Dpm 644 dconf/20-screenlock %{buildroot}/%{_sysconfdir}/dconf/db/distro.d/20-screenlock
%{__install} -Dpm 644 dconf/locks/20-screenlock %{buildroot}/%{_sysconfdir}/dconf/db/distro.d/locks/20-screenlock

# for KDE?
# %{__install} -D kscreensaverrc    %{buildroot}/%{_datadir}/config/kscreensaverrc

# for mate?
# %{__install} -D mate-blank-screenlock.override    %{buildroot}/%{_datadir}/glib-2.0/schemas/mate-blank-screenlock.override
# needs glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

#####################################################################

%post gnome -p /bin/bash
dconf update
%postun gnome -p /bin/bash
dconf update

#####################################################################
%files
%defattr(0644,root,root,0755)

%files gnome
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/dconf/db/distro.d/20-screenlock
%config %{_sysconfdir}/dconf/db/distro.d/locks/20-screenlock


#####################################################################
%changelog
* Wed Apr 13 2022 Pat Riehecky <riehecky@fnal.goc> 1.0-3.1
- use rich boolean deps

* Mon Feb 28 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-3
- Split to subpackages
- GNOME is the only shipped desktop for now

* Tue Feb 23 2016 Pat Riehecky <riehecky@fnal.gov> 1.0-2
- Provide old name

* Mon Feb 01 2016 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial build
