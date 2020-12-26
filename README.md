# Debian Packer

**Note:** This repository is still a _work in progress_.

This application & GitHub Action can build & generate DEBIAN packages with ease. Simply provide the resources, 
a configured file map and this app will generate for you a DEBIAN package with ease!
*Debian Packer* is ideal for applications that require DEBIAN package to be dynamically generated, such as 
part of an automated release with CI/CD.

## Dependencies
The following dependencies are required for this application to run:
* [json](https://docs.python.org/3/library/json.html) - Built-in
* [click](https://click.palletsprojects.com/en/7.x/)

They can simply be installed using `pip install [dependency name] ..`

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
