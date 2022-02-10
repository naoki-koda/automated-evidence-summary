# -*- coding: utf-8 -*-
import renameWithZeroFilled
import autoSummarizeEvidence


def main():
    # -------------------------------------------------------------------------------
    # 保存時のエクセルファイル名(要編集)
    saveFileName = "IT02_エビデンス_シナリオNo2.xlsx"
    # -------------------------------------------------------------------------------

    # srcフォルダの画像ファイルを0埋めでリネーム
    renameWithZeroFilled.main()
    # エビデンスまとめエクセル作成
    autoSummarizeEvidence.main(saveFileName)


if __name__ == "__main__":
    main()
