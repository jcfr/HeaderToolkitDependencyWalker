HeaderToolkitDependencyWalker
=========

Overview
--------

Think of HeaderToolkitDependencyWalker as an easy way to discover on which toolkit library (i.e [ITK][itk], [VTK][vtk] or [CTK][ctk]) your Cpp project is depending on.

Usage
-----

Quick examples:

    $ cd ~/Projects/Slicer4/Libs/MRML/Core
    $ header_toolkit_dependency_walker.py --toolkit-source-directory=~/Projects/Slicer4-Superbuild-Debug/VTK
    Common
    Filtering
    Graphics
    Hybrid
    IO
    Imaging
    Rendering

Simple.

Note also that passing the `--extra-verbose` option will provide you with more details:

    $ cd ~/Projects/Slicer4/Libs/MRML/Core
    $ header_toolkit_dependency_walker.py --toolkit-source-directory=~/Projects/Slicer4-Superbuild-Debug/VTK --extra-verbose
    3048 headers found in [/home/jchris/Projects/Slicer4-Superbuild-Debug/VTK] using [*.h]
    2966 entries added to 'Header -> Library' map 
    Found 98 files walking [.] using [*.h] pattern
    Found 188 files walking [.] using [*.cxx] pattern
    Found 0 files walking [.] using [*.cpp] pattern
    -------------------------------------------------- -------------------------------------------------- --------------------
    Project Header                                     Toolkit Header                                     Toolkit Library
    -------------------------------------------------- -------------------------------------------------- --------------------
    vtkImageAccumulateDiscrete.h                       vtkImageToImageFilter.h                            Filtering
    vtkMRMLScene.h                                     vtkObject.h                                        Common
    vtkCacheManager.h                                  vtkObject.h                                        Common
    vtkMRMLFiducial.h                                  vtkObject.h                                        Common
    [...]
    vtkObserverManagerTest1.cxx                        vtkIntArray.h                                      Common
    vtkMRMLTransformNodeTest1.cxx                      vtkGeneralTransform.h                              Common
    --------------------
    Toolkit Library
    --------------------
    Common
    Filtering
    Graphics
    Hybrid
    IO
    Imaging
    Rendering

Installation
------------

1. [Download the script](https://raw.github.com/jcfr/HeaderToolkitDependencyWalker/master/header_toolkit_dependency_walker.py).
2. Place it on your path. (I like to use `~/bin`)
3. Set it to be executable. (`chmod 755 ~/bin/header_toolkit_dependency_walker.py`)


Contributing
------------

Once you've made your great commits:

1. [Fork][fk] HeaderToolkitDependencyWalker
2. Create a topic branch - `git checkout -b my_branch`
3. Push to your branch - `git push origin my_branch`
4. Create an [Issue][is] with a link to your branch
5. That's it!


Meta
----

* Code: `git clone git://github.com/jcfr/HeaderToolkitDependencyWalker.git`
* Home: <http://jcfr.github.com>
* Bugs: <http://github.com/jcfr/HeaderToolkitDependencyWalker/issues>

License
-------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[fk]: http://help.github.com/forking/
[is]: http://github.com/jcfr/HeaderToolkitDependencyWalker/issues
[itk]: http://itk.org
[vtk]: http://vtk.org
[ctk]: http://commontk.org

