import os
import argparse

# ------------------------------------------------------------------------------
#       Arguments
# ------------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("-U", "--update", action="store_true", help="Update")
parser.add_argument("-C", "--configure", action="store_true", help="Force Configure")
parser.add_argument("-B", "--build", action="store_true", help="Build")
parser.add_argument("-R", "--run", action="store_true", help="Run")
args = parser.parse_args()

# ------------------------------------------------------------------------------
#       Locations
# ------------------------------------------------------------------------------

build_root = "build"
dep_folder = ".3rdparty"

# ------------------------------------------------------------------------------
#       Dependencies
# ------------------------------------------------------------------------------

def dep(name, url, branch, dumb = False):
    path = f"{dep_folder}/{name}"

    if os.path.exists(f"{path}"):
        if args.update:
            print(f"  Updating [{name}]")
            os.system(f"cd \"{path}\" && git pull")
            os.system(f"cd \"{path}\" && git submodule update --depth 1 --recursive")
    else:
        print(f"  Cloning [{name}]")
        os.system(f"git clone -b {branch} {"" if dumb else "--depth 1"} --recursive {url} \"{path}\"")

dep("GLFW", "https://github.com/glfw/glfw.git", "master")
dep("GLAD", "https://github.com/Dav1dde/glad.git", "glad2")

# ------------------------------------------------------------------------------
#       Configure / Build / Run
# ------------------------------------------------------------------------------

configure_ok = True

if ((not os.path.exists("build")) or args.configure):
    print("  Configuring [Debug]")
    configure_ok = 0 == os.system(f"cmake -B build -G Ninja -DVENDOR_DIR={dep_folder} -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_C_COMPILER=clang-cl -DCMAKE_CXX_COMPILER=clang-cl")

build_ok = True

if configure_ok and args.build:
    print("  Building [Debug]")
    build_ok = 0 == os.system("cmake --build build")

if build_ok and args.run:
    print("  Running [Debug]")
    os.system(".\\build\\Hello-World.exe")
