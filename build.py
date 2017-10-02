from conan.packager import ConanMultiPackager
import os

os.environ['CONAN_USERNAME'] = os.getenv('CONAN_USERNAME', 'jjones646')
os.environ['CONAN_CHANNEL'] = os.getenv('CONAN_CHANNEL', 'stable')
os.environ['CONAN_LOG_RUN_TO_FILE'] = os.getenv('CONAN_LOG_RUN_TO_FILE', '1')

def get_builds_with_options(builder):
    builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        builds.append([settings, {'json:no_exceptions':True}, env_vars, build_requires])
        builds.append([settings, {'json:no_exceptions':False}, env_vars, build_requires])
    return builds

if __name__ == '__main__':
    builder = ConanMultiPackager(
        gcc_versions=['5.2', '5.3', '5.4', '6.2'],
        apple_clang_versions=['6.1', '7.0', '7.3', '8.0'],
        visual_versions=['14'],
        archs=['x86_64', 'x86'],
        reference='json/2.1.0',
    )
    builder.add_common_builds(pure_c=False)
    builder.builds = get_builds_with_options(builder)
    builder.run()
