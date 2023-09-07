
## fetch CLIc from repo release
include(FetchContent)

FetchContent_Declare(
  CLIc
  GIT_REPOSITORY ${CLIC_REPO_URL}
  GIT_TAG ${CLIC_REPO_TAG}
)
FetchContent_MakeAvailable(CLIc)
