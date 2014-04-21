# Truchas files in directory
#   functions

# List of files to  process
set(FUNC_FILES)

# List of files to add to the Truchas library
set(FUNC_SOURCE_FILES)

# Process target name
set(FUNC_TARGET_NAME ProcessTruchasFunctionFiles)


set(FUNC_FILES
        functions/function_namelist.F90
        functions/scalar_func_class.F90
        functions/const_scalar_func_type.F90
        functions/poly_scalar_func_type.F90
        functions/mpoly_scalar_func_type.F90
        functions/tabular_scalar_func_type.F90
        functions/fptr_scalar_func_type.F90
        functions/scalar_func_factories.F90
        functions/scalar_func_containers.F90
        functions/scalar_func_tools.F90
        functions/scalar_func_map_type.F90
        )

if(ENABLE_DYNAMIC_LOADING)
  list(APPEND FUNC_FILES functions/dl_scalar_func_type.F90)
endif()

set(FUNC_FPP_FLAGS 
        -I${TruchasExe_SOURCE_DIR}/utilities
	${Truchas_FPP_FLAGS})

# Process files
fortran_preprocess_files(FUNC_SOURCE_FILES
                         FILES ${FUNC_FILES}
			 FPP_EXECUTABLE ${Truchas_PREPROCESSOR}
			 FPP_FLAGS ${FUNC_FPP_FLAGS}
			 PROCESS_TARGET ${FUNC_TARGET_NAME})
set_source_files_properties(${FUNC_SOURCE_FILES} PROPERTIES
                            COMPILE_FLAGS -I${PGSLib_MODULE_DIR})

if(Fortran_COMPILER_IS_INTEL)
  set_source_files_properties(${FUNC_SOURCE_FILES} PROPERTIES
                              COMPILE_FLAGS "-standard-semantics -assume nostd_mod_proc_name")
endif()

list(APPEND Truchas_LIBRARY_SOURCE_FILES ${FUNC_SOURCE_FILES})		       
list(APPEND Truchas_PROCESS_TARGETS ${FUNC_TARGET_NAME})


