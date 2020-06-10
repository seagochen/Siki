#!/bin/bash


dir_build="./build"
dir_dist="./dist"
dir_egg="./siki.egg-info"

if [ -d $dir_build ];then
      rm -rf $dir_build
fi

if [ -d $dir_dist ];then
      rm -rf $dir_dist
fi

if [ -d $dir_egg ];then
      rm -rf $dir_egg
fi

# now packaging python dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*