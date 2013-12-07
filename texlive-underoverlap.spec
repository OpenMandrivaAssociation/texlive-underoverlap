# revision 29019
# category Package
# catalog-ctan /macros/latex/contrib/underoverlap
# catalog-date 2013-02-03 19:03:00 +0100
# catalog-license lppl1.3
# catalog-version 0.0.1-r1
Name:		texlive-underoverlap
Version:	0.0.1.r1
Release:	5
Summary:	Position decorations over and under expressions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/underoverlap
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underoverlap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/underoverlap.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
