Name:		texlive-xoptarg
Version:	15878
Release:	2
Summary:	Expandable macros that take an optional argument
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xoptarg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xoptarg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xoptarg.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Commands that take an optional argument are not ordinarily
expandable; this package allows such commands to be expandable
provided they have at least one mandatory argument.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xoptarg/xoptarg.sty
%doc %{_texmfdistdir}/doc/latex/xoptarg/README
%doc %{_texmfdistdir}/doc/latex/xoptarg/xoptarg.pdf
%doc %{_texmfdistdir}/doc/latex/xoptarg/xoptarg.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
