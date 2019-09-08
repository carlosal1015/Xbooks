import os
import sys
from git import Repo, Actor
import time, datetime

from . import ccc

closeCode = 0

months = {
    "[01]": "A",
    "[02]": "B",
    "[03]": "C",
    "[04]": "D",
    "[05]": "E",
    "[06]": "F",
    "[07]": "G",
    "[08]": "H",
    "[09]": "I",
    "[10]": "J",
    "[11]": "K",
    "[12]": "L"
}


def close(shouldPush=True, err="", fail="", note="", success="", cyan=[], alert=""):
    """
    print failure,
    clean workspace
    exit with stderr
    """
    global closeCode

    if err != "":
        ccc.stderr(err)
        closeCode = 1
    if cyan != []:
        ccc.cyan(cyan[0], cyan[1])
    if note != "":
        ccc.note(note)
    if fail != "":
        ccc.fail(fail)
        closeCode = 1
    if alert != "":
        ccc.alert(alert)
    if success != "":
        ccc.success(success)
    # if shouldPush:
    #     update_Xbooksrc_transform()
    if "linux" in sys.platform:
        try:
            os.system("rm -r -f ./Xblog/")
            ccc.success("cleaning temp workspace")
        except Exception as err:
            ccc.fail=("cleaning temp workspace")
            closeCode = 1
    else:
        ccc.note("aborted cleaning temp workspace")
        closeCode = 1

    sys.exit(closeCode)
