from conans import ConanFile
from conans.tools import download, check_sha256

class NlohmannJsonConan(ConanFile):
    name = 'json'
    version = '2.1.0'
    description = 'JSON for Modern C++.'
    url = 'https://github.com/jjones646/conan-nlohmann-json'
    license = 'https://github.com/nlohmann/json/blob/v2.1.0/LICENSE.MIT'
    settings = None
    options = { 'no_exceptions': [True, False] }
    default_options = 'no_exceptions=False'

    def source(self):
        download_url = 'https://github.com/nlohmann/json/releases/download/v{!s}/json.hpp'.format(self.version)
        download(download_url, 'json.hpp')
        check_sha256('json.hpp', 'a571dee92515b685784fd527e38405cf3f5e13e96edbfe3f03d6df2e363a767b')

    def build(self):
        return  # do nothing - header only

    def package(self):
        self.copy(pattern='json.hpp', dst='include/nlohmann')

    def package_info(self):
        if self.options.no_exceptions:
            self.cpp_info.defines.append('JSON_NOEXCEPTION=1')

    def package_id(self):
        self.info.requires.clear()
