"""
Compile + Run Programs.

 - Transforms a Bryce File into a Python File.

History:
 - Jan.16.2026: Adapted by Bryce Summers from another his
                compiler for Transcript reports.
"""

import Bryce_Parser

def compile(src_file, dst_file):
    print(f"src: {src_file} -> dest: {dst_file}")
    
    with open(src_file, 'r', encoding="utf-8", errors="ignore") as f_src:
        with open(dst_file, 'w', encoding="utf-8", errors="ignore") as f_out:
            parser = Bryce_Parser.Bryce_Parser(f_src, f_out)
            parser.parseFile() # That's it!

compile("./Program_Bryce_Code/Program.txt", "./Program_Python/Program.py")