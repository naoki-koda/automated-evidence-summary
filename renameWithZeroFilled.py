# -*- coding: utf-8 -*-

import os
import copy
import re


def main():
    images = getImagesName()
    renameImagesName(images)


def getImagesName():
    dirLists = os.listdir("src")
    dirLists_file = [
        f for f in dirLists if os.path.isfile(
            os.path.join(
                "src", f))]
    # dirLists_file.remove(".DS_Store")
    imagesName = copy.copy(dirLists_file)
    # print(imagesName)
    return imagesName


def renameImagesName(images):

    fill0Lengh = 9
    for image in images:
        baseName = re.sub('(?<=.)([^.]+$)', '', image).replace(".", "")
        extensionName = image.replace(baseName, "")
        while True:
            if(len(baseName) == fill0Lengh):
                break
            elif(len(baseName) >= fill0Lengh):
                print("画像ファイル：" + str(baseName) + "のファイル名が誤っています")
                break
            else:
                baseName = "0" + baseName

        beforeFileName = "./src/" + str(image)
        afterFileName = "./src/" + baseName + extensionName
        os.rename(beforeFileName, afterFileName)


if __name__ == "__main__":
    main()
