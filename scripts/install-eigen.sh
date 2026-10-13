#!/usr/bin/env bash
# install-eigen.sh <install_prefix>
# Installs Eigen once, so that CLIc finds it with find_package(Eigen3) instead of cloning it from GitLab
# for every wheel it builds. CLIc accepts any Eigen >= 3.4; keep EIGEN_VERSION in sync with CLIC_EIGEN_TAG
# (the version CLIc downloads when none is found) so that every build uses the same Eigen.

INSTALL_PREFIX="${1:?Usage: $0 <install_prefix>}"
EIGEN_VERSION="5.0.1"
EIGEN_SHA256="e9c326dc8c05cd1e044c71f30f1b2e34a6161a3b6ecf445d56b53ff1669e3dec"
EIGEN_URL="https://gitlab.com/libeigen/eigen/-/archive/${EIGEN_VERSION}/eigen-${EIGEN_VERSION}.tar.gz"

set -e -x

WORK_DIR=$(mktemp -d)
ARCHIVE="${WORK_DIR}/eigen-${EIGEN_VERSION}.tar.gz"

curl -fsSL --retry 5 --retry-delay 10 "${EIGEN_URL}" -o "${ARCHIVE}"
if command -v sha256sum >/dev/null; then
    echo "${EIGEN_SHA256}  ${ARCHIVE}" | sha256sum -c -
else
    echo "${EIGEN_SHA256}  ${ARCHIVE}" | shasum -a 256 -c -
fi
tar -xzf "${ARCHIVE}" -C "${WORK_DIR}"

# Header-only: install the headers and the Eigen3Config.cmake package files, nothing to compile
cmake -S "${WORK_DIR}/eigen-${EIGEN_VERSION}" -B "${WORK_DIR}/build" \
    -DCMAKE_INSTALL_PREFIX="${INSTALL_PREFIX}" \
    -DEIGEN_BUILD_CMAKE_PACKAGE=ON \
    -DEIGEN_BUILD_TESTING=OFF \
    -DEIGEN_BUILD_BLAS=OFF \
    -DEIGEN_BUILD_LAPACK=OFF \
    -DEIGEN_BUILD_DEMOS=OFF \
    -DEIGEN_BUILD_DOC=OFF \
    -DEIGEN_BUILD_PKGCONFIG=OFF
cmake --install "${WORK_DIR}/build"

rm -rf "${WORK_DIR}"
