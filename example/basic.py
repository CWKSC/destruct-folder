from destructfolder.destructfolder import *

folderStructure =  [
    Folder("data",[
        TxtFolder("txt_folder1", key_for_contents="txt_folder1_key"),
        TxtFolder("txt_folder2", key_for_contents="txt_folder2_key"),
        TxtFolder("txt_folder3", key_for_contents="txt_folder3_key"),
    ]),
    Folder("cache", [
        TxtFolder("txt_folder4", key_for_contents="txt_folder4_key"),
        ForEachFolder("foreach_folder", key_for_path="foreach_folder_key_for_path", key_for_subfolder="foreach_folder_key", subfolder=
            TxtFolder("txt_folder5_inside_foreach_folder", key_for_contents="txt_folder5_inside_foreach_folder_key")
        ),
        TxtFolder("txt_folder6", key_for_contents="txt_folder6_key")
    ])
]

rootPath = Path(__file__).parent
buildFramework(rootPath, folderStructure)

folderDict = destructFolder(rootPath, folderStructure)

print(folderDict)
print()
print(folderDict["txt_folder1_key"])
print(folderDict["txt_folder2_key"])
print(folderDict["txt_folder3_key"])
print()
print(folderDict["txt_folder4_key"])
print(folderDict["foreach_folder_key"]["txt_folder_n1"])
print(folderDict["foreach_folder_key"]["txt_folder_n2"])
print(folderDict["foreach_folder_key"]["txt_folder_n3"])
print(folderDict["txt_folder6_key"])


