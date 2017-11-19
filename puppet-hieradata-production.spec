Name:		puppet-hieradata-production
Version:	1.0
Release:	1%{?dist}
Summary:	Production Puppet hieradata

Group:		Applications/Engineering
License:	GPL
URL:		http://www.bit-sys.com
Source0:	%{name}-%{version}.tar.gz

Requires:	puppet-agent >= 5.0
Requires:   puppet-modules-production

%define debug_package %{nil}
%define environment_path /etc/puppetlabs/code/environments/production

%description
Production Puppet modules


%prep
%setup -q

%{__rm} *.spec
%{__rm} -fr .tito
%{__rm} -fr LICENSE


%build


%install
%{__rm} -fr %{buildroot}
%{__mkdir_p} %{buildroot}/%{environment_path}

%{__cp} hiera.yaml hiera.yaml.real
%{__cp} -R * %{buildroot}/%{environment_path}/


%clean
%{__rm} -fr %{buildroot}


%post
# since we can't deliver this file in place
%{__mv} -f %{environment_path}/hiera.yaml.real %{environment_path}/hiera.yaml || :


%files
%defattr(-,root,root,-)
%{environment_path}/data
%{environment_path}/hiera.yaml.real
%ghost %{environment_path}/hiera.yaml


%changelog
* Sun Nov 12 2017 Marc Schweikert <schweikm@gmail.com> 1.0-1
- new package built with tito

