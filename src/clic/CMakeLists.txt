## fetch CLIc from repo release
include(FetchContent)

if(NOT DEFINED CLIC_REPO_URL)
  message(FATAL_ERROR "CLIC_REPO_URL is not set")
endif()

if(NOT DEFINED CLIC_REPO_TAG)
  message(FATAL_ERROR "CLIC_REPO_TAG is not set")
endif()

FetchContent_Declare(
  CLIc
  GIT_REPOSITORY ${CLIC_REPO_URL}
  GIT_TAG ${CLIC_REPO_TAG}
)
FetchContent_MakeAvailable(CLIc)
