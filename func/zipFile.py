import os
import zipfile


def zip_file(src_dir):
    """
    压缩文件
    @param src_dir:
    @return:返回压缩文件的路径
    """
    try:

        zip_name = src_dir + '.zip'
        z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for dir_path, dir_names, file_names in os.walk(src_dir):
            fpath = dir_path.replace(src_dir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in file_names:
                z.write(os.path.join(dir_path, filename), fpath + filename)
        z.close()
        return zip_name
    except Exception as ex:
        print(ex)
