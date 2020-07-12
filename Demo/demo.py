#!/usr/bin/env python
# coding: utf-8

import sys

sys.path.append('..')

from AutoGitignore import AutoGitignore

autoGI = AutoGitignore()

autoGI.run()

print('Directories where markers were found')
print(autoGI.passlst)

autoGI.save('result.gitignore')
