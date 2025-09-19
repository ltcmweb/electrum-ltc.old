#!/bin/bash

set -e

. $(dirname "$0")/build_tools_util.sh || (echo "Could not source build_tools_util.sh" && exit 1)

here="$(dirname "$(realpath "$0" 2> /dev/null || grealpath "$0")")"
CONTRIB="$here"
PROJECT_ROOT="$CONTRIB/.."

pkgname="mwebd"
info "Building $pkgname..."

(
    cd "$CONTRIB/mwebd"

    if [ "$BUILD_TYPE" = "wine" ] ; then
        CC=x86_64-w64-mingw32-gcc
        GOARCH=amd64
        GOOS=windows
    fi
    export CC GOARCH GOOS

    CGO_ENABLED=1 go build -buildmode=c-shared -o "$PROJECT_ROOT/electrum_ltc/libmwebd.so" . || fail "Could not build $pkgname"
    rm "$PROJECT_ROOT/electrum_ltc/libmwebd.h"
    info "libmwebd.so has been placed in the inner 'electrum_ltc' folder."
)
