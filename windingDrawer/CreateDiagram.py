import subprocess
import os
from yaml import Loader, load

from Winding import Winding
from Section import Section

def run_asy_file(asy_file, img_file=None, fmt="png"):
    """Runs asymptote code located in asy_file and writes to
    img_file if specified, otherwise use's asymptote's default
    output location. Returns tuple (IPython.display, stdout).
    """
    if not os.path.exists(asy_file):
        raise IOError("File not found: " + asy_file)
    if img_file is None:
        img_file = asy_file[:-3] + fmt

    asy_proc = subprocess.Popen(["asy", "-noView", "-f", fmt,
                                 "-o", img_file, asy_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

#    asy_proc = subprocess.Popen(["asy", "-noView", asy_file],
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE)


    asy_ret_code = asy_proc.wait()
    if asy_ret_code != 0:
        raise Exception(asy_proc.stderr.read())

    asy_stdout = asy_proc.stdout.read()

  #  if fmt == "svg":
  #      return SVG(filename=img_file), asy_stdout


def diagram():

    asy_commands = []

#    settings.outformat = "pdf";

    commands = """
settings.render = 16;
defaultpen(fontsize(10pt));
unitsize(1cm);

currentpen = linewidth(0.5);

draw((0, 0) -- (5, 0), arrow=Arrow);
draw((5, 0) -- (5, 0.5));
draw((5, 0.5) -- (0, 0.5), arrow=Arrow);

draw((0, 0.25) -- (5, 0.25), currentpen + dashed);
"""

    asy_commands = commands.split('\n')
    with open("test.asy","w") as asyFile:

        for command in asy_commands:
            asyFile.write(command + '\n')

    run_asy_file("test.asy", fmt="png")


winding = Winding("primary")

section = Section("sect1", 6,)

section.create_asy_commands()

with open("out.asy", "w") as outFile:
    outFile.write('settings.outformat = "pdf";\n')
    outFile.write('unitsize(1cm);\n')

    for cmd in section.asy_commands:
        outFile.write(cmd + '\n')


#diagram()


with open ("build.yml", "r") as yamlFile:

    build = load(yamlFile,Loader=Loader)

