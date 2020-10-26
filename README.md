# Usage

First build the docker image. In the root of the repo run
```
dts devel build -f
```

Record the name of the built image.

To run the image
```
docker run --rm -v <directory containing bag>:/bags -e BAG_NAME="name of the bag file" <name of image built in the previous step>
```

For example

```
docker run --rm -v ~/bags/:/bags -e BAG_NAME="example_rosbag_H3.bag" duckietown/analyze-bags-rh3:v2-amd64
```
Would process the bag file `example_rosbag_H3.bag` in the directory `~/bags` using the built image called `duckietown/analyze-bags-rh3:v2-amd64`