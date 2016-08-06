from __future__ import unicode_literals

import sass
from pipeline.compilers import CompilerBase


class SASSCompiler(CompilerBase):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        with open(outfile, 'w') as f:
            f.write(sass.compile(filename=infile))

