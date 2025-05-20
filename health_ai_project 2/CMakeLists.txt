cmake_minimum_required(VERSION 3.10)
project(HealthAI)

set(CMAKE_CXX_STANDARD 20)

include_directories(
    ${CMAKE_SOURCE_DIR}/include
    /opt/homebrew/include
)

add_executable(HealthAI main.cpp)

find_package(Threads REQUIRED)
target_link_libraries(HealthAI PRIVATE Threads::Threads)