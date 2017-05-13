Name:           check_ali_plugin
Version:        1.0
Release:        1%{?dist}
Summary:        this is ali's nagios nrpe plugin

Group:          nti-320-ashand01
License:        GPL
URL:            http://www.github.com
Source0:        check_ali_plugin-1.0.tar.gz

BuildRequires:  bash
Requires:       nagios, check_nrpe_plugin

%description
this is ali's nagios nrpe plugin

%prep
%setup -q


%build



%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib64/nagios/plugins

install -m 0755 %{name} %{buildroot}/usr/lib64/nagios/plugins/%{name}

%clean
rm -rf %{buildroot}

%files
/usr/lib64/nagios/plugins/check_ali_plugin

%post
sudo chown nagios:nagios /usr/lib64/nagios/plugins/check_ali_plugin
sudo chmod +x /usr/lib64/nagios/plugins/check_ali_plugin

