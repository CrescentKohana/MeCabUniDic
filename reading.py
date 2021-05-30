# -*- coding: utf-8 -*-
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
# Mecab configured with UniDic dictionary.
#

import sys, os, subprocess

isMac = sys.platform.startswith("darwin")
isWin = sys.platform.startswith("win")

mecabArgs = ['--node-format=%m[%f[10]] ', '--eos-format=\n',
            '--unk-format=%m[] ']

supportDir = os.path.join(os.path.dirname(__file__), "support")

if sys.platform == "win32":
    si = subprocess.STARTUPINFO()
    try:
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    except:
        # pylint: disable=no-member
        si.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW
else:
    si = None

# Mecab
##########################################################################

def mungeForPlatform(popen):
    if isWin:
        popen = [os.path.normpath(x) for x in popen]
        popen[0] += ".exe"
    elif not isMac:
        popen[0] += ".lin"
    return popen

class MecabController(object):

    def __init__(self):
        self.mecab = None

    def setup(self):
        self.mecabCmd = mungeForPlatform(
            [os.path.join(supportDir, "mecab")] + mecabArgs + [
                '-d', supportDir, '-r', os.path.join(supportDir, "mecabrc")])
        os.environ['DYLD_LIBRARY_PATH'] = supportDir
        os.environ['LD_LIBRARY_PATH'] = supportDir
        if not isWin:
            os.chmod(self.mecabCmd[0], 0o755)

    def ensureOpen(self):
        if not self.mecab:
            self.setup()
            try:
                self.mecab = subprocess.Popen(
                    self.mecabCmd, bufsize=-1, stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    startupinfo=si)
            except OSError:
                raise Exception("Please ensure your Linux system has 64 bit binary support.")

# Init
##########################################################################

mecab = MecabController()

# Tests
##########################################################################

if __name__ == "__main__":
    expr = u"カリン、自分でまいた種は自分で刈り取れ"
    print(mecab.reading(expr).encode("utf-8"))
    expr = u"昨日、林檎を2個買った。"
    print(mecab.reading(expr).encode("utf-8"))
    expr = u"真莉、大好きだよん＾＾"
    print(mecab.reading(expr).encode("utf-8"))
    expr = u"彼２０００万も使った。"
    print(mecab.reading(expr).encode("utf-8"))
    expr = u"彼二千三百六十円も使った。"
    print(mecab.reading(expr).encode("utf-8"))
    expr = u"千葉"
    print(mecab.reading(expr).encode("utf-8"))
