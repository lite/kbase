PROJECT (main) 

set(CMAKE_CXX_FLAGS "-g")
set(CMAKE_EXE_LINKER_FLAGS "-framework Foundation")

set(SRC MethodSwizzling.mm NSString_MD5.mm main.mm)

# add_executable(main MACOSX_BUNDLE ${SRC})
add_executable(main ${SRC})


