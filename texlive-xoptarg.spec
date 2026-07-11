%global tl_name xoptarg
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Expandable macros that take an optional argument
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xoptarg
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xoptarg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xoptarg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Commands that take an optional argument are not ordinarily expandable;
this package allows such commands to be expandable provided that they
have at least one mandatory argument.

