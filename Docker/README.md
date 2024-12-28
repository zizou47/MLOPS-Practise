
* Docker Image: A blueprint or template that contains the application, dependencies, and environment needed to run it. It’s static and read-only.

* Docker Container: A running instance of a Docker image. It’s dynamic, has a writable layer, and represents the actual execution of the application. 
* VM: Clones everything — the entire operating system along with the application and dependencies.
* Docker: Packages only the application and its dependencies, while sharing the host's OS kernel.
- This makes Docker more lightweight and faster compared to VMs, but VMs provide a more isolated and complete environment.
* to build a docker image :   docker build -t <name> .
* run docker image as container : docker run -p 5000:5000 <name>
 ps: docker images, ps (know how to list images)

