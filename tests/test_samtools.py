# Copyright (C) 2016 by Per Unneberg
from os.path import join, basename
import shutil
import subprocess as sp
import pytest

samtools = pytest.mark.skipif(shutil.which("samtools") is None, reason="samtools not installed")

blacklist = []
rules = [(x) for x in pytest.rules.samtools if not basename(x).rsplit(".rule") in blacklist]

@pytest.mark.parametrize("rule", rules)
def test_samtools_list(rule):
    output = sp.check_output(['snakemake', '-s', rule, '-l'])

# @bwa
# @samtools
# @pytest.mark.parametrize("rule", params)
# def test_bwa_run(rule):
#     output = sp.check_output(['snakemake', '-s', rule, '-l'])
