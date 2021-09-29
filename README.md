# Debian Packer

**Note:** This repository is still a _work in progress_.

![Debian Packer Example](https://github.com/Nightwind-Developments/debian-packer/workflows/Debian%20Packer%20Example/badge.svg?branch=main)

## Contents
1. [Description](#description)
1. [Usage](#usage)
   1. [Input Parameters](#input-parameters)
   1. [Output Variables](#output-variables)
1. [Dependencies](#dependencies)
1. [Contributors](#contributors)
1. [Copyright & Licensing](#copyright--licensing)

## Description
This application & GitHub Action can build & generate DEBIAN packages with ease. Simply provide the resources,
a configured file map and this app will generate for you a DEBIAN package with ease!
*Debian Packer* is ideal for applications that require DEBIAN package to be dynamically generated, such as
part of an automated release with CI/CD.

This GitHub Action and the software included is designed to used another one of our projects,
[Debian Control File Builder](https://github.com/Nightwind-Developments/debian-control-file-builder), which can be used to generate the required Debian Control File for this action.

## Usage

### Input Parameters
| Name          | Type   | Required | Default                           | Description |
|---------------|--------|----------|-----------------------------------|-------------|
| `input_dir` | String | Yes      | `${{ github.workspace }}/input/`  | Path to the directory with all the files to be included in the generated package |
| `layout_map_file`   | String | Yes       |                                   | Path to JSON configuration file with how to organise the build package directory |
| `package_name`   | String | Yes       |                                   | Name of the Package to be used in the file name |
| `package_version`   | String | Yes       |                                   | Version number of the Package to be used in the file name |
| `package_arch`   | String | No       |                                   | Architecture of the Package to be used in the file name |
| `output_dir` | String | No       | `${{ github.workspace }}/output/` | Directory path to where the generated package is intended to be saved |

Example use case for input parameters:
```yaml
  steps:
    - name: Step Name
      with:
        input-name: value
```

### Output Variables
| Name                | Type   | Description |
|---------------------|--------|-------------|
| `generated_package_path` | String | The configured path where the generated package is saved and can be retrieved |

Example use case for output variables:
```yaml
    steps:
    - name: Step Name
      id: step-id
      run: ./

    - name: Print Output Variable
      run echo "${{ steps.step-id.outputs.output_variable }}"
```

## Dependencies
The following dependencies are required for this application to run:
* [json](https://docs.python.org/3/library/json.html) - Built-in
* [click](https://click.palletsprojects.com/en/7.x/)

They can simply be installed using `pip install [dependency name] ..`

## Contributors
The following developers have contributed to this repository:
* [Asami De Almeida](https://github.com/RedHoodedWraith) - theengineer@redhoodedwraith.com

## Copyright & Licensing
Copyright (C) 2020  Nightwind Future Industries Ltd. (NZ) <https://nightwind-developments.co.nz/>
<hello@nightwind-developments.co.nz>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License,
or any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program, such as below this paragraph.
If those links are not accessible, see <https://www.gnu.org/licenses/>.

The license for code in this repository follows LGPL-3.0-or-later.
* [GNU Lesser General Public License](/COPYING.LESSER)
* [GNU General Public License](/COPYING)
