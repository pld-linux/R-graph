%define		packname	graph

Summary:	A package to handle graph data structures
Name:		R-%{packname}
Version:	1.40.0
Release:	1
License:	Artistic 2.0
Group:		X11/Applications
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	a1d30ab931d4edf8b63e28ffc81a7057
URL:		http://www.bioconductor.org/packages/release/bioc/html/graph.html
BuildRequires:	R-BiocGenerics
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-BiocGenerics
Suggests:	R-cran-SparseM
Suggests:	R-cran-RUnit
Suggests:	R-RBGL
Suggests:	R-cran-XML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package that implements some simple graph handling capabilities.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/GXL
%{_libdir}/R/library/%{packname}/Scripts
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/perf
%{_libdir}/R/library/%{packname}/unitTests
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/BioC_graph.so
