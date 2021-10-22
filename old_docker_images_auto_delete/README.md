# Auto Cleanup of Older Versions of Docker Images present in a System

During Containerized Deployment of applications, often some VMs are particularly allotted for building the Docker Containers. Whenever a new code change takes place, automatically the CI/CD pipeline triggers the build of a new container containing the latest codes.

Since the VMs have a fixed Disk Size, often storage issues arise, which lead to failure in the building of the containers leading to breakage in the CICD pipeline.

Therefore it's necessary to remove older versions of the container images on a regular basis to avoid storage issues.
A script has to be written, which would perform the clean-up process based on the image tags.

It will preserve all the docker images containing the latest tag.
For a particular repository, the tag with the highest number would be preserved.
A provision is made to add exception images that would be never stopped.

---
<br>  

## Rules Implemented:
   
    1. All images with 'latest' tag would not be touched.
    2. For a particular repository, the tag with the highest number would be preserved.
    3. A provision is made to add exception images which would be never stopped.