# destructfolder

Destruct folders and get data `txt`, `png`, `npy`

> [!NOTE]
> 
> It is created when I am doing some data processing work
>
> I need to read some data from `.png`, `.txt`
> 
> Reading data from different folder is trouble, repeated, and hard to maintain
>
> So I make a library for destruct folder, read data, and store into dict 

> [!NOTE]
>
> This is also my first time learning how to publish a python library
>
> https://pypi.org/project/destructfolder/
>
> In 2020, nowaday should have better way to publish
>
> Not longer maintain, just for fun
>
> If I restart this project, I will created a DSL for it or just use json 

## Exmaple:

File structure:

```
- data
    - txt_folder1
        1.txt
        2.txt
    - txt_folder2
        1.txt
        2.txt
    - txt_folder3
        1.txt
        2.txt
- cache
    - foreach_folder
        - txt_folder_n1
            1.txt
            2.txt
        - txt_folder_n1
            1.txt
            2.txt
        - txt_folder_n1
            1.txt
            2.txt
    - txt_folder4
        1.txt
        2.txt
    - txt_folder6
        1.txt
        2.txt
```

```python
from destructfolder import *

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
```

Output:

```
Loading TxtFolder contents (txt_folder1) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

Loading TxtFolder contents (txt_folder2) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

Loading TxtFolder contents (txt_folder3) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

Loading TxtFolder contents (txt_folder4) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

Loading TxtFolder contents (txt_folder_n1) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

Loading TxtFolder contents (txt_folder_n2) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

Loading TxtFolder contents (txt_folder_n3) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

Loading TxtFolder contents (txt_folder6) ...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 

{'txt_folder1_key': {'1': 'this is txt file in txt_folder1', '2': 'this is another txt file in txt_folder1'}, 'txt_folder2_key': {'1': 'txt file in txt_folder2', '2': 'another txt file in txt_folder2'}, 'txt_folder3_key': {'1': 'txt in txt_folder3', '2': 'another txt in txt_folder3'}, 'txt_folder4_key': {'1': 'this is txt file in txt_folder4', '2': 'this is another txt file in txt_folder4'}, 'foreach_folder_key_for_path': WindowsPath('D:/Develop/Python/DestructFolder/example/cache/foreach_folder'), 'foreach_folder_key': {'txt_folder_n1': {'txt_folder5_inside_foreach_folder_key': {'1': 'this is txt file in txt_folder_n1', '2': 'this is another txt file in txt_folder_n1'}}, 'txt_folder_n2': {'txt_folder5_inside_foreach_folder_key': {'1': 'this is txt file in txt_folder_n2', '2': 'this is another txt file in txt_folder_n2'}}, 'txt_folder_n3': {'txt_folder5_inside_foreach_folder_key': {'1': 'this is txt file in txt_folder_n3', '2': 'this is another txt file in txt_folder_n3'}}}, 'txt_folder6_key': {'1': 'this is txt file in txt_folder6', '2': 'this is another txt file in txt_folder6'}}

{'1': 'this is txt file in txt_folder1', '2': 'this is another txt file in txt_folder1'}
{'1': 'txt file in txt_folder2', '2': 'another txt file in txt_folder2'}
{'1': 'txt in txt_folder3', '2': 'another txt in txt_folder3'}

{'1': 'this is txt file in txt_folder4', '2': 'this is another txt file in txt_folder4'}
{'txt_folder5_inside_foreach_folder_key': {'1': 'this is txt file in txt_folder_n1', '2': 'this is another txt file in txt_folder_n1'}}
{'txt_folder5_inside_foreach_folder_key': {'1': 'this is txt file in txt_folder_n2', '2': 'this is another txt file in txt_folder_n2'}}
{'txt_folder5_inside_foreach_folder_key': {'1': 'this is txt file in txt_folder_n3', '2': 'this is another txt file in txt_folder_n3'}}
{'1': 'this is txt file in txt_folder6', '2': 'this is another txt file in txt_folder6'}
```
