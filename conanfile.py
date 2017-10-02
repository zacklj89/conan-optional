import os, shutil
from conans import ConanFile, CMake
from conans.tools import download, check_sha256, unzip

class OptionalConan(ConanFile):
    name = 'optional'
    version = '2.1.0'
    description = 'std::optional lightweight implementation'
    url = 'https://github.com/zacklj89/conan-optional'
    license = 'https://github.com/martinmoene/optional-lite/blob/master/LICENSE'
    settings = 'os', 'compiler', 'arch', 'build_type'
    exports_sources = 'CMakeLists.txt'
    generators = 'cmake'

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
        download(download_url, 'optional-lite-{!s}.zip'.format(self.version))
        check_sha256('optional-lite-{!s}.zip'.format(self.version),'d2b6f6f5e2a762119bdad963ee1392b22b85a138cced9505f4c006b13820d686')
        unzip('optional-lite-{!s}.zip'.format(self.version))
        os.unlink('optional-lite-{!s}.zip'.format(self.version))
        os.rename('optional-lite-{!s}'.format(self.version), 'optional')

    def build(self):
        cmake = self._run_cmake()    # rerun cmake
        cmake.build()

    def package(self):
        self.copy(pattern='*.hpp', dst='include/nonstd', keep_path=False)

    def package_id(self):
        self.info.header_only()
