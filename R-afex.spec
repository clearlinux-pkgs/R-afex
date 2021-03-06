#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-afex
Version  : 0.28.1
Release  : 36
URL      : https://cran.r-project.org/src/contrib/afex_0.28-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/afex_0.28-1.tar.gz
Summary  : Analysis of Factorial Experiments
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-car
Requires: R-lme4
Requires: R-lmerTest
Requires: R-pbkrtest
Requires: R-reshape2
BuildRequires : R-car
BuildRequires : R-lme4
BuildRequires : R-lmerTest
BuildRequires : R-pbkrtest
BuildRequires : R-reshape2
BuildRequires : buildreq-R

%description
mixed models. aov_ez(), aov_car(), and aov_4() allow specification of
         between, within (i.e., repeated-measures), or mixed (i.e., split-plot) 
         ANOVAs for data in long format (i.e., one observation per row),
         automatically aggregating multiple observations per individual and cell

%prep
%setup -q -c -n afex
cd %{_builddir}/afex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610486699

%install
export SOURCE_DATE_EPOCH=1610486699
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library afex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library afex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library afex
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc afex || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/afex/DESCRIPTION
/usr/lib64/R/library/afex/INDEX
/usr/lib64/R/library/afex/Meta/Rd.rds
/usr/lib64/R/library/afex/Meta/data.rds
/usr/lib64/R/library/afex/Meta/features.rds
/usr/lib64/R/library/afex/Meta/hsearch.rds
/usr/lib64/R/library/afex/Meta/links.rds
/usr/lib64/R/library/afex/Meta/nsInfo.rds
/usr/lib64/R/library/afex/Meta/package.rds
/usr/lib64/R/library/afex/Meta/vignette.rds
/usr/lib64/R/library/afex/NAMESPACE
/usr/lib64/R/library/afex/NEWS
/usr/lib64/R/library/afex/R/afex
/usr/lib64/R/library/afex/R/afex.rdb
/usr/lib64/R/library/afex/R/afex.rdx
/usr/lib64/R/library/afex/data/Rdata.rdb
/usr/lib64/R/library/afex/data/Rdata.rds
/usr/lib64/R/library/afex/data/Rdata.rdx
/usr/lib64/R/library/afex/doc/afex_analysing_accuracy_data.R
/usr/lib64/R/library/afex/doc/afex_analysing_accuracy_data.Rmd
/usr/lib64/R/library/afex/doc/afex_analysing_accuracy_data.html
/usr/lib64/R/library/afex/doc/afex_anova_example.R
/usr/lib64/R/library/afex/doc/afex_anova_example.Rmd
/usr/lib64/R/library/afex/doc/afex_anova_example.html
/usr/lib64/R/library/afex/doc/afex_mixed_example.R
/usr/lib64/R/library/afex/doc/afex_mixed_example.Rmd
/usr/lib64/R/library/afex/doc/afex_mixed_example.html
/usr/lib64/R/library/afex/doc/afex_plot_introduction.R
/usr/lib64/R/library/afex/doc/afex_plot_introduction.Rmd
/usr/lib64/R/library/afex/doc/afex_plot_introduction.html
/usr/lib64/R/library/afex/doc/afex_plot_supported_models.R
/usr/lib64/R/library/afex/doc/afex_plot_supported_models.Rmd
/usr/lib64/R/library/afex/doc/afex_plot_supported_models.html
/usr/lib64/R/library/afex/doc/index.html
/usr/lib64/R/library/afex/doc/introduction-mixed-models.pdf
/usr/lib64/R/library/afex/doc/introduction-mixed-models.pdf.asis
/usr/lib64/R/library/afex/extdata/output_afex_plot_mixed_vignette.rda
/usr/lib64/R/library/afex/extdata/output_mixed_vignette.rda
/usr/lib64/R/library/afex/extdata/outputs_glmm_vignette.rda
/usr/lib64/R/library/afex/extdata/plots_brms.rda
/usr/lib64/R/library/afex/extdata/plots_rstanarm.rda
/usr/lib64/R/library/afex/extdata/tmb_example_fit.rda
/usr/lib64/R/library/afex/help/AnIndex
/usr/lib64/R/library/afex/help/afex.rdb
/usr/lib64/R/library/afex/help/afex.rdx
/usr/lib64/R/library/afex/help/aliases.rds
/usr/lib64/R/library/afex/help/figures/README-unnamed-chunk-17-1.png
/usr/lib64/R/library/afex/help/figures/README-unnamed-chunk-18-1.png
/usr/lib64/R/library/afex/help/figures/README-unnamed-chunk-19-1.png
/usr/lib64/R/library/afex/help/figures/README-unnamed-chunk-6-1.png
/usr/lib64/R/library/afex/help/figures/README-unnamed-chunk-7-1.png
/usr/lib64/R/library/afex/help/paths.rds
/usr/lib64/R/library/afex/html/00Index.html
/usr/lib64/R/library/afex/html/R.css
/usr/lib64/R/library/afex/tests/testthat.R
/usr/lib64/R/library/afex/tests/testthat/afex_aov_16_1.rda
/usr/lib64/R/library/afex/tests/testthat/anova_hf_error.rda
/usr/lib64/R/library/afex/tests/testthat/lmm_old_object.rda
/usr/lib64/R/library/afex/tests/testthat/m_machines_lmerTest-pre3.0.rda
/usr/lib64/R/library/afex/tests/testthat/mixed_with_dot.rda
/usr/lib64/R/library/afex/tests/testthat/test-afex_aov.R
/usr/lib64/R/library/afex/tests/testthat/test-afex_plot-basics.R
/usr/lib64/R/library/afex/tests/testthat/test-afex_plot-bugs.R
/usr/lib64/R/library/afex/tests/testthat/test-afex_plot-default-support.R
/usr/lib64/R/library/afex/tests/testthat/test-afex_plot-vignette.R
/usr/lib64/R/library/afex/tests/testthat/test-aov_car-basic.R
/usr/lib64/R/library/afex/tests/testthat/test-aov_car-bugs.R
/usr/lib64/R/library/afex/tests/testthat/test-aov_car-structural.R
/usr/lib64/R/library/afex/tests/testthat/test-assumption_tests.R
/usr/lib64/R/library/afex/tests/testthat/test-compare_2_vectors.R
/usr/lib64/R/library/afex/tests/testthat/test-emmeans-interface.R
/usr/lib64/R/library/afex/tests/testthat/test-lmerTest-support.R
/usr/lib64/R/library/afex/tests/testthat/test-mixed-bugs.R
/usr/lib64/R/library/afex/tests/testthat/test-mixed-effects.R
/usr/lib64/R/library/afex/tests/testthat/test-mixed-mw.R
/usr/lib64/R/library/afex/tests/testthat/test-mixed-structure.R
/usr/lib64/R/library/afex/tests/testthat/test-residuals.R
