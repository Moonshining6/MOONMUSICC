import glob
from os.path import dirname, isfile


def list_all_modules():
    work_dir = dirname(__file)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("init.py")
    ]

    return all_modules


ALL_MODULES = sorted(list_all_modules())
__all = ALL_MODULES + ["ALL_MODULES"]
