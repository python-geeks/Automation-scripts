# Python Program to auto-delete old docker images
"""
    Rules:
    1. All images with 'latest' tag would not be touched.
    2. For a particular repository, the tag with
        the highest number would be preserved.
    3. A provision is made to add exception images
         which would be never stopped.
"""

import subprocess as sp
import re
import operator
import itertools


class DeleteImage:
    """
    Deleting Old Docker Images
    """
    def __init__(self):
        self.img_list = []
        self.hash_list = []

    def get_all(self):
        """
        Storing All the Docker Image Details Found on the System to a File
        """
        file = open("temp.txt", "r+", encoding='utf-8')
        file.truncate(0)
        sp.run("sudo docker image list --format '{{.Repository}}~{{.Tag}}' >> temp.txt",shell=True , capture_output=True, check=True) # noqa
        file.close()

    def is_excluded(self, tag):
        """
        Add other exceptions here
        """
        # Excluding all the images with Alpine, Buster, Slim & Latest Tags
        reg = r"alpine|buster|slim|latest"
        flag = re.search(reg, tag)
        if flag is not None:
            return 0
        return 1

    def load_all(self):
        """
        Loading data from the File to the Python program
        """
        file = open("temp.txt", "r", encoding='utf-8')

        for line in file:
            line = line.rstrip("\n")
            image = line.split('~')
            if self.is_excluded(image[1]):

                regex = r"^(((\d+\.)?(\d+\.)?(\*|\d+)))(\-(dev|stage|prod))*$"
                match = re.search(regex, image[1])

                img_dict = {'Repository': image[0], 'Tag': match.group(2)}
                self.img_list.append(img_dict)
        file.close()

    def man_data(self):
        """
        Manipulating Data to perform the reqd operation
        """
        key = operator.itemgetter('Repository')
        b_key = [{'Repository': x, 'Tag': [d['Tag'] for d in y]}
        for x, y in itertools.groupby(sorted(self.img_list, key=key), key=key)] # noqa

        self.img_list.clear()
        self.img_list = b_key.copy()

    def sort_tag(self):
        """
        Sorting Tags according to the Version Numbers
        """

        for img in self.img_list:
            temp = img['Tag'].copy()

            for new, i in enumerate(img['Tag']):
                img['Tag'][new] = int(i.replace('.', ''))

            max_len = len(str(max(abs(x) for x in img['Tag'])))
            template_string = '{:<0' + str(max_len) + '}'
            final_list = []

            for new, i in enumerate(img['Tag']):
                final_list.append(template_string.format(i))

            for i in range(0, len(img['Tag'])):
                hash_map = {'TagsManipulated': final_list[i], 'TagsOriginal': temp[i]}  # noqa
                self.hash_list.append(hash_map)

            final_list.sort()

            img['Tag'].clear()
            img['Tag'].extend(final_list[:-1])

        print(self.hash_list)
        print(self.img_list)

    def hash_function(self, tag):
        """
        Hash Function for Error Detection
        """
        for hash_map in self.hash_list:
            if tag == hash_map['TagsManipulated']:
                temp = hash_map['TagsOriginal']
                break
            else:
                temp = 'Error in Manipulation'
        return temp

    def remove_image(self):
        """
        Running the Docker RMI Command to Delete the Older Versions
        """
        for img in self.img_list:
            if img['Tag']:
                for tag in img['Tag']:
                    val = self.hash_function(tag)
                    image_url = img['Repository'] + ":" + val
                    print("Deleting Image : " + image_url)
                    sp.run("sudo docker rmi " + image_url,shell=True,capture_output=True , check=True) # noqa


# Main Function
if __name__ == "__main__":

    docker = DeleteImage()
    docker.get_all()
    docker.load_all()
    docker.man_data()
    docker.sort_tag()
    docker.remove_image()
