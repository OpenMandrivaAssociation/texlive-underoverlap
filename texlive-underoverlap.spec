%global tl_name underoverlap
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1~r1
Release:	%{tl_revision}.1
Summary:	Position decorations over and under expressions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/underoverlap
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/underoverlap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/underoverlap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package overcomes TeX's inherent limitations in commands that place
decorations (such as braces) at arbitrary positions over and under
expressions, overlapping as necessary.

