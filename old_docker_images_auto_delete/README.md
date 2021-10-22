# Auto Cleanup of Older Versions of Docker Images present in a System

During Containerized Deployment of applications, often some VMs are particularly allotted for building the Docker Containers. Whenever a new code change takes place, automatically the CI/CD pipeline triggers the build of a new container containing the latest codes.

Since the VMs have a fixed Disk Size, often storage issues arise, which lead to failure in the building of the containers leading to breakage in the CICD pipeline.

Therefore it's necessary to remove older versions of the container images on a regular basis to avoid storage issues.

**This script will preserve all the docker images containing the latest tag.
For a particular repository, the tag with the highest number would be preserved.
A provision is made to add exception images that would be never stopped.**

## Setup instructions

Make sure to have Docker Installed in your System.  
Run the `main.py` file.  


## Detailed explanation of script

- All images with 'Alpine, Buster, Slim & Latest' tag would not be touched.  
- For a particular repository, the tag with the highest number would be preserved.  
- A provision is made to add exception images which would be never stopped.

## Output

```
Deleting <Old Docker Image Name:Version>...
```

## Author(s)

Avik Kundu

## Disclaimer

Be Careful Before Running this code.   
Docker Image deletion cannot be reverted back.