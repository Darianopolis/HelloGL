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
#       ImGui
# ------------------------------------------------------------------------------
    
add_library(imgui)
target_sources(imgui
    PRIVATE
    ${VENDOR_DIR}/imgui/imgui.h
    ${VENDOR_DIR}/imgui/imgui.cpp
    ${VENDOR_DIR}/imgui/imgui_demo.cpp
    ${VENDOR_DIR}/imgui/imgui_tables.cpp
    ${VENDOR_DIR}/imgui/imgui_draw.cpp
    ${VENDOR_DIR}/imgui/imgui_widgets.cpp
    ${VENDOR_DIR}/imgui/backends/imgui_impl_opengl3.cpp
    ${VENDOR_DIR}/imgui/backends/imgui_impl_glfw.cpp
    )
target_include_directories(imgui PUBLIC ${VENDOR_DIR}/imgui)
target_link_libraries(imgui PUBLIC glfw)
target_link_libraries(imgui PUBLIC Opengl32.lib)

# ------------------------------------------------------------------------------
#       Hello-World
# ------------------------------------------------------------------------------

add_executable(Hello-World main.cpp)
set_default_compile_options(Hello-World)
target_link_libraries(Hello-World PUBLIC glfw glad imgui)
