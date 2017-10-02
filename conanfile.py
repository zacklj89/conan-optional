import os, shutil
from conans import ConanFile, CMake
from conans.tools import download, check_sha256, unzip

class OptionalConan(ConanFile):
    name = 'optional'
    version = '2.1.0'
    description = 'std::optional lightweight implementation'
    url = 'https://github.com/zacklj89/conan-optional'
    license = 'https://github.com/nlohmann/json/blob/v2.1.0/LICENSE.MIT'
    settings = None

    @property
    def _archive_dirname(self):
        return 'optional-{!s}'.format(self.version)

    def _get_build_dir(self):
        return os.getcwd()

    def _run_cmake(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(build_dir=self._get_build_dir(), source_dir=self.conanfile_directory)
        return cmake

## replace url and rename
    def source(self):
        download_url = 'https://github.com/martinmoene/optional-lite/archive/v{!s}.zip'.format(self.version)
        download(download_url, 'optional.zip')
        check_sha256('optional.zip','d2b6f6f5e2a7621119bdad963ee1392b22b85a138cced9505f4c006b13820d686')
        unzip('optional.zip')
        os.unlink('optional.zip')
        os.rename(self._archive_dirname, 'optional')

    def build(self):
        cmake = self._run_cmake()    # rerun cmake
        cmake.build()

    def package(self):
        self.copy(pattern='*.hpp', dst='include/')

    def package_id(self):
        self.info.header_only()
