#include <print>

#include <glad/gl.h>
#include <GLFW/glfw3.h>

int main()
{
    std::println("Hello, world!");

    glfwInit();

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    auto window = glfwCreateWindow(1920, 1080, "Hello World", nullptr, nullptr);

    glfwMakeContextCurrent(window);
    auto version = gladLoadGL(glfwGetProcAddress);
    if (version) {
        std::println("Loaded GL version: {}.{}", GLAD_VERSION_MAJOR(version), GLAD_VERSION_MINOR(version));
    } else {
        std::println("Failed to load GL");
        glfwTerminate();
        return EXIT_FAILURE;
    }

    while (!glfwWindowShouldClose(window)) {
        int w, h;
        glfwGetFramebufferSize(window, &w, &h);

        glViewport(0, 0, w, h);
        glClearColor(0.2, 0.2, 0.2, 1);
        glClear(GL_COLOR_BUFFER_BIT);

        glfwSwapBuffers(window);

        glfwWaitEvents();
    }

    glfwTerminate();
}
