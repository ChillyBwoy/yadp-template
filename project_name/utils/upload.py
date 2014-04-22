# -*- coding: utf-8 -*-

import datetime
import hashlib
import time


def upload_name(file_name, keep_name=False):
    if keep_name:
        return file_name.encode('utf-8')
    else:
        fname = file_name.encode('utf-8')
        suffix = fname.split('.')[-1]
        stamp = int(time.time())
        md5 = hashlib.md5()
        md5.update(fname)
        return '.'.join([str(stamp), md5.hexdigest(), suffix]).lower()


def upload_to(path, prefix='uploads', keep_name=False):
    now = datetime.datetime.now()
    return lambda i, f: "%s/%s/%s" % (prefix, now.strftime(path),
                                      upload_name(f, keep_name))
