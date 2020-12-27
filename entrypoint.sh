#!/bin/sh -l

#
# Copyright (C) 2020  Nightwind Future Industries Ltd. (NZ)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.
# If not, see <https://www.gnu.org/licenses/>.
#

# The following script was referenced from: https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
# And here: https://gist.github.com/jehiah/855086

# Parses the Argument Options
while [ "$1" != "" ]; do
  key="$1"
  data="$2"
  case $key in
    -n|--pkg_name)
    PKG_NAME="$data"
    shift # past argument
    shift # past value
    ;;
    -v|--pkg_version)
    PKG_VER="$data"
    shift # past argument
    shift # past value
    ;;
    -a|--pkg_arch)
    PKG_ARCH="$data"
    shift # past argument
    shift # past value
    ;;
    -m|--pkg_file_map)
    PKG_MAP="$data"
    shift # past argument
    shift # past value
    ;;
    -i|--input)
    PKG_IN_DIR="$data"
    shift # past argument
    shift # past value
    ;;
    -o|--output)
    PKG_OUT_DIR="$data"
    shift # past argument
    shift # past value
    ;;
    *)
      echo "ERROR: Invalid parameter key (\"$key\")"
      usage
      exit 1
esac
done

# Lists the Arguments that were found
echo ""
echo "Arguments Read from Entrypoint Script:"
echo "PACKAGE NAME  = ${PKG_NAME}"
echo "PACKAGE VERSION  = ${PKG_VER}"
echo "PACKAGE ARCH  = ${PKG_ARCH}"
echo "LAYOUT MAP FILE  = ${PKG_MAP}"
echo "INPUT DIRECTORY PATH  = ${PKG_IN_DIR}"
echo "OUTPUT DIRECTORY PATH  = ${PKG_OUT_DIR}"

# Runs the Main Application
echo ""
echo "Starting Debian Packer Application"
DP_ARGS="-n ${PKG_NAME} -v ${PKG_VER} -a ${PKG_ARCH} -m ${PKG_MAP} -i ${PKG_IN_DIR} -o ${PKG_OUT_DIR}"
if debpack ${DP_ARGS} ; then
  echo "Success"
else
  echo "App Failed"
fi