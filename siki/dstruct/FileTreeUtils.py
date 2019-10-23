from siki.basics import FileUtils as fu
from siki.basics import SystemUtils as su
from siki.basics import Exceptions as excepts
from siki.dstruct.FileNodeTree import FileNodeTree


def _convert_path(path):
    if not fu.exists(path):
        raise excepts.InvalidParamException("path is not valid")

    if su.is_windows():
        return path.split("\\")
    else:
        return path.split("/")


def _merge_to_tree(f_tokens, main_tree):
    if len(f_tokens) <= 0:
        pass # do nothing

    tree = None
    for token in f_tokens:
        node = FileNodeTree(token)

        if tree is not None:
            tree.append_node(node)
        
        tree = node

    if tree is None:
        print("tree is NONE!")

    if main_tree is None:
        print("main tree is NONE!")

    # back to the top
    while tree.root is not None:
        tree = tree.root

    if type(main_tree) is FileNodeTree:
        main_tree.merge_subtree(tree)
    else:
        raise InvalidParamException("main_tree is not FileNodeTree")


def traversal_dir(path, pattern="*"):
    """
    @param path: path to traversal or scanning
    @return: FileNodeTree with dirs and files 
    """

    files = fu.search_files(path, pattern)

    if len(files) <= 0:
        print("no file found")
        pass

    # file tree
    tree = FileNodeTree(_convert_path(path)[0])

    # append files to tree
    for f in files:
        _merge_to_tree(_convert_path(f), tree)

    return tree


if __name__ == "__main__":
    tree = None

    if su.is_windows():
        tree = traversal_dir(r"D:\Repository\Siki", r"\.py$")
    else:
        tree = traversal_dir("/mnt/d/Repository/Siki", r"\.py$")

    files = tree.only_files()
    for f in files:
        print(f)
    

