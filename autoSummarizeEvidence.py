# -*- coding: utf-8 -*-
import openpyxl
import os
from PIL import Image
import copy
import math
import re


def main(saveFileName):
    # 保存時のエクセルファイル名(要編集)
    saveFileName = saveFileName

    # 画像貼り付けサイズ（縦横比を維持して貼り付けるので高さのみ指定)
    height = 500
    # srcフォルダから画像ファイル一覧をリストで取得
    dirLists = os.listdir("src")
    dirLists_file = [
        f for f in dirLists if os.path.isfile(
            os.path.join(
                "src", f))]
    # macだと不要なファイル".DS_Store"が存在するのでリストから削除
    # dirLists_file.remove(".DS_Store")
    print(dirLists_file)
    imageLists = copy.copy(dirLists_file)

    # 画像ファイル一覧から数字の文字列だけ抽出(=数字以外の文字を削除)
    for index, noDirList in enumerate(dirLists_file):
        dirLists_file[index] = re.sub(r"[a-z]", "", dirLists_file[index])
        dirLists_file[index] = re.sub(r"[A-Z]", "", dirLists_file[index])
        dirLists_file[index] = dirLists_file[index].replace('_', '')
        dirLists_file[index] = dirLists_file[index].replace('.', '')

    # 要素に空文字だけのものがないかチェックし
    for index, noDirList in enumerate(dirLists_file):
        if len(dirLists_file[index]) == 0:
            dirLists_file.pop(index)
    createSheetNames = list(set(dirLists_file))

    print(createSheetNames)

    # エクセルシートをシート名=「No+番号」かつシートの左から番号の昇順で作成したいためソート
    sheetNames = sorted(createSheetNames, key=int)

    # エクセルブック新規作成
    wb = openpyxl.Workbook()

    # ケースNo毎のシート作成と画像貼り付け
    for index, itemNo in enumerate(sheetNames):
        # シート名=テストケースNoのエクセルシート作成
        sheetName = "No" + itemNo
        print(sheetName)
        wb.create_sheet(index=index, title=sheetName)
        sheet = wb[sheetName]
        # A1セルとM1セルに文字を挿入
        sheet['A1'] = "(現行)"
        sheet['M1'] = "(新)"
        oldStartInsertCol = 2
        newStartInsertCol = 2

        insertimages = [s for s in imageLists if itemNo + "_" in s]
        sortedImages = sorted(insertimages)
        print(sortedImages)

        for index, itemImageName in enumerate(sortedImages):
            print("itemImageName=" + itemImageName)
            openImage = Image.open("src/" + itemImageName)
            imgWidth, imgHeight = openImage.size
            whRatio = imgWidth / imgHeight

            print(itemImageName)
            img = openpyxl.drawing.image.Image("src/" + itemImageName)
            img.height = height
            img.width = height * whRatio
            cellHeight = math.ceil(height / 18)

            if "new" in itemImageName:
                insertCell = "M" + str(newStartInsertCol)
                newStartInsertCol += cellHeight
            elif "old" in itemImageName:
                insertCell = "A" + str(oldStartInsertCol)
                oldStartInsertCol += cellHeight
            sheet.add_image(img, insertCell)

    # エクセルブック作成時にデフォルトで作成されるシート（Sheet）を削除
    del wb['Sheet']
    wb.save("dst/" + saveFileName)
