# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/envlab
# catalog-date 2009-01-23 15:11:09 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-envlab
Version:	1.2
Release:	6
Summary:	Addresses on envelopes or mailing labels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/envlab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envlab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envlab.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envlab.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for producing mailing envelopes and labels,
including barcodes and address formatting according to the US
Postal Service rules. Redefines the standard \makelabels
command of the LaTeX letter documentclass.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/envlab/envlab.cfg
%{_texmfdistdir}/tex/latex/envlab/envlab.sty
%doc %{_texmfdistdir}/doc/latex/envlab/elguide.pdf
%doc %{_texmfdistdir}/doc/latex/envlab/elguide.tex
%doc %{_texmfdistdir}/doc/latex/envlab/envlab.pdf
%doc %{_texmfdistdir}/doc/latex/envlab/readme.v12
#- source
%doc %{_texmfdistdir}/source/latex/envlab/elold.ins
%doc %{_texmfdistdir}/source/latex/envlab/envlab.drv
%doc %{_texmfdistdir}/source/latex/envlab/envlab.dtx
%doc %{_texmfdistdir}/source/latex/envlab/envlab.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 751490
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718341
- texlive-envlab
- texlive-envlab
- texlive-envlab
- texlive-envlab

