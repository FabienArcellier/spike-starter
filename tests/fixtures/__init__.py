import os
import shutil
import tempfile

from decorator import contextmanager

SCRIPT_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))


@contextmanager
def clone_fixture(fixture_name, working_dir=None):
    tmp_prefix = "{}_{}".format(fixture_name, "_")
    working_directory = tempfile.mktemp(prefix=tmp_prefix) if not working_dir else working_dir
    template_working_directory = os.path.join(SCRIPT_DIRECTORY_PATH, fixture_name)

    if not os.path.isdir(template_working_directory):
        fixtures_list = [
            d
            for d in os.listdir(SCRIPT_DIRECTORY_PATH)
            if os.path.isdir(os.path.join(SCRIPT_DIRECTORY_PATH, d))
        ]
        raise Exception(f"the fixture {fixture_name} does not exists in fixtures : {fixtures_list}")

    shutil.copytree(template_working_directory, working_directory)
    yield working_directory

    shutil.rmtree(working_directory)
