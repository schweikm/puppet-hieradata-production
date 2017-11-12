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

%build


%install
%{__rm} -fr %{buildroot}
%{__mkdir_p} %{buildroot}/%{environment_path}/data

%{__cp} -R * %{buildroot}/%{environment_path}/data/

%clean
%{__rm} -fr %{buildroot}


%files
%defattr(-,root,root,-)
%{environment_path}/*



%changelog
* Sun Nov 12 2017 Marc Schweikert <schweikm@gmail.com> 1.0-1
- new package built with tito

