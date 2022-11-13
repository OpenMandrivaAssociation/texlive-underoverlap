Name:		texlive-underoverlap
Version:	29019
Release:	1
Summary:	Position decorations over and under expressions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/underoverlap
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underoverlap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underoverlap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package overcomes TeX's inherent limitations in commands
that place decorations (such as braces) at arbirary positions
over and under expressions, overlapping as necessary.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/underoverlap/underoverlap.sty
%doc %{_texmfdistdir}/doc/latex/underoverlap/README
%doc %{_texmfdistdir}/doc/latex/underoverlap/dry.sty
%doc %{_texmfdistdir}/doc/latex/underoverlap/packagedoc.cls
%doc %{_texmfdistdir}/doc/latex/underoverlap/underoverlap.pdf
%doc %{_texmfdistdir}/doc/latex/underoverlap/underoverlap.tex
%doc %{_texmfdistdir}/doc/latex/underoverlap/with.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
