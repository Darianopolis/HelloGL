cmake_minimum_required(VERSION 3.30)
project(Hello-World)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

function(set_default_compile_options target)
    target_compile_options(${target} PUBLIC
        /clang:-std=c++26
        /clang:-Wall /clang:-Wextra /clang:-Wpedantic
        /clang:-Werror
        /clang:-Wno-missing-field-initializers
        /clang:-Wno-comment
        /clang:-Wno-language-extension-token
        )
endfunction()

set(VENDOR_DIR .3rdparty)
set(BUILD_SHARED_LIBS OFF)

# ------------------------------------------------------------------------------
#       GLFW
# ------------------------------------------------------------------------------

add_subdirectory(${VENDOR_DIR}/GLFW EXCLUDE_FROM_ALL)

# ------------------------------------------------------------------------------
#       GLAD
# ------------------------------------------------------------------------------

add_subdirectory(${VENDOR_DIR}/GLAD/cmake EXCLUDE_FROM_ALL)
glad_add_library(glad
    REPRODUCIBLE EXCLUDE_FROM_ALL LOADER
    API gl:core=4.6
    )

# ------------------------------------------------------------------------------
#       Hello-World
# ------------------------------------------------------------------------------

add_executable(Hello-World main.cpp)
set_default_compile_options(Hello-World)
target_link_libraries(Hello-World PUBLIC glfw glad)
