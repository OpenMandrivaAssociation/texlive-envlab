%global tl_name envlab
%global tl_revision 61937

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Addresses on envelopes or mailing labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/envlab
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/envlab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/envlab.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/envlab.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package for producing mailing envelopes and labels, including
barcodes and address formatting according to the US Postal Service
rules. Redefines the standard \makelabels command of the LaTeX letter
documentclass.

